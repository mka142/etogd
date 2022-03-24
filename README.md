# Archive to google drive
Simple python tool that allows you to archive files and folders to google drive

### Prepare environment
Firstly install required packages: `python install -r requirements.txt` (best in python env). Then go to google cloud console, create project, enable Google Drive API and create credentials for Desktop. Copy credentials to project root directory and rename it to `credentials.json`.

### Configuration
- SOURCE_TO_BACKUP
    path to directory or file that should be archived
- ZIP_FILE_NAME
    Prefix for archive name. Helpful to recognize archive later. Sufix of the file is just current date and time.
    `default: ''`
- GDRIVE_PARENT_FOLDER (optional)
    `ID` of google folder where archive should be uploaded
    `default ''` (home google drive directory)
- REMOVE_LOCAL (optional)
    Boolean 1 or 0 refer to remove local created archive after uploading it to Google Drive
    default: 1
- SCHEDULE_TIME (optional)
    describes how often will be your backup done (in minutes)
    `default: 1480`
- APPRISE_NOTIFICATIONS (optional)
    any valid space separated list of apprise services
    `default: ''`


### Future goals:
- configuration for docker
- add many sources to backup
- add ohter formats to make_archive
- add option to protect archive via password
