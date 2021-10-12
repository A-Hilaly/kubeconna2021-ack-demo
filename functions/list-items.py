from __future__ import print_function

import json
import os
import boto3
from botocore.exceptions import ClientError

# Get the service resource.
dynamodb = boto3.resource('dynamodb')

# set environment variable
TABLE_NAME = os.environ['TABLE_NAME']

def lambda_handler(event, context):
    table = dynamodb.Table(TABLE_NAME)
    # Scan items in table
    try:
        response = table.scan()
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        print(json.dumps(response['Items']))
    
    return {
        'items': response['Items'],
    }