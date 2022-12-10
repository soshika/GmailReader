
import smtplib
import imaplib
import email
import redis_c
import os
import re
import traceback
from dotenv import load_dotenv
from symbol_converter import find_symbols, converter
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


def use_regex(input_text):
    pattern = re.compile(r"Your [a-zA-Z]+ alert was triggered", re.IGNORECASE)
    return pattern.match(input_text)

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

                    if email_subject != 'TradingView':
                        continue

                    r = redis_c.REDIS().r

                    exists = r.get(msg['Message-ID'])
                    if exists:
                        #end state!
                        return
                    else:
                        r.set(msg['Message-ID'], "True")
                        symbol = find_symbols(msg)
                        symbol = converter(symbol)
                        # send request to API
                    
                    print('-'*40)

    except Exception as e:
        traceback.print_exc() 
        print(str(e))

read_email_from_gmail()