import boto3
import os

from dotenv import load_dotenv

load_dotenv()

# linode access keys to the bucket
linode_obj_config = {
    "aws_access_key_id": os.getenv("AWS_ACCESS_KEY_ID"),
    "aws_secret_access_key": os.getenv("AWS_SECRET_ACCESS_KEY"),
    "endpoint_url": os.getenv("ENDPOINT_URL"),
}

# boto service
client = boto3.client("s3", **linode_obj_config)
