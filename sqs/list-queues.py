import boto3
from boto3.session import Session

# Initiate a session
session = Session(profile_name="default")

# Create sts client to assume the role
sts_client = session.client("sts")

assumed_role_object = sts_client.assume_role(
    RoleArn="PON EL TUYO",
    RoleSessionName="PON EL TUYO",
)
credentials = assumed_role_object['Credentials']

# Create an SQS client with the newly generated credentials
sqs_client = session.client(
    "sqs",
    aws_access_key_id=credentials['AccessKeyId'],
    aws_secret_access_key=credentials['SecretAccessKey'],
    aws_session_token=credentials['SessionToken'],
)

# List queues in the target account
q = sqs_client.list_queues()

print("Queue URLS:")
print(q.get("QueueUrls"))
print("Type of the response:")
print(type(q))

