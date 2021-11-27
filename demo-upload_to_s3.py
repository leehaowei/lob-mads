import boto3
import os

# credentials
access_key = 'access_key'
access_secret = 'access_secret'
bucket_name = 'lob-upload-hwl'

# create client instance
client_s3 = boto3.client(
    's3',
    aws_access_key_id=access_key,
    aws_secret_access_key=access_secret
)

# upload files to S3
# data_file_folder = '/Users/haowei/Desktop/aws-lob/data'
data_file_folder = os.path.join(os.getcwd(), 'data')
for file in os.listdir(data_file_folder):
    client_s3.upload_file(
        os.path.join(data_file_folder, file),
        bucket_name,
        file
    )
