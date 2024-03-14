""" Images class analyzer module
"""

from typing import Dict
from torch import argmax
from app.model.wide_resnet.load_model import model
from app.model.data.dataloader import get_dataloader


def do_predictions(im_folder: str, batch_size: int = 1) -> Dict:
    """ Returns a dict containing each image name and its prediction from model
    """
    loader = get_dataloader(im_folder, batch_size)
    predictions = {}
    
    # Store every prediction from model into a dict
    for image, name in loader:
        prediction = model(image)
        prediction = argmax(prediction, dim=1)
        predictions[name[0]] = prediction.item()
    
    return predictions
