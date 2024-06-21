import logging
import boto3
from botocore.exceptions import ClientError
import os


def upload_file(file_name, bucket, object_name=None):
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = os.path.basename(file_name)

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        print("Error! {}".format(str(e)))
        return False

    print("Files have been uploaded to {}".format(bucket))
    return True

def get_s3_keys(bucket):
    """get a list of keys from an s3 bucket
    """
    keys = []

    client = boto3.client('s3')
    response = client.list_objects_v2(Bucket = bucket)

    for obj in response["Contents"]:
        keys.append(obj['Key'])

    return keys
