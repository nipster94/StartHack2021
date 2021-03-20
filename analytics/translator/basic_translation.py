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


        self.constructed_url = self.endpoint + self.default_translator_path

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
        params_ = '&from=en&to=de'
        body = [{
            'text': requested_text
        }]
        request = requests.post(self.constructed_url + params_, headers=self.headers, json=body)
        response = request.json()
        print(response[0]["translations"][0]['text'])
        print(json.dumps(response, sort_keys=True, indent=4, separators=(',', ': ')))

    def translate_text(self,requested_text,lan_from,lan_to):
        body = [{
            'text': requested_text
        }]
        params_ = '&from=' + lan_from + '&to=' + lan_to
        request = requests.post(self.constructed_url+params_, headers=self.headers, json=body)
        response = request.json()
        # print(response[0]["translations"][0]['text'])
        return response[0]["translations"][0]['text']



if __name__ == '__main__':
    BasicTranslation()