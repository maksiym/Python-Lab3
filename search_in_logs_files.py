import re
import zipfile


def find_failed_requests():

    zip_log = zipfile.ZipFile('access.log.zip')
    log_file = zip_log.open('access.log.txt')



    zip_log.close()
