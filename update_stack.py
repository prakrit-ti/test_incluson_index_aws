import boto3

cf_client = boto3.client('cloudformation', region_name='us-east-1')

cf_client.update_stack(
    StackName='demo-stack-prti',
    UsePreviousTemplate=True,
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