from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve(strict=True).parent

BACKUP_DIR = BASE_DIR / 'backups'

SOURCE_TO_BACKUP = os.environ.get('SOURCE_TO_BACKUP','')
ZIP_FILE_NAME = os.environ.get("ZIP_FILE_NAME",'testfile')
GDRIVE_PARENT_FOLDER = os.environ.get("GDRIVE_PARENT_FOLDER",'')
REMOVE_LOCAL = os.environ.get("REMOVE_LOCAL",True)
SCHEDULE_TIME=  os.environ.get("SCHEDULE_TIME",1480) # in minutes
APPRISE_NOTIFICATIONS = os.environ.get("APPRISE_NOTIFICATIONS",'').split(" ")