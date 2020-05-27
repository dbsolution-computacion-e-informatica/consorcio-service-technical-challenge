# -*- coding: utf-8 -*-
"""Stats micro functions.
"""

import os
import boto3
import json
from utils import utils

DYNAMODB_CLIENT = boto3.resource('dynamodb')


def build(event, context):
    """This micro function consolidate statistics of human vs mutant (ratio).

    Args:
        event (mixed): The input event of the micro function.
        context (mixed): The input context of the micro function.
    """

    count_mutant_dna = 0
    count_human_dna = 0

    for record in event['Records']:

        if record['dynamodb']['NewImage']['mutant']['BOOL']:
            count_mutant_dna += 1
        else:
            count_human_dna += 1

    DYNAMODB_CLIENT.Table(os.getenv('DNA_ANALYSE_STATS_TABLE_NAME')).update_item(
        Key={
            'id': 1
        },
        UpdateExpression='ADD #ATTCMD :CMD, #ATTCHD :CHD',
        ExpressionAttributeNames={
            '#ATTCMD': 'count_mutant_dna',
            '#ATTCHD': 'count_human_dna'
        },
        ExpressionAttributeValues={
            ':CMD': count_mutant_dna,
            ':CHD': count_human_dna
        },
    )


def get(event, context):
    """This micro function give the statistics of DNA analyzes.

    Args:
        event (mixed): The input event of the micro function.
        context (mixed): The input context of the micro function.
    """

    item = DYNAMODB_CLIENT.Table(os.getenv('DNA_ANALYSE_STATS_TABLE_NAME')).get_item(
        Key={
            'id': 1
        }
    )

    # hack - Decimal transformation
    item = utils.replace_decimals(item)

    if item['Item']['count_human_dna'] > 0:
        ratio = float(item['Item']['count_mutant_dna']) / float(item['Item']['count_human_dna'])
    else:
        if item['Item']['count_mutant_dna'] == 0:
            ratio = 0
        else:
            ratio = 1

    response = {
        "statusCode": 200,
        "body": json.dumps({
            "count_mutant_dna": item['Item']['count_mutant_dna'],
            "count_human_dna": item['Item']['count_human_dna'],
            "ratio": ratio
        })
    }

    return response
