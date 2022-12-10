
import smtplib
import imaplib
import email
import os
import traceback
from dotenv import load_dotenv
# -------------------------------------------------
#
# Utility to read email from Gmail Using Python
#
# ------------------------------------------------

load_dotenv()

FROM_EMAIL = os.getenv('EMAIL')
FROM_PWD = os.getenv('PASSWORD') 
SMTP_SERVER = "imap.gmail.com" 
SMTP_PORT = 993

def read_email_from_gmail():
    try:
        mail = imaplib.IMAP4_SSL(SMTP_SERVER)
        mail.login(FROM_EMAIL,FROM_PWD)
        mail.select('inbox')

        data = mail.search(None, 'ALL')
        mail_ids = data[1]
        id_list = mail_ids[0].split()   
        first_email_id = int(id_list[0])
        latest_email_id = int(id_list[-1])

        for i in range(latest_email_id,first_email_id, -1):
            data = mail.fetch(str(i), '(RFC822)' )
            for response_part in data:
                arr = response_part[0]
                if isinstance(arr, tuple):
                    msg = email.message_from_string(str(arr[1],'utf-8'))
                    email_subject = msg['subject']
                    email_from = msg['from']
                    # print(msg.keys())
                    print(msg['Message-ID'])
                    # print('From : ' + email_from + '\n')
                    # print('Subject : ' + email_subject + '\n')
                    # print(msg)
                    print('-'*40)

    except Exception as e:
        traceback.print_exc() 
        print(str(e))

read_email_from_gmail()