import os,sys
import logging

import schedule,time

from core.utils import (
    current_time_suffix_for_file,
    make_archive,
    extract_sources_dirs,
    )
from core.hashes import source_hashes
from core.gdrive import upload_file,refresh_token
from core.notify import notify
import config

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler('export-to-google-drive.log'),
        logging.StreamHandler(sys.stdout)
    ]
)

soh = source_hashes(config.SOURCES_HASHES_FILE)

def main(source_to_be_zipped,file_prefix,gdrive_parent_folder=None,remove=True):
    
    sources = extract_sources_dirs(config.SOURCES_TO_BACKUP)
    logging.info(sources)
    logging.info(f'Starting backup: {source_to_be_zipped}')
    
    if not soh.is_changed(source_to_be_zipped):
        logging.info('No changes detected in source')
        if config.BACKUP_WHEN_NO_CHANGE:
            pass
            logging.info('Due to BACKUP_WHEN_NO_CHANGE=1 backup will be done.' \
                'If you don\'t want to backup sources thath doesn\'t changed' \
                'to the previus, set this option to 0')
        else:
            notify(
                config.APPRISE_NOTIFICATIONS,
                title="Skiped Google drive backup",
                body=f'Backup for source: "{source_to_be_zipped}"' \
                'was scheduled for now, but no changes was detected in source'
                )
            return None
    else:
        soh.save_current_source(source_to_be_zipped)
    
    zip_file_name = config.BACKUP_DIR / f'{file_prefix}_{current_time_suffix_for_file()}.zip'

    make_archive(source_to_be_zipped,zip_file_name)
    
    logging.info(f'Archive made in: {zip_file_name}')
    
    uploaded = upload_file(zip_file_name,gdrive_parent_folder)
    
    if remove:
        logging.info(f'Deleting archive: {zip_file_name}')
        os.remove(zip_file_name)
    
    if not uploaded:
        logging.error("File not uploaded")
        notify(config.APPRISE_NOTIFICATIONS,title='Google drive backup',body=f'Error during uploading archive:\n{zip_file_name}')
    else:
        logging.info("File uploaded successfully")
        notify(config.APPRISE_NOTIFICATIONS,title='Google drive backup',body=f'Successfully uploaded backup from archive:\n{zip_file_name}')
    
if __name__ == '__main__':
    logging.info(f'etogd started at {time.ctime()}')
    notify(config.APPRISE_NOTIFICATIONS,title="Google drive backup",body="etogd started")
    
    #if config.DOCKER:
    #    # create directory that is maped in docker/docker-compose
    #    os.makedirs(config.SOURCE_TO_BACKUP)
    sources = extract_sources_dirs(config.SOURCES_TO_BACKUP)
    
    def run():
        for zip_file_name,source_path in sources:
            main(
                source_path,
                zip_file_name,
                config.GDRIVE_PARENT_FOLDER,
                config.REMOVE_LOCAL
                )
    
    
    def refresh_google_token():
        logging.info('Refreshing google token')
        refreshed = refresh_token()
        
        if not refreshed:
            msg = 'Google token not refreshed. You need to change your toakn manually'
            logging.warning(msg)
            notify(config.APPRISE_NOTIFICATIONS,title='ERROR Google drive backup',body=msg)
            
        
    if config.SCHEDULE_TIME:
        schedule.every(config.SCHEDULE_TIME).minutes.do(run)
        schedule.every(5).minutes.do(refresh_google_token)
        
        while True:
            schedule.run_pending()
            time.sleep(1)
    else:
        sys.exit(run())
