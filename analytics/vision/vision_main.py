#!/usr/bin/env python3
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
import requests, uuid, json
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials
from analytics.translator.basic_translation import BasicTranslation

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
        self.res_file_ = '../template/resources/'
        self.load_config('../template/config.json')
        self.max_num_retries = 2

        self.basic_trans_ = BasicTranslation()
        if not self.api_key or not self.endpoint:
            raise Exception('Please set/export API key')

        self.authentication()
        # image = Image.open(self.res_file_ + 'de-OP-Bericht-001.jpeg').convert('RGB')
        image =  open(self.res_file_ + 'de-OP-Bericht-001.jpeg', "rb")
        self.azure_ocr_image(image,"en")

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

    def azure_ocr_image(self, image, lan_to, lan_from=None):
        description_results = self.computervision_client.recognize_printed_text_in_stream(image,language='de')
        if not lan_from:
            lan_from = description_results.language
        translated_text_ = ""
        for region in description_results.regions:
            region_line_ = ""
            for line in region.lines:
                s = ""
                for word in line.words:
                    s += word.text + " "
                region_line_ += s

            translated_text_ += self.basic_trans_.translate_text(region_line_,lan_from,lan_to)

        print(translated_text_)
        return translated_text_

    def azure_ocr_pdf(self,pdf):
        pass

    def upload_document(self,file):
        pass


if __name__ == '__main__':
    AnalyzeDocument()

