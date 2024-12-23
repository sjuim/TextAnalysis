from box_sdk_gen import BoxClient, BoxDeveloperTokenAuth #ignore, is just a warning

# this file downloads all data from the Box folder to allow for easy updates to data (expected monthly)
def main(token: str):
    auth: BoxDeveloperTokenAuth = BoxDeveloperTokenAuth(token=token)
    client: BoxClient = BoxClient(auth=auth)


    #confirm that in correct folder
    print(client.folders.get_folder_by_id('158906423184').name)
    counter = 0
    for item in client.folders.get_folder_items('158906423184').entries:
        if counter >= 44: 
          print(item.name)
          #print(type(item))

          # how to just get file contents in type Optional[ByteStream]
          # ACCESS NOT WORKING
          # NEED TO FIX LATER
          # file_contents = client.downloads.download_file(item.id)

          # with open(file_contents) as f:
          #   file_like_object = io.BytesIO(file_contents)
          #print(file_contents)

          # how to download file contents locally
          with open(item.name, 'wb') as open_file:
            client.downloads.download_file_to_output_stream(item.id, open_file)
            open_file.close()
        counter += 1

    # print("Number of files: " + str(counter)) #60 files, confirms that all files accessed via the loop

    # find ids for top level folders
    # for item in client.folders.get_folder_items('0').entries:
    #     print(item.name + ": " + item.id)

if __name__ == '__main__':
    main('OpMhQHLFVBl8ctMheRlQTZn1PzobRyqK') # my developer token on box