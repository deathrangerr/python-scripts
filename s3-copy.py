import boto3
import datetime 
from datetime import date, timedelta
import subprocess
import os 
import sys
import shutil
import re

today = date.today()
d = datetime.timedelta(days = 2)
#start = today - timedelta(days=today.weekday())
start = today - d
today = str(today)
start = str(start)
bad = ['-']

for i in bad :
    start = start.replace(i, '')
print(start)

aws_bucket = "new-test1111"
localfile = 'D:\\Desktop\\' + str(start)
#print(localfile)

#def upload_aws( localfile, start, access_key=aws_access_key_id, secret_key=aws_secret_access_key, bucket_name=aws_bucket):
#    s3 = boto3.client('s3', aws_access_key_id=access_key,aws_secret_access_key=secret_key)

copy = "aws s3 cp " + str(start) + " s3://new-test1111/" + str(start) +  " --recursive" 
#print(copy)

subprocess.call (copy, shell=True)

shutil.rmtree(localfile)
