import re
import time
import zipfile


def find_failed_requests():

    zip_log = zipfile.ZipFile('access.log.zip')
    log_file = zip_log.open('access.log.txt')
    date_format = "%d/%b/%Y:%H:%M:%S"
    min_date = time.strptime("22/Mar/2009:19:25:21", date_format)
    max_date = time.strptime("29/Mar/2009:12:00:00", date_format)

    for line in log_file:
        log = re.search('.*((\d\d/Mar/2009:\d\d:\d\d:\d\d).*(4\d\d) (\d+))', str(line))
        if log:
            date = time.strptime(log.group(2), date_format)
            if min_date <= date <= max_date:
                print(line)

    zip_log.close()
