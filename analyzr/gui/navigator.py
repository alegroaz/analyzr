from PyQt5.QtWidgets import QMainWindow, QPushButton
from PyQt5.QtGui import QPainter, QPainterPath, QPen, QColor
from PyQt5.QtCore import Qt, QRectF

from analyzr.gui.elements.plate import ControlBar

class Navigator(QMainWindow):


    def __init__(self, parent=None):
        super(Navigator, self).__init__(parent)
        self.title = 'Navigator'
        self.left = 200
        self.top = 200
        self.width = 1028
        self.height = 768
        self.__init_UI__()
        #self.__draw_shape()
        self.setCentralWidget(ControlBar())
        self.show()


    def __init_UI__(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)


    '''def paintEvent(self, event):
        shape = QPainter(self)
        shape.setRenderHint(QPainter.Antialiasing)
        path = QPainterPath()
        path.addRoundedRect(QRectF(10, 10, self.width-20, self.height-20), 50, 50)
        pen = QPen(Qt.black, 2)
        shape.setPen(pen)
        shape.fillPath(path, Qt.white)
        shape.setStyleSheet(background-color: #262626;)
        shape.drawPath(path)
        print("shape drew")'''
