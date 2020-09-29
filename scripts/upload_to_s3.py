import os
import boto3
from botocore.client import ClientError
from os.path import join

# Set our input filepaths
# Should we so desire, we could break this out into an input variable
root_dir = os.path.abspath("..")
data_dir = join(root_dir, "data")
processed_data_dir = join(data_dir, "processed")
filename = "ufo_locations.csv"
processed_dataset = join(processed_data_dir, filename)

# S3 config
bucket_name = "acg-sm-demo-goyder"
target_key = filename

# Upload
s3 = boto3.resource("s3")
bucket = s3.Bucket(bucket_name)
try:
    s3.meta.client.head_bucket(Bucket=bucket.name)
except ClientError:
    bucket.create(CreateBucketConfiguration={
        "LocationConstraint": "ap-southeast-2"
    })

bucket.upload_file(processed_dataset, target_key)