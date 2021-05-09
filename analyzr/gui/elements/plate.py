from PyQt5.QtWidgets import QMainWindow, QWidget, QHBoxLayout
from PyQt5.QtGui import QPainter, QPainterPath, QPen, QColor
from PyQt5.QtCore import Qt, QRectF


class ControlBar(QWidget):
    """ docstring for ControlBar"""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setGeometry(10, 10, 100, 200)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setStyleSheet('''background-color : red;''')
        #self.buildUi()
        #self.show()

    def mousePressEvent(self, event):
        quit()

    def mouseMoveEvent(self, event):
        try:
              x=event.globalX()
              y=event.globalY()
              x_w = self.offset.x()
              y_w = self.offset.y()
              self.move(x-x_w, y-y_w)
        except: pass

    '''def paintEvent(self, ev):
        painter = QPainter(self)
        painter.setBrush(Qt.blue)
        painter.drawRoundedRect(QRectF(10, 10, 50, 50))'''

    '''def buildUi(self):
        self.hoelayout = QHBoxLayout()
        self.openBtn = QWidget()
        self.hoelayout.addStretch(1)
        self.hoelayout.addWidget(self.openBtn)
        self.setLayout(self.hoelayout)'''
