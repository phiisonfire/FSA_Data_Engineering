import boto3

s3 = boto3.client("s3")
s3.upload_file("requirements.txt", "phinguyen98bucket01", "requirements.txt")