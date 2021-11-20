import subprocess
from mailgun import send_message_mailgun
import json
import os
from datetime import datetime as dt

# RUN TESTING UNIT
subprocess.run("python testing.py 2> log.txt", shell=True)

# SET VARIABLES FOR MAIL
if "Users" in os.getcwd():
    cwd = str(os.path.dirname(__file__))
    secrets = cwd + '/secrets.json'
    with open(secrets) as f:
        secret = json.load(f)
    developer = secret["developer"]
    sender = secret["sender"]
    smtp_login = secret["smtp_login"]
    password = secret["password"]

else:
    developer = os.environ["developer"]
    sender = "foo@" + str(os.environ["MAILGUN_DOMAIN"])
    smtp_login = os.environ["MAILGUN_SMTP_LOGIN"]
    password = os.environ["MAILGUN_SMTP_PASSWORD"]


# DEFINE TEXT FOR MAIL
attachment_file = "./log.txt"
with open(attachment_file, 'r') as f:
    log_file_text = f.read()
if "OK" in str(log_file_text):
    status = "OK"
else:
    status = "ERROR"
date = str(dt.now().month)+"-"+str(dt.now().day)+"-"+str(dt.now().year)
text = log_file_text
subject = "Unittest result " + date + ":" + status

# SEND MAIL
send_message_mailgun(text, subject, developer, sender, smtp_login, password)