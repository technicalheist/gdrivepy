gdrivepy : Google Drive Python API is a simplest way to access the google drive api
===================================================================================

this setup file simply uses the google drive api and work accordingly
---------------------------------------------------------------------

Features
--------

-  Authentication of users
-  Upload Files
-  Create Folders
-  List Files
-  More coming soon

How To Use
----------

::


    from gdrivepy import auth,upload,createFolder,listFiles
    if __name__ == '__main__':
        service = auth('credential/data.json') #credential Path
        # List Files 
        data = listFiles(service)
        print(data['data'])

        #upload file
        data = upload(service, 'test.pdf', './files/sample.pdf', 'application/pdf', 'FOLDER-ID-HERE(optional)') #access, new name, file path , mime type,folder_id (folder id of parent folder leave blank if root folder)
        print(data)
        
        #Create a folder
        data = createFolder(service, 'folderName' 'FOLDER-ID-HERE(optional)'); # access, new folder name, folder_id (folder id of parent folder leave blank if root folder)
        print(data)

