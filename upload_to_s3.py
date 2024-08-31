import boto3

# AWS credentials and S3 bucket information
aws_access_key_id = 'your-access-key-id'
aws_secret_access_key = 'your-secret-access-key'
bucket_name = 'your-s3-bucket-name'
file_to_upload = 'traffic_data.csv'

# Create an S3 client
s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)

# Upload the file to S3
try:
    s3.upload_file(file_to_upload, bucket_name, file_to_upload)
    print(f"Uploaded {file_to_upload} to {bucket_name}")
except Exception as e:
    print(f"Error uploading file: {str(e)}")
