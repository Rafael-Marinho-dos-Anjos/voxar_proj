""" Images class analyzer module
"""

from typing import Dict

from torch import argmax

from app.model.wide_resnet.load_model import model, device
from app.model.data.dataloader import get_dataloader


def do_predictions(im_folder: str, batch_size: int = 1) -> Dict:
    """ Returns a dict containing each image name and its prediction from model
    
    :param im_folder: The path of folder containing images
    :type im_folder: str
    :param batch_size: The number of images readed every classification loop
    :type batch_size: int
    :returns predictions: The collection of all names and predictions for each image in folder
    :rtype: Dict
    """
    loader = get_dataloader(im_folder, batch_size)
    predictions = {}
    
    # Store every prediction from model into a dict
    for image, name in loader:
        prediction = model(image.to(device))
        prediction = argmax(prediction, dim=1)
        predictions[name[0]] = prediction.item()
    
    return predictions
