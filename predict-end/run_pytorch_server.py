# encoding: utf-8
"""
@author: xyliao
@contact: xyliao1993@qq.com
"""

import io
import json

import flask
import torch
import torch
import torch.nn.functional as F
from PIL import Image
from torch import nn
from torchvision import transforms as T
from torchvision.models import resnet50
import base64
from model.predict import predict_img

# Initialize our Flask application and the PyTorch model.
app = flask.Flask(__name__)
model = None
use_gpu = False

with open('imagenet_class.txt', 'r') as f:
    idx2label = eval(f.read())


def load_model():
    """
    Load the pre-trained model, you can use your model just as easily.
    """
    global model
    model = resnet50(pretrained=True)
    model.eval()
    if use_gpu:
        model.cuda()


def prepare_image(image, target_size):
    """Do image preprocessing before prediction on any data.

    :param image:       original image
    :param target_size: target image size
    :return:
                        preprocessed image
    """

    if image.mode != 'RGB':
        image = image.convert("RGB")

    # Resize the input image nad preprocess it.
    image = T.Resize(target_size)(image)
    image = T.ToTensor()(image)

    # Convert to Torch.Tensor and normalize.
    image = T.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])(image)

    # Add batch_size axis.
    image = image[None]
    if use_gpu:
        image = image.cuda()
    return torch.autograd.Variable(image, volatile=True)


@app.route("/torch/predict", methods=["POST"])
def predict_pytorch():
    # Initialize the data dictionary that will be returned from the view.
    data = {"success": False}

    # Ensure an image was properly uploaded to our endpoint.
    if flask.request.method == 'POST':
        adata = flask.request.json
        if adata:
            # Read the image in PIL format
            img_data = adata['image']
            if isinstance(img_data,str):
                image = base64.b64decode(img_data)
                print(type(image))
                image = Image.open(io.BytesIO(image))
        elif flask.request.files.get("image"):
            img_data = flask.request.files["image"]
            image = img_data.read()
            print(type(image))
            image = Image.open(io.BytesIO(image))
            # Preprocess the image and prepare it for classification.
        image = prepare_image(image, target_size=(224, 224))

        # Classify the input image and then initialize the list of predictions to return to the client.
        preds = F.softmax(model(image), dim=1)
        results = torch.topk(preds.cpu().data, k=3, dim=1)
        print(results)
        data['predictions'] = list()

        # Loop over the results and add them to the list of returned predictions
        for prob, label in zip(results[0][0], results[1][0]):
            print(prob,label)
            label_name = idx2label[int(label)]
            r = {"label": label_name, "probability": float(prob)}
            data['predictions'].append(r)

        # Indicate that the request was a success.
        data["success"] = True

    # Return the data dictionary as a JSON response.
    return flask.jsonify(data)


@app.route("/paddle/predict", methods=["POST"])
def predict_paddle():
    # Initialize the data dictionary that will be returned from the view.
    data = {"success": False}

    # Ensure an image was properly uploaded to our endpoint.
    if flask.request.method == 'POST':
        try:
            adata = flask.request.json
            if adata:
                # Read the image in PIL format
                img_data = adata['image']
                if isinstance(img_data,str):
                    image = base64.b64decode(img_data)
                    image = Image.open(io.BytesIO(image))
            elif flask.request.files.get("image"):
                img_data = flask.request.files["image"]
                image = img_data.read()
                print(type(image))
                image = Image.open(io.BytesIO(image))
                # Preprocess the image and prepare it for classification.
            data["predict"] = predict_img(image)
            # Indicate that the request was a success.
            data["success"] = True
        except Exception as e:
            data['success'] = False
            data['message'] = str(e)


    # Return the data dictionary as a JSON response.
    return flask.jsonify(data)

if __name__ == '__main__':
    print("Loading PyTorch model and Flask starting server ...")
    print("Please wait until server has fully started")
    load_model()
    app.run(host="0.0.0.0",port=5032)
