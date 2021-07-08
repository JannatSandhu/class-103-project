import dropbox
import os

class TransferData:
    def __init__(self,access_token):
        self.access_token= access_token

        def upload_file(self, file_from, file_to):
            dbx=dropbox.Dropbox(self.access_token)
            
                         # enumerate local files recursively
            for root, dirs, files in os.walk(file_from):

                for filename in files:
                    # construct the full local path
                    local_path = os.path.join(root, filename)

                    # construct the full Dropbox path
                    relative_path = os.path.relpath(local_path, file_from)
                    dropbox_path = os.path.join(file_to, relative_path)
                    # upload the file
             

            with open(file_from, 'rb') as f:
                dbx.files_upload(f.read(), file_to)

def main():
    access_token = '*****'
    transferData = TransferData(access_token)
            
    file_from = 'text.txt'
    file_to = 'text.txt'

    transferData.upload_file(file_from, file_to)

if __name__ == '__main__':
    main()

    
