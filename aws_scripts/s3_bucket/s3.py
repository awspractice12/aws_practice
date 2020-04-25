import sys
import boto3


#Create a new service object 
s3_list = boto3.resource('s3')
# Access the event system on the S3 client
event_system = s3.meta.events


#List the s3 Buckets and it's subdirectories 
for bucket in s3_list.buckets.all():
    print (bucket.name)
    print ("---")
    for item in bucket.objects.all():
        print ("\t%s" % item.key)

