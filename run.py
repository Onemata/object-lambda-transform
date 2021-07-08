from io import BytesIO
import pyarrow.parquet as pq
import boto3
import pandas as pd
import os

s3_client = boto3.client('s3')
# Read CSV directly using the bucket
pd.read_csv(s3_client.get_object(
    Bucket=os.environ['BUCKET_NAME'],
    Key='weather.csv'
)['Body'])

# Read CSV using the Lambda Access Point
df=pd.read_csv(s3_client.get_object(
    Bucket=os.environ['LAP_ARN'],
    Key='weather.csv'
)['Body'])
#print(len(df.index))
#print(df.head)
#print(df.describe())

# Read *Parquet* using the Lambda Access Point - dynamically generated!
df=pd.read_parquet(BytesIO(s3_client.get_object(
    Bucket=os.environ['LAP_ARN'],
    Key='weather.parquet'
)['Body'].read()))
#
print(df.head())
