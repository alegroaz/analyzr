
from PyQt5.QtWidgets import QWidget, QFileDialog

class Browser(QWidget):

    def __init__(self, defaultDirectory):
        super().__init__()
        self.title = 'Select Data Folder'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.defaultDirectory = defaultDirectory
        self.__init_UI__()
        self.show()

    def __init_UI__(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.__open_directory_dialog__()

    def __open_directory_dialog__(self):
        #options = QFileDialog.Options()
        #options |= QFileDialog.DontUseNativeDialog

        dialog = QFileDialog()
        if self.defaultDirectory != "":
            dialog.setDirectory(self.defaultDirectory)

        self.path = dialog.getExistingDirectory(self, 'Select Data Folder')

    def get_path(self):
        return self.path
