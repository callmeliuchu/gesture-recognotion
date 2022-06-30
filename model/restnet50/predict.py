import os
from torchvision import transforms
import torchvision
import torch
import torch.nn as nn

data_transform = transforms.Compose([            #[1]
 transforms.Resize(224),                    #[2]
 transforms.Grayscale(num_output_channels=3),
 transforms.ToTensor(),                     #[4]
 transforms.Normalize(                      #[5]
 mean=[0.485, 0.456, 0.406],                #[6]
 std=[0.229, 0.224, 0.225]                  #[7]
 )])

dir_path = os.path.dirname(__file__)


def predict_img(img):
    global model2
    im = data_transform(img)
    model2 = torchvision.models.resnet18()
    num_ftrs = model2.fc.in_features
    model2.fc = nn.Linear(num_ftrs, 6)
    model2.load_state_dict(torch.load(dir_path + "/restnet50.pth"))
    model2.to('cpu')
    with torch.no_grad():
        model2.eval()
        o = model2(im.unsqueeze(0))
        return int(torch.argmax(o, dim=1))
