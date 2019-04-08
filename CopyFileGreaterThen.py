import boto3
from os import environ

if __name__ == "__main__":
    # Bucket Names (MinSize gets converted to Bytes to be compatible with object Sizes)
    DestBucketName = "destinationbucketwilkins30"
    SrcBucketName = "sourcebucketwilkins30"
    MinSize = .02 * 1024 * 1024

    # User credentials
    user = "AKIAWNAVMEGVNWWFY54Y"
    passkey = "r5MRRcbPf5CA3srRoxW0DTN7DwIKMNMhPJqVher4"

    # Get Buckets from s3 resource
    S3 = boto3.resource('s3', aws_access_key_id=user, aws_secret_access_key=passkey)
    S3Source = S3.Bucket(SrcBucketName)
    S3Destination = S3.Bucket(DestBucketName)


    # Gets files that are larger then minimum size
    FilesToMove = []
    for obj in S3Source.objects.all():
        if obj.size >= MinSize:
            FilesToMove.append(obj.key)

    # Copies found files from SrcBucket to DestBucket
    for key in FilesToMove:
        CopySource = {
            "Bucket" : SrcBucketName,
            "Key" : key
        }
        S3.meta.client.copy(CopySource, DestBucketName, obj.key)




