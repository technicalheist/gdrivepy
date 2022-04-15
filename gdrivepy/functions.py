import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.http import MediaFileUpload
import io

from typing import Optional, Any

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/drive']

class File:
    pass

class GDriver:
    def __init__(self, credential_path:str)->None:
        """Shows basic usage of the Drive v3 API.
        Prints the names and ids of the first 10 files the user has access to.
        """
        creds = None
        # The file token.pickle stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(credential_path, SCOPES)
                # creds = flow.run_local_server(port=0)
                creds = flow.run_console()
            # Save the credentials for the next run
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)

        self.service = build('drive', 'v3', credentials=creds)

    def list_files(
        self,
        query:str="",
        spaces:str="drive",
        page_size:int=10,
        fields:str="nextPageToken, files(id, name)"
    )->list[File]:
        page_token = None
        files = []
        while True:
            args = {
                "q" : query,
                "spaces" : spaces,
                "pageSize" : page_size,
                "fields" : fields,
            }
            results = self.service.files().list(**args).execute()
            items = results.get('files', [])
            files.append(items)

            # Next Page
            page_token = response.get('nextPageToken', None)
            if page_token is None:
                break
            return files

    def upload(
        self,
        file_metadata:dict[str,Any],
        file_path:str,
        mime:str,
        parents:bool=False,
        resumable:bool=True,
    )->Optional[int]:
        '''
        # For Google Sheets
        metadata = {'name':'My Cool Report','mimeType':'application/vnd.google-apps.spreadsheet'}
        GDriver.upload(file_metadata=metadata)
        '''
        media = MediaFileUpload(file_path, mime, resumable=resumable)
        args = {
            "body":file_metadata,
            "media_body":media,
            "fields":'id'
        }
        file = self.service.files(**args).create(**args).execute()
        return file.get('id',None)

    def create_folder(self, file_metadata:dict[str,Any])->Optional[File]:
        '''
        Accessing File in Folder
        folder_id = '0BwwA4oUTeiV1TGRPeTVjaWRDY1E'
        file_metadata = {
            'name': 'photo.jpg',
            'parents': [folder_id]
        }
        '''
        all_metadata = file_metadata|{'mimeType' : 'application/vnd.google-apps.folder'}
        file = self.service.files().create(body=all_metadata,fields='id').execute()
        if file:
            return file
        return None

    def update_file_location(self, file_id:str, folder_id:str)->None:
        # Retrieve the existing parents to remove
        file = drive_service.files().get(fileId=file_id,fields='parents').execute()
        previous_parents = ",".join(file.get('parents'))
        # Move the file to the new folder
        args = {
            "fileId":file_id,
            "addParents":folder_id,
            "removeParents":previous_parents,
            "fields":"id, parents",
        }
        file = self.service.files().update(**args).execute()
        return None

    def download(self, file_id:str)->None:
        request = self.service.files().get_media(fileId=file_id)
        fh = io.BytesIO()
        downloader = MediaIoBaseDownload(fh, request)
        done = False
        while done is False:
            status, done = downloader.next_chunk()
