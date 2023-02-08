import boto3
sns = boto3.client('sns', region_name='us-east-1')
topic_arn = sns.create_topic(Name='get-notifications-prti')['TopicArn']

sns.subscribe(
    TopicArn=topic_arn,
    Protocol='https',
    Endpoint='https://webhook.site/0758c9b3-5a2f-48e7-8a01-97a8d76dd4d6'
)

template_body = """
---
AWSTemplateFormatVersion: '2010-09-09'
Resources:
  MyBucket:
    Type: AWS::S3::Bucket
    Properties:
      BucketName: s3-bucket-prti
"""

cf_client = boto3.client('cloudformation', region_name='us-east-1')
cf_client.update_stack(
    StackName='demo-stack-prti',
    TemplateBody=template_body,
    NotificationARNs=[topic_arn]
)



