import subprocess
from email_testoutcome import send_email

subprocess.run("python testing.py 2> log.txt", shell=True)
send_email("Test results FeedbackApp", "./log.txt")