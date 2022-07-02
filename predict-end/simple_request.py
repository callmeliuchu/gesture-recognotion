# encoding: utf-8
"""
@author: xyliao
@contact: xyliao1993@qq.com
"""

import requests
import argparse
import base64
import json

# Initialize the PyTorch REST API endpoint URL.
PyTorch_REST_API_URL = 'http://106.14.149.194:5032/torch/predict'

import time
def predict_result(image_path,use_base64=True):
    # Initialize image path
    image = open(image_path, 'rb').read()
    bg = time.time()
    if use_base64:
        base64_data = base64.b64encode(image)
        base64_str = str(base64_data, 'utf-8')
        payload = {'image': base64_str}
        with open('img.json','w') as f:
            json.dump(payload,f)
        # for _ in range(10):
        r = requests.post(PyTorch_REST_API_URL, json=payload).json()
            # print(r)
    else:
        payload = {'image': image}
        # for _ in range(10):
        r = requests.post(PyTorch_REST_API_URL, files=payload).json()
        # print(r)
    print('hhh',r)
    ed = time.time()
    print(ed-bg)
    # Submit the request.


    # Ensure the request was successful.
    if r['success']:
        pass
        # print(r)
        # Loop over the predictions and display them.
    # Otherwise, the request failed.
    else:
        print('Request failed')
    return r

import os


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Classification demo')
    parser.add_argument('--file', type=str, help='test image file')
    args = parser.parse_args()
    dir_path = "/Users/liuchu/Desktop/学习类/一级实践群/一级工程实践大作业/手势识别数据集/train/"
    # total = 0
    # correct = 0
    # for dir_name in os.listdir(dir_path):
    #     label = dir_name
    #     path = dir_path + '/' + label
    #     for file_name in os.listdir(path):
    #         try:
    #             total += 1
    #             pp = path + '/' + file_name
    #             ans = predict_result(pp)
    #             if int(label) == ans["predict"]:
    #                 correct += 1
    #             print(ans)
    #         except:
    #             pass
    #         # print(label,pp)
    # print(correct,total,correct/total)

    # for file_name in
    predict_result(args.file)
