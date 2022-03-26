from __future__ import print_function

import os.path
import sys
from pathlib import Path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload

sys.path.append(str(Path(__file__).resolve().parent.parent))

from core.utils import get_file_mime_type
from config import BASE_DIR

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/drive']


def upload_file(file_path: Path,parent_folder_id=None):
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists(BASE_DIR /'token.json'):
        creds = Credentials.from_authorized_user_file(BASE_DIR / 'token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
               BASE_DIR / 'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open(BASE_DIR / 'token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('drive', 'v3', credentials=creds)

        # Call the Drive v3 API
        file_metadata = {'name':file_path.name}
        
        if parent_folder_id:
            file_metadata['parents'] = [parent_folder_id]
        
        media = MediaFileUpload(file_path,
                                mimetype=get_file_mime_type(file_path),
                                resumable=True)
        file = service.files().create(body=file_metadata,
                                      media_body=media,
                                      fields='id').execute()
        
        return True
        
    except HttpError as error:
        # TODO(developer) - Handle errors from drive API.
        print(f'An error occurred: {error}')
        return False
    
if __name__ == '__main__':
    upload_file(None,None)