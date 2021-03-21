#!/usr/bin/env python3
import os, requests, uuid, json


class TextTranslator():
    def __init__(self):
        self.api_key = ""
        self.endpoint = ""
        self.location = ""
        self.default_translator_path = 'translate?api-version=3.0'

    def authentication(self, config_path):
        self.load_config(config_path)
        if not self.api_key or not self.endpoint:
            raise Exception('Please set/export API key')

        self.headers = {
            'Ocp-Apim-Subscription-Key': self.api_key,
            'Ocp-Apim-Subscription-Region': self.location,
            'Content-type': 'application/json',
            'X-ClientTraceId': str(uuid.uuid4())
        }
        self.constructed_url = self.endpoint + self.default_translator_path

    def load_config(self, file_path):
        file_ = open(file_path)
        data = json.load(file_)
        self.api_key = data['api_keys']['translator']
        self.endpoint = data['endpoints']['translator']
        self.location = data['locations']['translator']

    def translate_text(self, requested_text, lan_from, lan_to):
        if requested_text:
            body = [{
                'text': requested_text
            }]
            params_ = '&from=' + lan_from + '&to=' + lan_to
            request = requests.post(self.constructed_url + params_, headers=self.headers, json=body)
            response = request.json()

            return response[0]["translations"][0]['text']

        return ""
