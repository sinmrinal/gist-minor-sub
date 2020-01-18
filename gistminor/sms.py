from django.conf import settings
import requests
import json
import os

URL = 'https://www.sms4india.com/api/v1/sendCampaign'

with open(os.path.join(settings.BASE_DIR, 'config.json'), 'r') as config:
    d = json.load(config)["SMS"]


# get request
def sendPostRequest(reqUrl, apiKey, secretKey, useType, phoneNo, senderId, textMessage):
    req_params = {
        'apikey': apiKey,
        'secret': secretKey,
        'usetype': useType,
        'phone': phoneNo,
        'message': textMessage,
        'senderid': senderId
    }
    return requests.post(reqUrl, req_params)


def send(mobile, message):
    response = sendPostRequest(
    URL, d['api_key'], d['secret_key'], 'stage', mobile, 'SMSIND', message)
    return json.loads(response.text)
