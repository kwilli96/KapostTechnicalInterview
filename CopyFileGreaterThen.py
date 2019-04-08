import boto3
from os import environ

if __name__ == "__main__":
    #Grabs bucket names from enviroment variable set in Dockerfile
    DestBucketName = environ["DestBucket"]
    SrcBucketName = environ["SrcBucket"]
    MinSize = float(environ["MinSize"]) * 1024 * 1024

    #Grabs user credentials from enviroment variables
    user = environ["username"]
    passkey = environ["passkey"]

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



