from gdrivepy import GDriver

if __name__ == '__main__':
    driver = GDriver('credentials.json') # Credential path

    # List All Files
    data = driver.list_files()
    print(data['data'])

    # Upload file
    data = driver.upload('test.pdf', './files/sample.pdf', 'application/pdf') # access, new name, file path , mime type
    print(data)

    # Create a folder
    data = driver.create_folder({'name':'FolderName'}); # access, new folder metadata
    print(data)
