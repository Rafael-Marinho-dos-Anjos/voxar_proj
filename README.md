# Voxar Aplication Project - Rafael Marinho dos Anjos

This README document is composed by two parts:
- The first teaching how to install dependencies and use the software
- The seccond showing the project developement pipeline

## How to install and use application

### Description
This software is a easy way to classify animal images in a entire folder, saving all predictions answers into a csv file.

### Setup
- Clone project repository: `git clone https://github.com/Rafael-Marinho-dos-Anjos/voxar_proj.git`
- Ensure that Python 3.9 programming language or a newer version is installed
- Install all dependences listed in requirements.txt (to install dependences execute the command 'pip install -r requirements.txt' on command prompt)

### Setup for GPU
- In addiction to the previous steps, for running predictions in GPU is necessary to install the NVIDIA CUDA Toolkit and PyTorch CUDA pakcage
- To install NVIDIA CUDA Toolkit go to 'https://developer.nvidia.com/cuda-downloads' website, download and install the CUDA Toolkit for your system specifications
- Next to it, install all dependences listed in requirements-gpu.txt (to install dependences execute the command 'pip install -r requirements-gpu.txt' on command prompt). If you are not running on Windows OS, please move to 'https://pytorch.org/get-started/locally/' website, select your system specifications and copy the command instalation to command prompt

### How to use
- To execute the software in windows just open the file 'launch.bat' located in root folder or run the file 'main.py' with Python in command prompt 'python .\main.py'
- There are four buttons on main screen application: the first one (Select images folder) opens a new window to select the folder with images to be classified, the seccond (Select output location) opens a new window to select the folder where will be saved the csv file, the third (Start) executes the classification and the last (Generate Random Visualization) will draw randomly an image to classify and show it in a new window
- Before clicking to start (third button) is necessary to select the folders by clicking on the other two previous buttons (in any order), otherwise will be shown a message error
- If the folders are selected properly, by clicking on Start the software will execute the classification and generates the file 'classifications.csv' in specified path automatically
- Before clicking in Generate Random Visualization (fourth button) is necessary to select at least the images folder, otherwise a message error is shown. If the button is clicked when the images folder is already selected, a drawn image wil be showed in a new window with its classification

### Warnings
- Running software for the first time can be a little time consuming depending on your internet connection quality due to the neural network weights download. For later software uses, the Python stores weights in cache to avoid downloading again

## Developement pipeline

The project pipeline was organized seeking the priority order bellow:

1. Reading and preprocessing files
2. Model selection
3. Information post processing
4. Saving informations to a file
5. Application front-end and files navigator
6. Easy results visualization

### Reading and preprocessing files
In this step were created the Dataset and DataLoader classes to access image files from folder directly to torch tensor type

### Model selection
In this step several neural networks pretrained with ImageNet avaliable in PyTorch were tested and evaluated precision and performance to choose the bets for this application purpose

### Information post processing
After the model classification is necessary to convert the output tensor to the class prediction, for this were created a superclasses list with all animals species (not races). With the classification label and image file name, is necessary to concatenate the strings to the required format

### Saving informations to a file
With the information in correct format, the application must save it into a external cvs file

### Application front-end and files navigator
Construct a window for any user manipulate the software easily

### Easy results visualization
Introduce in application a easy way to visualize the results without the need to read csv file