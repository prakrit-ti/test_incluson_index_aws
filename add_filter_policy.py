import boto3
import json

# sns_client = boto3.client('sns', region_name='us-east-1')
import boto3

sns = boto3.resource('sns', region_name='us-east-1')
subscription = sns.Subscription('arn:aws:sns:us-east-1:018066703918:get-notifications-prti')

topic_arn = "arn:aws:sns:us-east-1:018066703918:get-notifications-prti"

filter_policy = {
    "aws:CloudFormation:Status": [
        "CREATE_COMPLETE",
        "CREATE_FAILED",
        "UPDATE_COMPLETE"
    ]
}
response = subscription.set_attributes(
    AttributeName='FilterPolicy',
    AttributeValue=str(filter_policy)
)
# sns_client.set_topic_attributes(
#     TopicArn=topic_arn,
#     AttributeName='FilterPolicy',
#     AttributeValue=json.dumps(filter_policy)
# )