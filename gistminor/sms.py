from django.conf import settings
import requests
import json, os

URL = 'https://www.sms4india.com/api/v1/sendCampaign'

with open(os.path.join(settings.BASE_DIR, 'config.json'), 'r') as config :
    d = json.load(config)["SMS"]


# get request
def sendPostRequest(phoneNo, textMessage):
    req_params = {
    'apikey':d['api_key'],
    'secret':d['secret_key'],
    'usetype':'stage',
    'phone': phoneNo,
    'message':textMessage,
    'senderid':'SMSIND'
    }
    return requests.post(reqUrl, req_params)

def send(ph, message):
    response = sendPostRequest(URL,phoneNo=ph , textMessage=message)
    return response['status']

