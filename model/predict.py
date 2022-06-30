import os
import time
import random
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import paddle
import paddle.fluid as fluid
import paddle.fluid.layers as layers
from multiprocessing import cpu_count
from paddle.fluid.dygraph import Pool2D, Conv2D
from paddle.fluid.dygraph import Linear
from model.model import MyLeNet

# 读取预测图像，进行预测
def load_image(path):
    img = Image.open(path)
    img = img.resize((32, 32), Image.ANTIALIAS)
    img = np.array(img).astype('float32')
    img = img.transpose((2, 0, 1))
    img = img / 255.0
    print(img.shape)
    return img


def handle_imgae(img):
    img = img.resize((32, 32), Image.ANTIALIAS)
    img = np.array(img).astype('float32')
    img = img.transpose((2, 0, 1))
    img = img / 255.0
    print(img.shape)
    return img

# 构建预测动态图过程


def predict_img(img):
    global model1
    model1 = MyLeNet()  # 模型实例化
    with fluid.dygraph.guard():
        model_dict, _ = fluid.load_dygraph('/Users/liuchu/gesture-recognition/model/paddle_gesture/MyLeNet')
        model1.load_dict(model_dict)  # 加载模型参数
        model1.eval()  # 评估模式
        infer_img = handle_imgae(img)
        infer_img = np.array(infer_img).astype('float32')
        infer_img = infer_img[np.newaxis, :, :, :]
        infer_img = fluid.dygraph.to_variable(infer_img)
        result = model1(infer_img)
        # display(Image.open('手势.JPG'))
        ans = int(np.argmax(result.numpy()))
        if ans > 5:
            ans = 3
        return ans
