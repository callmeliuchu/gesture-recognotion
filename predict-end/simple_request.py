# encoding: utf-8
"""
@author: xyliao
@contact: xyliao1993@qq.com
"""

import requests
import argparse
import base64

# Initialize the PyTorch REST API endpoint URL.
PyTorch_REST_API_URL = 'http://localhost:5032/paddle/predict'


def predict_result(image_path,use_base64=True):
    # Initialize image path
    image = open(image_path, 'rb').read()
    if use_base64:
        base64_data = base64.b64encode(image)
        base64_str = str(base64_data, 'utf-8')
        payload = {'image': base64_str}
        r = requests.post(PyTorch_REST_API_URL, json=payload).json()
        print(r)
    else:
        payload = {'image': image}
        r = requests.post(PyTorch_REST_API_URL, files=payload).json()

    # Submit the request.


    # Ensure the request was successful.
    if r['success']:
        print(r)
        # Loop over the predictions and display them.
    # Otherwise, the request failed.
    else:
        print('Request failed')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Classification demo')
    parser.add_argument('--file', type=str, help='test image file')
    args = parser.parse_args()
    predict_result(args.file)
