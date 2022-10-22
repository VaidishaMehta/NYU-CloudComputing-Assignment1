

import random
import boto3



def lambda_handler(event, context):
    
    response = {
      "dialogAction": {
        "type": "Close",
        "fulfillmentState": "Fulfilled",
        "message": {
          "contentType": "PlainText",
          }
        }
    }
    
    
    
    if event["currentIntent"]["name"]=="DiningSuggestionsIntent":
      
      slot = event["currentIntent"]["slots"]
      sqs = boto3.client('sqs')
      queue_url = 'https://sqs.us-east-1.amazonaws.com/235400441598/PushMessage'
      send_queue = sqs.send_message(
      QueueUrl=queue_url,
      DelaySeconds=10,
      MessageAttributes={
                'Cuisine': {
                'DataType': 'String',
                'StringValue': slot['Cuisine']
            },
                'Location': {
                'DataType': 'String',
                'StringValue': slot['Location']
            },
                'Email': {
                'DataType': 'String',
                'StringValue': slot['Email']
            },
                'Number': {
                'DataType': 'Number',
                'StringValue': slot['Number']
            }
        },
        MessageBody=(
            'New recommendation request'))
    response["dialogAction"]["message"]["content"] = "Thank you, you will receive recommendations via email shortly"
    return response