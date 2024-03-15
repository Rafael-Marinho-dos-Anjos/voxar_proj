""" Dataloader module to load images
"""

from app.model.data.dataset import CustomDataset
from app.model.wide_resnet.load_model import transforms
from torch.utils.data import DataLoader


def get_dataloader(
        im_folder: str,
        batch_size: int,
        shuffle: bool = False,
        transforms=transforms
    ) -> DataLoader:
    """ Returns the dataloader object for loading images from given folder

    :param im_folder: Images folder path
    :type im_folder: str
    :param batch_size: The number of images readed every classification loop
    :type batch_size: int
    :param shuffle: If the batch returned every loop is a random choice
    :type shuffle: bool
    :param transforms: Image preprocessing steps
    :type transforms: torch.nn.Sequential
    :returns loader: Loading images and names object
    :rtype: torch.utils.data.DataLoader
    """
    dataset = CustomDataset(im_folder, transforms)
    loader = DataLoader(dataset, batch_size=batch_size, shuffle=shuffle)

    return loader
