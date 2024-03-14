""" Main window application module
"""

from threading import Thread, Lock
from tkinter import filedialog
import tkinter as tk
from app.controller.images_analyzer import do_predictions
from app.controller.save_csv import save_csv


class MainWindow(tk.Tk):
    def __init__(self, screenName: str = None, baseName: str = None, className: str = "Tk", useTk: bool = True, sync: bool = False, use: str = None) -> None:
        super().__init__(screenName, baseName, className, useTk, sync, use)
        self.mutex = Lock()

        self.resizable(False, False)
        self.geometry("400x250")
        self.title("Voxar Classification Project")

        self.create_widgets()
        self.place_widgets()
    
    def create_widgets(self):
        self.folder_path = tk.StringVar(value="Please select folder")
        self.output_path = tk.StringVar(value="Please select folder")
        self.progress = tk.StringVar()

        self.bt_select_folder = tk.Button(master=self, text="Select images folder", command=self.select_folder)
        self.lb_folder = tk.Label(master=self, textvariable=self.folder_path, anchor='center')

        self.bt_select_output = tk.Button(master=self, text="Select output location", command=self.select_output)
        self.lb_output = tk.Label(master=self, textvariable=self.output_path, anchor='center')

        self.bt_start = tk.Button(master=self, text="Start", command=self.start)
        self.lb_progress = tk.Label(master=self, textvariable=self.progress)

    def place_widgets(self) -> None:
        self.bt_select_folder.place(relx=0.5, rely=0.1, anchor='center')
        self.lb_folder.place(relx=0.5, rely=0.2, anchor='center')

        self.bt_select_output.place(relx=0.5, rely=0.4, anchor='center')
        self.lb_output.place(relx=0.5, rely=0.5, anchor='center')

        self.bt_start.place(relx=0.5, rely=0.8, anchor='center')
        self.lb_progress.place(relx=0.5, rely=0.9, anchor='center')

    def select_folder(self) -> None:
        """ Select the folder where are stored the images
        """
        folder = filedialog.askdirectory()
        self.folder_path.set(folder)
        self.progress.set("")
        
    def select_output(self) -> None:
        """ Select the folder where will be stored the csv file
        """
        folder = filedialog.askdirectory()
        self.output_path.set(folder)
        self.progress.set("")
    
    def start(self) -> None:
        folder_path = self.folder_path.get()
        output_path = self.output_path.get()

        # If images folder or output folder are not selected, warn the user
        if folder_path == "Please select folder" or output_path == "Please select folder":
            self.progress.set("Select all folders before start")
            return
        
        def __start_classification(progress_var) -> None:
            # Disable all buttons while program makes the predictions
            self.bt_select_folder["state"] = "disabled"
            self.bt_select_output["state"] = "disabled"
            self.bt_start["state"] = "disabled"

            # Predict classes for each image in folder
            progress_var.set("Doing classification for each image in folder...")
            predictions = do_predictions(folder_path)

            # Save predictions in the output folder as a csv file
            progress_var.set("Saving answer into the csv file...")
            save_csv(predictions, output_path)
            progress_var.set("Done!")

            # Enable again all buttons
            self.bt_select_folder["state"] = "normal"
            self.bt_select_output["state"] = "normal"
            self.bt_start["state"] = "normal"
        
        # Running the classification in a worker thread to avoid freezing the application window
        worker_thread = Thread(target=__start_classification, args=[self.progress])
        worker_thread.start()
