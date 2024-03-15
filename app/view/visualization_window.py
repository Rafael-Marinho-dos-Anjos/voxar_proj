""" Visualization module for a random sample image in folder
"""

import tkinter as tk
from PIL import Image, ImageTk
from torch import argmax

from app.model.data.dataloader import get_dataloader
from app.model.wide_resnet.load_model import model, device
from app.utils.imagenet_classes import superclasses


class VisualizationWindow(tk.Tk):
    def __init__(self, path: str) -> None:
        """ Image visualization window

        :param path: Images folder path
        :type path: str
        """
        super().__init__()

        self.resizable(False, False)
        self.geometry("250x300")
        self.title("Random image visualization")

        # Instanciating DataLoader
        self.loader = get_dataloader(im_folder=path, batch_size=1, shuffle=True)

        # Get a random image from DataLoader
        self.image, self.im_name = next(iter(self.loader))
        self.im_path = path + "/" + self.im_name[0]

        # Generating model prediction
        prediction = model(self.image.to(device))
        prediction = argmax(prediction, dim=1).item()
        self.class_name = superclasses[prediction] if prediction < 400 else "Not animal"
        
        # Converting image to numpy array for displaying
        self.image = self.image.squeeze(0).permute(1, 2, 0).cpu().numpy()
        self.image = ImageTk.PhotoImage(image=Image.open(self.im_path), master=self)

        self.create_widgets()
        self.place_widgets()

        self.mainloop()

    def create_widgets(self) -> None:
        self.canvas = tk.Label(master=self, image=self.image)
        self.lb_pred = tk.Label(master=self, text="Prediction: " + self.class_name)

    def place_widgets(self) -> None:
        self.canvas.place(relx=0.5, rely=0.4, relheight=0.7, anchor='center')
        self.lb_pred.place(relx=0.5, rely=0.9, anchor='center')
