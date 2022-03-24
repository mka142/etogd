import os,sys
import logging

import schedule,time

from core.utils import zip_folder,current_time_suffix_for_file,make_archive
from core.gdrive import upload_file
from core.notify import notify
import config



def main(source_to_be_zipped,file_prefix,gdrive_parent_folder=None,remove=True):
    
    logging.info(f'Starting backup: {source_to_be_zipped}')
    
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
    def run():
        main(
            config.SOURCE_TO_BACKUP,
            config.ZIP_FILE_NAME,
            config.GDRIVE_PARENT_FOLDER,
            config.REMOVE_LOCAL)
    if config.SCHEDULE_TIME:
        schedule.every(config.SCHEDULE_TIME).minutes.do(run)
        while True:
            schedule.run_pending()
            time.sleep(1)
    else:
        sys.exit(run())
    