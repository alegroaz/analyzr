import sys
import matplotlib.pyplot as plt
import numpy as np
import cv2


from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget
from PyQt5 import QtGui

from nd2reader import ND2Reader

class Launcher():

    def __init__(self):
        self.main_window = QWidget()
        self.main_window.setWindowTitle('Pipeline Launcher')
        self.main_window.setGeometry(100, 100, 880, 580)

        self.data_path = 'not set'
        #Put in elements.py
        self.pathLabel = QLabel('<h3>Path: %s' % path, parent=window).move(20, 20)

        with ND2Reader(
                'C:\\Users\\alegr\\Documents\\University\\St-Pierre\\Sample data\\KIN-AG004\\X2048Y200C3\\[Lin-Kir2.1-T2A-aKv1.1-mScarlet] +dox_P0D4-4.nd2') as images:
            print(images.metadata)
            plt.imshow(images[0])
            images.iter_axes = 'c'
            plt.imshow(images[0])
            plt.show()
        self.main_window.show()

        # print_hi('PyCharm')