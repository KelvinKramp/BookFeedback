import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from datetime import datetime as dt
from encryption import *
import json
import sys
import os
from urllib.parse import urlparse


msg = MIMEMultipart()
# DEFINE VARIABLES
if "Users" in os.getcwd():
    cwd = str(os.path.dirname(__file__))
    secrets = cwd+'/secrets.json'
    with open(secrets) as f:
      secret = json.load(f)
    fromaddr = decrypt_message(secret["email_email_comments"].encode('utf-8'))
    password = decrypt_message(secret["password_email_comments"].encode('utf-8'))
    toaddr = decrypt_message(secret["email_receive_comments"].encode('utf-8'))
    developer = secret["developer"]
    domain_name = secret["website_URL"]
    msg['From'] = urlparse(domain_name).netloc
else:
    fromaddr = os.environ["email_email_comments"]
    password = os.environ["password_email_comments"]
    toaddr = os.environ["email_receive_comments"]
    developer = os.environ["developer"]
    domain_name = os.environ["website_URL"]
    msg['From'] = urlparse(domain_name).netloc
msg['To'] = toaddr

date = str(dt.now().month)+"-"+str(dt.now().day)+"-"+str(dt.now().year)
filename = "Log-"+date+".txt"


def send_email(text, attachment_file):
    with open(attachment_file, 'r') as f:
        log_file_text = f.read()
    if "OK" in str(log_file_text):
        status = "OK"
    else:
        status = "ERROR"
    body = "" + date
    msg['Subject'] = "Unittest result " + date + ":" + status
    msg.attach(MIMEText(body, 'plain'))
    attachment = open(attachment_file, "rb")
    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    msg.attach(part)
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, password)
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()
    print("EMAIL SENT")

def send_email_developer(text, attachment_file):
    body = "This is the outcome of the test of this app on " + date
    msg['Subject'] = "Unittest result " + date + ":" + status
    msg.attach(MIMEText(body, 'plain'))
    attachment = open(attachment_file, "rb")
    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    msg.attach(part)
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, password)
    text = msg.as_string()
    server.sendmail(fromaddr, developer, text)
    server.quit()
    print("EMAIL SENT")

if __name__ == '__main__':
    send_email("Test results FeedbackApp", "./log.txt")
