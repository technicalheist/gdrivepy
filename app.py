from gdrivepy import auth,upload,createFolder,listFiles
if __name__ == '__main__':
    service = auth('YOUR-CREDENTIALS.json') # Credential path
    # List Files 
    data = listFiles(service)
    print(data['data'])

    #upload file
    # data = upload(service, 'test.pdf', './files/sample.pdf', 'application/pdf') #access, new name, file path , mime type
    # print(data)
    
    #Create a folder
    # data = createFolder(service, 'FolderName'); # access, new folder name
    # print(data)