import boto3
import os

# linode access keys to the bucket
linode_obj_config = {
    "aws_access_key_id": os.environ.get("AWS_ACCESS_KEY_ID"),
    "aws_secret_access_key": os.environ.get("AWS_SECRET_ACCESS_KEY"),
    "endpoint_url": os.environ.get("ENDPOINT_URL"),
}

# boto service
client = boto3.client("s3", **linode_obj_config)
