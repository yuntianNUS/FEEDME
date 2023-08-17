import ftplib


class FileZilla:
    ftp = None

    def __init__(self):
        self.connect()

    def connect(self):
        ftpHost = "localhost"
        ftpPort = 21
        ftpUname = "user"
        ftpPass = "password"

        # create an FTP client instance, use the timeout(seconds) parameter for slow connections only
        self.ftp = ftplib.FTP(timeout=30)

        # connect to the FTP server
        self.ftp.connect(ftpHost, ftpPort)

        # login to the FTP server
        self.ftp.login(ftpUname, ftpPass)

    def grab_file(self, filename, folder_path):
        """retrieves file from server and then shoves it into this hardcoded directory

        Args:
            filename (_type_): _description_
        """
        self.connect()

        # touching a file to store the bytes of the files from server
        localfile = open(f"{folder_path}/{filename}", "wb")

        # calling the server to get the file and writes the bytes into the file as
        # defined in `localfile`
        self.ftp.retrbinary("RETR " + filename, localfile.write, 1024)

        self.ftp.quit()

    def upload_file(self, filename, folder_path):
        """
        stores file into server. root directory: i.e. /

        Args:
            filename (_type_): _description_
        """
        self.connect()
        self.ftp.storbinary("STOR " + filename, open(f"{folder_path}/{filename}", "r"))
        self.ftp.quit()
