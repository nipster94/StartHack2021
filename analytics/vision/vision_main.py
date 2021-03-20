#!/usr/bin/env python3
import os, requests, uuid, json
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials

from array import array
import os
from PIL import Image
import sys
import time

class AnalyzeDocument():
    def __init__(self):
        self.api_key = ""
        self.endpoint = ""
        self.location = ""
        self.load_config('../template/config.json')

        if not self.api_key or not self.endpoint:
            raise Exception('Please set/export API key')

        self.authentication()

    def load_config(self, file_path):
        file_ = open(file_path)
        data = json.load(file_)
        self.api_key = data['api_keys']['vision']
        self.endpoint = data['endpoints']['vision']
        self.location = data['locations']['vision']

    def authentication(self):
        self.computervision_client = ComputerVisionClient(self.endpoint,
                                                     CognitiveServicesCredentials(self.api_key))

    def run_example(self):
        remote_image_url = "https://raw.githubusercontent.com/Azure-Samples/cognitive-services-sample-data-files/master/ComputerVision/Images/landmark.jpg"
        print("===== Describe an image - remote =====")
        # Call API
        description_results = self.computervision_client.describe_image(remote_image_url)

        # Get the captions (descriptions) from the response, with confidence level
        print("Description of remote image: ")
        if (len(description_results.captions) == 0):
            print("No description detected.")
        else:
            for caption in description_results.captions:
                print("'{}' with confidence {:.2f}%".format(caption.text, caption.confidence * 100))

    def azure_ocr_by_url(self,url):
        pass

    def azure_orc_image(self,image):
        pass

    def azure_orc_pdf(self,pdf):
        pass

    def upload_document(self,file):
        pass



if __name__ == '__main__':
    AnalyzeDocument()

