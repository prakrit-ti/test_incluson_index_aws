import boto3

cf_client = boto3.client('cloudformation', region_name='us-east-1')

stack_name = "demo-stack-prti"

notification_arn = "arn:aws:sns:us-east-1:018066703918:my-topic"

response = cf_client.update_stack(
    StackName=stack_name,
    NotificationARNs=[
        notification_arn
    ]
)

print(response)