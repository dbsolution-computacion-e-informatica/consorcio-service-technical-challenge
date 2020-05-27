# -*- coding: utf-8 -*-
"""DNA Analyse micro functions.
"""

import json
from utils import checker
import os
import boto3
import hashlib

SQS_CLIENT = boto3.client('sqs')
DYNAMODB_CLIENT = boto3.resource('dynamodb')


def check(event, context):
    """This micro function is used by API Gateway and run the check processing of the DNA.
    It first hash the DNA to search for already processed results, if already processed, it
    returns the boolean result, else the processing will occur and a message will be sent
    to the SQS queue in charge and saving the item to database

    Args:
        event (mixed): The input event of the micro function.
        context (mixed): The input context of the micro function.

    Returns:
        mixed: The micro function response
    """

    body = json.loads(event['body'])

    # calculating DNA hash
    dna_hash = hashlib.md5(
        json.dumps(body['dna']).encode("utf-8")
    ).hexdigest()

    # looking for existing result for this DNA
    item = DYNAMODB_CLIENT.Table(os.getenv('DNA_ANALYSE_TABLE_NAME'))\
        .get_item(Key={
            'hash': dna_hash
        }, ProjectionExpression='mutant'
    )

    # If already analyzed, get the result
    if hasattr(item, 'Item'):

        result = item['Item']['mutant']

    # Else we calculate and set to DB via SQS Queue
    else:

        result = checker.is_mutant(body['dna'])

        SQS_CLIENT.send_message(
            QueueUrl=os.getenv('DNA_ANALYSE_QUEUE_URL'),
            MessageBody=json.dumps({
                'hash': dna_hash,
                'dna': body['dna'],
                'mutant': result
            })
        )

    # Responding
    response = {
        "statusCode": 200,
        "body": json.dumps(result)
    }

    return response


def process(event, context):
    """This micro function process the SQS queue and insert the item in database
    only if this item was not already in the database. If insertion fail
    the SQS Queue will automatically retry the insertion.

    Args:
        event (mixed): The input event of the micro function.
        context (mixed): The input context of the micro function.
    """

    for record in event['Records']:
        item = json.loads(record["body"])

        DYNAMODB_CLIENT.Table(os.getenv('DNA_ANALYSE_TABLE_NAME'))\
            .put_item(Item=item)