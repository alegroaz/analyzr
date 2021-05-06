import sys
import matplotlib.pyplot as plt
import numpy as np
import cv2
import os


from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget
from PyQt5 import QtGui

from nd2reader import ND2Reader
from analyzr.image.image import Dataset

def main():
    #app = launcher.Launcher()
    #sys.exit(app.exec_());

    path = 'C:\\Users\\alegr\\Documents\\University\\St-Pierre\\Sample data\\KIN-AG004\\'
    dataset = Dataset(path)
    #dataset.tree()

