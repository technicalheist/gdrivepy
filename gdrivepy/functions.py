from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.http import MediaFileUpload

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/drive']

def auth(credential_path):
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

    service = build('drive', 'v3', credentials=creds)
    return service

def listFiles(service):
        # Call the Drive v3 API
    results = service.files().list(
        pageSize=10, fields="nextPageToken, files(id, name)").execute()
    items = results.get('files', [])
    data = [];
    if not items:
        output = {}
        output['status'] = 'error'
        output['message']='No File Found'
        data.append(output)
        return data
    else:
        for item in items:
            data.append(item)
    return {
    'status':'ok', 
    'message':'File Found', 
    'data':data
    }

def upload(service,new_name,file_path, mime, parents=False):
    if parents == False:
        file_metadata = {'name': new_name}
    else:
        file_metadata = { 'name' : new_name, 'parents' : parents }
    media = MediaFileUpload(file_path, mime)
    file = service.files().create(body=file_metadata,
                                    media_body=media,
                                    fields='id').execute()
    return {
    'status':'ok',
    'message':'File Uploaded Successfully', 
    'file_id':file.get('id')
    }

def createFolder(service,new_name, parents=False):
    if parents == False:
        file_metadata = {'name': new_name, 'mimeType' : 'application/vnd.google-apps.folder'}
    else:
        file_metadata = { 'name' : new_name, 'mimeType' : 'application/vnd.google-apps.folder', 'parents' : parents }
    file = service.files().create(body=file_metadata,
                                    fields='id').execute()
    return {
    'status':'ok',
    'message':'File Uploaded Successfully', 
    'file_id':file.get('id')
    }

