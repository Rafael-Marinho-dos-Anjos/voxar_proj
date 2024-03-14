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
    """
    dataset = CustomDataset(im_folder, transforms)
    loader = DataLoader(dataset, batch_size=batch_size, shuffle=shuffle)

    return loader
