from time import sleep
from gmail_reader import read_email_from_gmail

if __name__ == '__main__':
    
    while True:
        sleep(2)
        read_email_from_gmail()
