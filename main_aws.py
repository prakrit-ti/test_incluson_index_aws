import boto3

cf_client = boto3.client('cloudformation', region_name='us-east-1')

template_body = """
---
AWSTemplateFormatVersion: '2010-09-09'
Resources:
  MyBucket:
    Type: AWS::S3::Bucket
    Properties:
      BucketName: s3-demo-bucket
    Tags:
      - Key: Owner
        Value: prakrit.raj@trilogy.com
      - Key: Project
        Value: Inclusion Index
      - Key: Quarter
        Value: Q1-2023
"""
cf_client.create_stack(
    StackName='s3-demo-stack',
    TemplateBody=template_body,
    Tags=[
        {
            'Key': 'Owner',
            'Value': 'prakrit.raj@trilogy.com'
        },
        {
            'Key': 'Project',
            'Value': 'Inclusion Index'
        },
        {
            'Key': 'Quarter',
            'Value': 'Q1-2023'
        }
    ]
)