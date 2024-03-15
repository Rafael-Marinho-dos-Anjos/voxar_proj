""" Main window application module
"""

from threading import Thread, Lock

from tkinter import filedialog
import tkinter as tk

from app.controller.images_analyzer import do_predictions
from app.controller.save_csv import save_csv
from app.view.visualization_window import VisualizationWindow


class MainWindow(tk.Tk):#verificar se todas as linhas estão com 79 ou 120
    def __init__(self) -> None:
        """ Main window application class
        """
        super().__init__()
        self.mutex = Lock()

        self.resizable(False, False)
        self.geometry("400x250")
        self.title("Voxar Classification Project")
        self.visualization = None

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

        self.bt_visualize = tk.Button(master=self, text="Generate random\nvisualization", command=self.generate_visualization)

    def place_widgets(self) -> None:
        self.bt_select_folder.place(relx=0.5, rely=0.1, anchor='center')
        self.lb_folder.place(relx=0.5, rely=0.2, anchor='center')

        self.bt_select_output.place(relx=0.5, rely=0.4, anchor='center')
        self.lb_output.place(relx=0.5, rely=0.5, anchor='center')

        self.bt_start.place(relx=0.3, rely=0.8, anchor='center')
        self.lb_progress.place(relx=0.5, rely=0.9, anchor='center')

        self.bt_visualize.place(relx=0.7, rely=0.77, anchor='center')

    def select_folder(self) -> None:
        """ Select the folder where are stored the images
        """
        self.progress.set("")
        folder = filedialog.askdirectory()
        if folder:
            self.folder_path.set(folder)
        
    def select_output(self) -> None:
        """ Select the folder where will be stored the csv file
        """
        self.progress.set("")
        folder = filedialog.askdirectory()
        if folder:
            self.output_path.set(folder)
    
    def start(self) -> None:
        """ Start inference over every image in specified folder and save the answers
        in a csv file
        """
        folder_path = self.folder_path.get()
        output_path = self.output_path.get()

        # If images folder or output folder are not selected, warn the user
        if folder_path in ["Please select folder", ""] or output_path in ["Please select folder", ""]:
            self.progress.set("Select all folders before start")
            return
        
        def __start_classification(progress_var) -> None:
            # Disable all buttons while program makes the predictions
            self.bt_start["state"] = "disabled"
            self.bt_visualize["state"] = "disabled"
            self.bt_select_folder["state"] = "disabled"
            self.bt_select_output["state"] = "disabled"

            # Predict classes for each image in folder
            progress_var.set("Doing classification for each image in folder...")
            predictions = do_predictions(folder_path)

            # Save predictions in the output folder as a csv file
            progress_var.set("Saving answer into the csv file...")
            save_csv(predictions, output_path)
            progress_var.set("Done!")

            # Enable again all buttons
            self.bt_start["state"] = "normal"
            self.bt_visualize["state"] = "normal"
            self.bt_select_folder["state"] = "normal"
            self.bt_select_output["state"] = "normal"
        
        # Running the classification in a worker thread to avoid freezing the application window
        worker_thread = Thread(target=__start_classification, args=[self.progress])
        worker_thread.start()

    def generate_visualization(self):
        """ Shows a new window with a drawn image from specified folder and its respective
        prediction
        """
        folder_path = self.folder_path.get()
        if folder_path in ["Please select folder", ""]:
            self.progress.set("Select the images folder before visualize a sample")
            return
        # Destroy visualization window if already have one opened
        if self.visualization:
            self.visualization.destroy()
        
        self.visualization = VisualizationWindow(self.folder_path.get())
