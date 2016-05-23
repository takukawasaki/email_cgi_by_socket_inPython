#!/usr/local/bin/python3
import sys

FTP_SERVER_URL = 'ftp.kernel.org'

import ftplib

def test_ftp_connection(path, username, email):
    #Open ftp connection
    ftp = ftplib.FTP(path, username, email)

    #List the files in the /pub directory
    ftp.cwd("/pub")
    print ("File list at %s:" %path)
    files = ftp.dir()
    print (files)

    ftp.quit()

if __name__ == '__main__':
    a1 = sys.argv[1]
    test_ftp_connection(path=a1, username='anonymous',
    email='nobody@nourl.com',)
        