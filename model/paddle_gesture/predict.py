import os
import numpy as np
from PIL import Image
import paddle.fluid as fluid
from model.paddle_gesture.model import MyLeNet

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

dir_path = os.path.dirname(__file__)
def predict_img(img):
    global model1
    model1 = MyLeNet()  # 模型实例化
    with fluid.dygraph.guard():

        model_dict, _ = fluid.load_dygraph(dir_path + '/MyLeNet')
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
