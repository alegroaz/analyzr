import sys
import matplotlib.pyplot as plt
import numpy as np
import cv2


from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QStatusBar, QToolBar
from PyQt5 import QtGui

from analyzr.gui.navigator import Navigator
from analyzr.gui.browser import Browser

from nd2reader import ND2Reader

class Launcher(QMainWindow):
    """Main Window."""

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle('Analyzr')
        self.setCentralWidget(Navigator())

        self._createMenu()

        #self._createToolBar()

        self._createStatusBar()

    def _createMenu(self):
        self.menu = self.menuBar().addMenu("&Menu")
        self.menu.addAction('&Exit', self.close)
        self.menu.addAction('&Browse Project Folder', self.browse)

    def _createToolBar(self):
        tools = QToolBar()

        self.addToolBar(tools)

        tools.addAction('Exit', self.close)

    def _createStatusBar(self):
        status = QStatusBar()

        status.showMessage("I'm the Status Bar")

        self.setStatusBar(status)

    def browse(self):
        global default_path
        global default_directory

        path = Browser(default_directory).get_path()
        return path





        '''with ND2Reader(
                'C:\\Users\\alegr\\Documents\\University\\St-Pierre\\Sample data\\KIN-AG004\\X2048Y200C3\\[Lin-Kir2.1-T2A-aKv1.1-mScarlet] +dox_P0D4-4.nd2') as images:
            print(images.metadata)
            plt.imshow(images[0])
            images.iter_axes = 'c'
            plt.imshow(images[0])
            plt.show()
        self.main_window.show()'''

        # print_hi('PyCharm')