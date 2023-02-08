import boto3

sns_client = boto3.client('sns', region_name='us-east-1')

response = sns_client.create_topic(
    Name='my-topic'
)
