import os
import boto3
from botocore.client import ClientError
from os.path import join

# Set our input filepaths
# Should we so desire, we could break this out into an input variable
root_dir = os.path.abspath("..")
data_dir = join(root_dir, "data")
processed_data_dir = join(data_dir, "processed")
filename = "ufo_locations.pb"
processed_dataset = join(processed_data_dir, filename)

# S3 config
bucket_name = os.environ["s3_bucket"]
target_key = "input_data/train/{}".format(filename)

# Upload
s3 = boto3.resource("s3")
bucket = s3.Bucket(bucket_name)
try:
    s3.meta.client.head_bucket(Bucket=bucket.name)
except ClientError:
    bucket.create(CreateBucketConfiguration={
        "LocationConstraint": os.environ["s3_region"]
    })
bucket.upload_file(processed_dataset, target_key)
