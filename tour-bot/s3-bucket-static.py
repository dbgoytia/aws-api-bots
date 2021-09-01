import boto3
import botocore


def create_sample_bucket(s3_client):
    response = s3_client.create_bucket(
        ACL='private',
        Bucket='tour-test-123',
    )
    return response

def create_website_in_bucket(s3_resource, bucket):
    bucket_website = s3_resource.BucketWebsite(bucket)
    bucket_website.index_document("index.html")
    print(bucket_website)

def main():
    boto3_session = boto3.session.Session(
        profile_name='terraform_user_dev')
    s3_client = boto3_session.client('s3')

    response = create_sample_bucket(s3_client)
    if response.get("ResponseMetadata").get("HTTPStatusCode") != 200:
        print("something went wrong, treat error here.")
    
    s3_resource = boto3.resource('s3')


    create_website_in_bucket(s3_resource, 'tour-test-123')


main()