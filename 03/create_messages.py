from urllib.request import urlopen
from bs4 import BeautifulSoup
import boto3
import botocore
# declare our keys (normally, don't hard code this)
access_key="AKIAYZPTISZNLPSDTBFF"
access_secret_key="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"
# create sqs client
sqs = boto3.client('sqs', "us-west-2",
 aws_access_key_id = access_key,
 aws_secret_access_key = access_secret_key)
# create / open the SQS queue
queue = sqs.create_queue(QueueName="PlanetMoreInfo")
print (queue)
# read and parse the planets HTML
html = urlopen("http://localhost:8080/planets.html")
bsobj = BeautifulSoup(html, "lxml")
planets = []
planet_rows = bsobj.html.body.div.table.findAll("tr", {"class": "planet"})
for i in planet_rows:
 tds = i.findAll("td")
 # get the URL
 more_info_url = tds[5].findAll("a")[0]["href"].strip()
 # send the URL to the queue
 sqs.send_message(QueueUrl=queue["QueueUrl"],
 MessageBody=more_info_url)
 print("Sent %s to %s" % (more_info_url, queue["QueueUrl"]))