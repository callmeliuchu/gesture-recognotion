# encoding: utf-8
"""
@author: xyliao
@contact: xyliao1993@qq.com
"""
import io


import flask
from PIL import Image
import base64
from model.paddle_gesture.predict import predict_img as predict_pad
from model.restnet50.predict import predict_img as predict_tt

# Initialize our Flask application and the PyTorch model.
app = flask.Flask(__name__)


def predict_by(predict_img):
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
            raise e
    return data




@app.route("/torch/predict", methods=["POST"])
def predict_pytorch():
    data = predict_by(predict_tt)
    return flask.jsonify(data)

@app.route("/paddle/predict", methods=["POST"])
def predict_paddle():
    data = predict_by(predict_pad)
    print(data)
    return flask.jsonify(data)

if __name__ == '__main__':
    print("Loading PyTorch model and Flask starting server ...")
    print("Please wait until server has fully started")
    app.run(host="0.0.0.0",port=5032)
