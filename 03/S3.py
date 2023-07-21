import json
import requests
import boto3

data = requests.get("http://localhost:8080/planets.html").text

# create a S3 client, use environment variable for keys
s3 = boto3.client('s3')

# the bucket
bucket_name = "planets-content-unique-id"

bucket_policy = {
    'Version': '2012-10-17',
    'Statement': [{
        'Sid': 'AddPerm',
        'Effect': 'Allow',
        'Principal': '*',
        'Action': ['s3:GetObject'],
        'Resource': f"arn:aws:s3:::{bucket_name}/*"
    }]
}

bucket_policy = json.dumps(bucket_policy)

#create bucket, set
s3.create_bucket(Bucket=bucket_name )
s3.put_bucket_acl(Bucket=bucket_name, ACL='public-read')

s3.put_object(Bucket=bucket_name, Key='planet.html', Body=data, ACL="public-read")