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
import analyzr.image.dataset as Dataset

def main():
    #app = launcher.Launcher()
    #sys.exit(app.exec_());
    #path = 'C:\\Users\\alegr\\Documents\\University\\St-Pierre\\Sample data\\KIN-AG004\\'
    path = 'C:\\Users\\alegr\\Documents\\University\\St-Pierre\\Sample data\\KIN-AG004\\X2048Y200C3\\[Lin-Kir2.1-T2A-aKv1.1-mScarlet] +dox_P0D4-4.nd2'
    #dataset = Dataset.Dataset(path)

    '''for file in dataset.file_list:
        fig, axs = plt.subplots(2,1)
        c = 0
        for folder in dataset.forg_folders:
            pointer = dataset.path + folder + '\\' + file;
            with ND2Reader(pointer) as images:
                print(images.metadata)

                #images.iter_axes = 'c'
                axs[c].imshow(images[0], cmap='gray')
                axs[c].set_title(folder)
                c = c + 1
        plt.show()'''

    image = Dataset.Image(path)

    #with ND2Reader('C:\\Users\\alegr\\Documents\\University\\St-Pierre\\Sample data\\KIN-AG004\\X2048Y200C3\\[Lin-Kir2.1-T2A-aKv1.1-mScarlet] +dox_P0D4-4.nd2') as images:

    '''
    images = dict()
    for key, val in sorted(dataset.filenames.items()):
        print(dataset.filenames[val])
        with ND2Reader(dataset.filenames[val]) as images:
            #print(images.metadata)
            plt.imshow(images[key][0])
            images.iter_axes = 'c'
            plt.imshow(images[key][0], cmap = 'gray')
    plt.show()'''

