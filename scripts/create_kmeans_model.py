import sagemaker
import os
import pandas as pd
from os.path import join

# Define our config
role = os.environ["sm_role"]
instance_type = "ml.m5.large"
k = 10
bucket_name = os.environ["s3_bucket"]
filename = "ufo_locations.csv"

# Define our input data
root_dir = os.path.abspath("..")
data_dir = join(root_dir, "data")
processed_data_dir = join(data_dir, "processed")
df_ufo = pd.read_csv(join(processed_data_dir, filename), index_col=0)

# S3 config
input_key = "input_data/train/"
target_key = "{}/{}".format(input_key, filename)

# Create the K-means model
kmeans = sagemaker.KMeans(
    role=role,
    instance_type=instance_type,
    k=k,
    instance_count=1,
    data_location="s3://{}/{}".format(bucket_name, input_key),
    output_path="s3://{}/output".format(bucket_name)
)

# Define the training data
record_set = kmeans.record_set(df_ufo.to_numpy(dtype="float32"), channel="train")

kmeans.fit(record_set)
