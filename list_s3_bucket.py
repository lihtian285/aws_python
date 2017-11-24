# Get S3 bucket
# import boto3 , AWS SDK for python

import boto3
s3 = boto3.resource('s3')
for bucket in s3.buckets.all():
        print(bucket.name)
        bucket_tagging = s3.BucketTagging(bucket.name)
        print(bucket_tagging)
