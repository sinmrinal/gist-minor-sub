from django import forms
from .settings import BASE_DIR
import json, os
import requests

with open(os.path.join(BASE_DIR, 'config.json'), 'r') as config :
    d = json.load(config)["OD"]

def search(word):
        result = {}
        endpoint = 'https://od-api.oxforddictionaries.com:443/api/v2/entries/{source_lang}/{word_id}'
        url = endpoint.format(source_lang='en', word_id=word)
        headers = {'app_id': d['app_id'], 'app_key': d['app_key']}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:  # SUCCESS
            result = response.json()
            result['success'] = True
        else:
            result['success'] = False
            if response.status_code == 404:  # NOT FOUND
                result['message'] = 'No entry found for "%s"' % word
            else:
                result['message'] = 'The Oxford API is not available at the moment. Please try again later.'
        return result