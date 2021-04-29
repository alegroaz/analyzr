import os
from nd2reader import ND2Reader

class Image:
    def __init__(self, path):
        self.path = path
        self.height,\
        self.width,\
        self.timestamp = self.__read__()
        print('SIZE = ' + str(self.height) + ' x ' + str(self.width))


    def __read__(self):
        with ND2Reader(self.path) as images:
            print('IMAGE ' + self.path + ' READ')
            print(images.metadata)
            height = images.metadata['height']
            width = images.metadata['width']
            timestamp = images.metadata['date']
            return height, width, timestamp
            # images.iter_axes = 'c'
            '''axs[c].imshow(images[0], cmap='gray')
            axs[c].set_title(folder)
            c = c + 1'''




class Dataset:
    def __init__(self, path):
        self.path = path
        self.__initialize__()
        #self.filenames = self.__initialize__()

    def __initialize__(self):
        self.forg_folders = [x for x in os.listdir(self.path) if not x.startswith('~') and os.path.isdir(self.path + x)]
        self.file_list = [x for x in os.listdir(self.path + self.forg_folders[0]) if x.endswith('.nd2')]
        #single_files = list()
        #for folder in forg_folders[1:]:
        #    single_files.append([x for x in file_list if not os.path.exists(self.path + folder + x)])

    '''def __initialize__(self):
        forg_folders = os.listdir(self.path)
        # print(forg_folders)
        filenames = dict()
        for folder in forg_folders:
            # print((path + '\\' + folder))
            for file in os.listdir((self.path + '\\' + folder)):
                # print(file)
                filelist = []
                filelist.append(os.path.abspath(self.path + '\\' + folder + '\\' + file))
                filenames[folder] = filelist
        # print(filenames)
        return filenames'''
