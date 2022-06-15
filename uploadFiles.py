import dropbox
import os

class TransferData ():

    def __init__( self, access_token ):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        f = open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)

def main():

    access_token = 'sl.BJkLdej83a1O15BCIeWHShGuvNHdx-rgVumyjwm62xq8hJbkHaGe-GotJgXqSaOXFeNGFCP3tidJx3tfsPyA8poBVh_mmtiAMfIa4Kv5R_AKvsTomq0RGCI2ZejaKqofkeBvtKCP8H4'

    file_from = input("Enter the path of the file to be uploaded ")
    file_to = input("Enter the full path to be uploaded to dropbox ")

    transfer_data = TransferData(access_token)

    transfer_data.upload_file(file_from, file_to)
    print("File has been uploaded")

main()
