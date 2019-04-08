import boto3
import sys
from os import environ

if __name__ == "__main__":
    # Grabs bucket names and minsize from variable passed into docker
    DestBucketName = sys.argv[1]
    SrcBucketName = sys.argv[2]
    MinSize = float(sys.argv[3]) * 1024 * 1024


    # Grabs user credentials from enviroment variables
    user = environ["username"]
    passkey = environ["passkey"]

    # Get Buckets from s3 resource
    S3 = boto3.resource('s3', aws_access_key_id=user, aws_secret_access_key=passkey)

    S3Source = S3.Bucket(SrcBucketName)
    S3Destination = S3.Bucket(DestBucketName)

    # Gets files that are larger then minimum size and copies them to the destination bucket
    for obj in S3Source.objects.all():
        if obj.size >= MinSize:
            CopySource = {
                "Bucket" : obj.bucket_name,
                "Key" : obj.key
            }
            S3.meta.client.copy(CopySource, DestBucketName, obj.key)




