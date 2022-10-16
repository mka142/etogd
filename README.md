# Archive to google drive
Simple python tool that allows you to archive files and folders to google drive

### Prepare environment
Firstly install required packages: `pip install -r requirements.txt` (best in python env). Then go to google cloud console, create project, enable Google Drive API and create credentials for Desktop. Copy credentials to project root directory and rename it to `credentials.json`.

To access your token.json you can run `python core/gdrive.py` or just use `main.py` with valid configuration

### Configuration
- SOURCES_TO_BACKUP
    comma separated list of paths to directorys or files that should be archived:
    `backup_name:/path/to/backup,backup_name2:/path2/to/backup`
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
- BACKUP_WHEN_NO_CHANGE (optional)
    if set to 1 backup will be done even there is no change in relation to previous backup
    `default: 0`

### Future goals:
- add ohter formats to make_archive
- add option to protect archive via password
