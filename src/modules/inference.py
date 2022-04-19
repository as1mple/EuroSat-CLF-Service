import efficientnet_pytorch
import torch
from torch import nn
from loguru import logger
from albumentations.pytorch import ToTensorV2
from albumentations import Normalize, Compose, Resize


class Model:
    def __init__(self, path_to_model, transform):
        self.path_to_model = path_to_model
        self.transform = transform

        self.device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
        logger.info(f"self.device = {self.device}")
        self.model = efficientnet_pytorch.EfficientNet.from_pretrained("efficientnet-b0")
        self.model._fc = nn.Linear(in_features=1280, out_features=10, bias=True)

        self.model.to(self.device)
        self.model.load_state_dict(
            torch.load(self.path_to_model, map_location=self.device)["model_state_dict"]
        )
        self.model.eval()

    def __call__(self, img):
        img = self.transform(image=img)["image"]
        img = torch.unsqueeze(img, 0)
        x_text = img.to(self.device)

        with torch.no_grad():
            _, predict = self.model(x_text).max(1)
        predict = predict.tolist()
        return predict[0]

    @staticmethod
    def transforms_valid(image_size=(256, 256)):
        return Compose([

            Resize(*image_size),
            Normalize(
                mean=[0.485, 0.456, 0.406],
                std=[0.229, 0.224, 0.225],
            ),
            ToTensorV2()
        ],
            p=1
        )