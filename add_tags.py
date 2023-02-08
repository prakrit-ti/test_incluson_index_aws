import boto3

s3 = boto3.client("s3")

bucket_name = "s3-bucket-prti"

tags = [
    {
        "Key": "Owner",
        "Value": "prakrit.raj@trilogy.com"
    },
    {
        "Key": "Project",
        "Value": "Inclusion Index"
    },
    {
        "Key": "Quarter",
        "Value": "Q1-2023"
    }
]

s3.put_bucket_tagging(
    Bucket=bucket_name,
    Tagging={
        "TagSet": tags
    }
)