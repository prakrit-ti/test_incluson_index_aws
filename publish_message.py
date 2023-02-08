# import boto3

# sns_client = boto3.client('sns', region_name='us-east-1')

# topic_arn = "arn:aws:sns:us-east-1:018066703918:get-notifications-prti"

# filter_policy = {
#     "aws:CloudFormation:Status": [
#         "CREATE_COMPLETE",
#         "CREATE_FAILED"
#     ]
# }

# sns_client.set_topic_attributes(
#     TopicArn=topic_arn,
#     AttributeName='Policy',
#     AttributeValue=str(filter_policy)
# )
import json
import boto3

client = boto3.client('sns', region_name='us-east-1')

message = "This is an SNS message with attributes version 2"
arn = "arn:aws:sns:us-east-1:018066703918:get-notifications-prti"

response = client.publish(
    TargetArn=arn,
    Message=json.dumps({'default': json.dumps(message)}),
    MessageStructure='json',
    MessageAttributes={
                        'myAttribute': {
                            'DataType': 'String',
                            'StringValue': 'myValue'
                        }
                    },
)