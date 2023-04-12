import requests
from datetime import datetime, timedelta


import json
import boto3

from datetime import datetime, timedelta

def lambda_handler(event, context):
    yesterday = datetime.now() - timedelta(2)
    yesterday_str = datetime.strftime(yesterday, '%Y-%m-%d')
    response = requests.get(f"https://public.opendatasoft.com/api/v2/catalog/datasets/donnees-synop-essentielles-omm/records?where=date%3E%3D%22{yesterday_str}T22%3A00%3A00Z%22&limit=10&offset=0&refine=nom%3AORLY&timezone=UTC")

    data = response.json()

    
    s3 = boto3.resource('s3')
    s3.Bucket('meteo-orly-daily').put_object(
        Key=f"data_{yesterday_str}.json",
        Body=json.dumps(data),
        ContentType='application/json'
        )
    
    
    return {
        'statusCode': 200,
        'body': json.dumps('OK!!')
    }