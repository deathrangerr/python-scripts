import subprocess
import smtplib
from email.mime.text import MIMEText

threshold = 80
partition = "/"

def report_via_email():
 msg = MIMEText("Server running out of disk space")
 msg["Subject"] = "Low disk space warning"
 msg["From"] = "sendemail"
 msg["To"] = "recieveremail"
 with smtplib.SMTP("smtp.gmail.com", 587) as server:
     server.ehlo()
     server.starttls()
     server.login("senderemail", "password")
     server.sendmail("sendemail","reciever" ,msg.as_string())

def check_once():
 df = subprocess.Popen(["df","-h"], stdout=subprocess.PIPE)
 for line in df.stdout:
     splitline = line.decode().split()
     if splitline[5] == partition:
         if int(splitline[4][:-1]) > threshold:
             report_via_email()
check_once() 
