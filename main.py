from search_in_logs_files import find_failed_requests


def main():
    print("Printing all failed requests between 23 and 30 March... ")
    find_failed_requests()


if __name__ == '__main__':
    main()
