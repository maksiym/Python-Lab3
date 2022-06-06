import re
import zipfile


def find_failed_requests():

    zip_log = zipfile.ZipFile('access.log.zip')
    log_file = zip_log.open('access.log.txt')

    for line in log_file:
        if re.search('.*(((22/Mar/2009:(19:25:2[1-9]|19:25:[3-5]\d|19:2[6-9]:\d\d|19:[3-5]\d:\d\d'
                     '|2[0-3]:[0-5]\d:[0-5]\d))|'
                     '(2[3-8]/Mar/2009:[0-2]\d:[0-5]\d:[0-5]\d)|'
                     '(29/Mar/2009:((0\d|1[0-1]):[0-5]\d:[0-5]\d)|(12:00:00))) .* (4\d\d )(\d+))',
                     str(line)):
            print(line)

    zip_log.close()
