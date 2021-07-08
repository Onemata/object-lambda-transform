# Additional Setup Instructions

1. Run the following commands
```
# Install node
#    sudo apt install nodejs
#    Window's users might want: https://nodejs.org/dist/v14.17.3/node-v14.17.3-x64.msi
brew install node 

# Install "Serverless Framework"
#    npm install -g serverless
curl -o- -L https://slss.io/install | bash

# Install Serverless Framework Dependencies
sls plugin install -n serverless-python-requirements
```

2. Install and start Docker daemon

3. Run the following commands
```
npx serverless deploy
export LAP_ARN=arn:aws:s3-object-lambda:us-east-1:620889225884:accesspoint/object-lambda-transform-dev-lambda-ap
export LAP_NAME=object-lambda-transform-dev-lambda-ap
export BUCKET_NAME=object-lambda-transform-dev-620889225884-us-east-1
aws s3 cp data/weather.csv s3://${BUCKET_NAME}/
```

4. Install Anaconda3 (condas)

5. Run the following commands

```
conda create --name myenv
conda activate myenv
conda install -c conda-forge pyarrow
conda install -c anaconda boto3
conda install pandas

python3 run.py
```

It appears that it's working!


# object-lambda-transform

An S3 Object Lambda example, converting CSV to Parquet on the fly.

See the full article covering this example [here](https://eoins.medium.com/using-s3-object-lambdas-to-generate-and-transform-on-the-fly-874b0f27fb84)!

## Deployment

The deployment consists of a Lambda Function, IAM Role, Log Group, S3 Bucket and Access Points.

Deployment uses [The Serverless Framework](https://serverless.com).

```
npx serverless deploy
```

The bucket name and Lambda access point names are generated based on your account ID and region.

```
export BUCKET_NAME=object-lambda-transform-dev-1234567890123-us-east-1
export LAP_NAME=object-lambda-transform-dev-lambda-ap
```

## Running

A sample CSV file is included. To test the function, first copy the csv to your bucket.

```
aws s3 cp data/weather.csv s3://${BUCKET_NAME}/
```


