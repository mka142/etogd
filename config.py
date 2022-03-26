from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve(strict=True).parent

BACKUP_DIR = BASE_DIR / 'backups'
SOURCES_HASHES_FILE = BASE_DIR / 'sources-hashes.json'

DOCKER = bool(int(os.environ.get('DOCKER',default=0)))
SOURCES_TO_BACKUP = os.environ.get('SOURCES_TO_BACKUP','')
GDRIVE_PARENT_FOLDER = os.environ.get("GDRIVE_PARENT_FOLDER",'')
REMOVE_LOCAL = os.environ.get("REMOVE_LOCAL",True)
SCHEDULE_TIME =  float(os.environ.get("SCHEDULE_TIME",'1480')) # in minutes
APPRISE_NOTIFICATIONS = os.environ.get("APPRISE_NOTIFICATIONS",'').split(" ")
BACKUP_WHEN_NO_CHANGE = bool(int(os.environ.get('BACKUP_WHEN_NO_CHANGE',default=0)))