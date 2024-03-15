""" Dataset module to load images
"""
#conferir a ordem dos imports e ajustar os locos, tmabem melhoras as docstriungs de descrição
from os import listdir
from typing import Any

from torch.utils.data import Dataset
from torchvision.io import read_image


class CustomDataset(Dataset):
    def __init__(self, path, transform=None) -> None:
        """ Class for get image and file name

        :param path: Images folder path
        :type path: str
        :param transform: Image preprocessing steps
        :type transform: torch.nn.Sequential
        """
        super().__init__()
        self.path = path
        self.image_names = listdir(path)
        self.transform = transform
    
    def __len__(self) -> int:
        """ Returns the quantity of images in folder
        """
        return len(self.image_names)
    
    def __getitem__(self, index) -> Any:
        """ Returns the image corresponding to the given index and
            its archive name
        """
        image_path = self.path + "/" + self.image_names[index]
        image = read_image(image_path)

        # Apply the transformations over image if exists
        if self.transform:
            image = self.transform(image)

        return image, self.image_names[index]
