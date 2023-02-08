import boto3

cf_client = boto3.client('cloudformation', region_name='us-east-1')

template_body = """
---
AWSTemplateFormatVersion: '2010-09-09'
Resources:
  MyBucket:
    Type: AWS::S3::Bucket
    Properties:
      BucketName: s3-bucket-prti
"""

cf_client.create_stack(
    StackName='demo-stack-prti',
    TemplateBody=template_body
)