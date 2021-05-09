import sys

from PyQt5.QtWidgets import QApplication

from analyzr.dataset.dataset import Dataset
from analyzr.gui.browser import Browser
from analyzr.gui.launcher import Launcher

# ----------------------------------------------------------------------------------------------------------------------
# OPTIONAL PARAMETERS
# default_path = "C:\\Users\\alegr\\Documents\\University\\St-Pierre\\Sample data\\KIN-AG004\\"
default_path = ""

default_directory = r"C:\Users\alegr\Documents\University\St-Pierre\Sample data"
# default_directory = ""

# ----------------------------------------------------------------------------------------------------------------------


def select_project(path, default_directory):
    if path != "":
        return path

    path = Browser(default_directory).get_path()
    return path


def main():

    app = QApplication(sys.argv)
    launcher = Launcher()
    launcher.show()

    '''path = select_project(default_path, default_directory)

    if path == "":
        quit()

    dataset = Dataset(path)
    dataset.tree()'''





    sys.exit(app.exec_())









