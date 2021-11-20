import subprocess
subprocess.run("python testing.py 2> log.txt", shell=True)

from email_testoutcome import send_email
send_email("Test results FeedbackApp", "./log.txt")