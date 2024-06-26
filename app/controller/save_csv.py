""" Module to store all model predictions into a csv file
"""

import csv
from typing import Dict

from app.utils.imagenet_classes import superclasses


def save_csv(classifications: Dict, destination: str) -> None:
    """ Converts the classifications to the right format and stores it
        into a csv file

    :param classifications: The collection of all names and predictions for each image in folder
    :type classifications: Dict
    :param destination: The path of folder where the csv file will be saved
    :type destination: str
    :return: None
    """
    # Generate a list converting classifications to format 'image_name; class'
    classification_list = [
        "{}; {}".format(
            im_name,
            superclasses[class_id] if class_id < 400 else "Nenhum")
        for im_name, class_id in classifications.items()
        ]
    
    # Writing classifications into csv file
    with open(destination + "/classifications.csv", "w") as file:
        writer = csv.writer(file)
        writer.writerow(classification_list)
