#!/usr/bin/env python3
import os, requests, uuid, json


class BasicTranslation():
    def __init__(self):
        self.api_key = ""
        self.endpoint = ""
        self.location = ""
        self.load_config('../template/config.json')

        if not self.api_key or not self.endpoint:
            raise Exception('Please set/export API key')

        self.default_translator_path = 'translate?api-version=3.0'
        self.params_ = '&from=en&to=de&to=it'

        self.constructed_url = self.endpoint + self.default_translator_path + self.params_

        self.headers = {
            'Ocp-Apim-Subscription-Key': self.api_key,
            'Ocp-Apim-Subscription-Region': self.location,
            'Content-type': 'application/json',
            'X-ClientTraceId': str(uuid.uuid4())
        }

        self.request_data("Hello world")

    def load_config(self, file_path):
        file_ = open(file_path)
        data = json.load(file_)
        self.api_key = data['api_keys']['translator']
        self.endpoint = data['endpoints']['translator']
        self.location = data['locations']['translator']

    def request_data(self, requested_text):
        body = [{
            'text': requested_text
        }]
        request = requests.post(self.constructed_url, headers=self.headers, json=body)
        response = request.json()

        print(json.dumps(response, sort_keys=True, indent=4, separators=(',', ': ')))


if __name__ == '__main__':
    BasicTranslation()