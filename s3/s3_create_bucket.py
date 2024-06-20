import boto3
from botocore.exceptions import ClientError
import logging


def create_bucket(bucket_name, region = None):
    """create a new bucket in the specified region.
    If region is left as None, the default region is US-East-1
    """

    try:
        if region is None:
            client = boto3.resource('s3')
            client.create_bucket(Bucket = bucket_name)
        else:
            client = boto3.resource('s3', region_name = region)
            location = {'LocationRestraint': region}
            client.create_bucket(Bucket = bucket_name, CreateBucketConfiguration = location)
    except ClientError as e:
        logging.error(e)
        print("Error! {}".format(str(e)))
        return False

    print("Bucket {} created!".format(bucket_name))
    return True
