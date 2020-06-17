import json
import boto3

ec2Client = boto3.client('ec2')


def lambda_handler(event, context):
    regions = ec2Client.describe_regions()
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps(regions['Regions'])
    }
