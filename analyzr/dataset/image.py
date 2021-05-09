import os
import re
from nd2reader import ND2Reader

import matplotlib.pyplot as plt

class Image:
    def __init__(self, path, sampleName, plateID, wellID, fovID, folder):
        self.path = path
        self.sampleName = sampleName
        self.plateID = plateID
        self.wellID = wellID
        self.fovID = fovID
        self.folder = folder

        #self.metadata = self.__extractFromMetadata__()

        self.__read__()
        #self.print_parameters()
        #self.print_metadata()
        #print("Created dataset ", folder)

    def __read__(self):
        with ND2Reader(self.path) as images:
            self.metadata = self.__extractFromMetadata__(images)


    def __extractFromMetadata__(self, images):
            return images.metadata


    def print_parameters(self):
        print("PARAMETERS:")
        for att in self.__dict__:
            print(att + ' --> ' + str(self.__dict__[att]))
        print("\n\n")

    def print_metadata(self):
        print("METADATA:")
        for meta in self.metadata:
            print(meta + ' --> ' + str(self.metadata[meta]))
        print("\n\n")

#class Well:
    #def __init__(self):

        '''#print(os.listdir(self.path))
        self.forg_folders = [x for x in os.listdir(self.path) if not x.startswith('~') and os.path.isdir(self.path + x)]
        self.file_list = [x for x in os.listdir(self.path + self.forg_folders[0]) if x.endswith('.nd2')]
        print(self.file_list)
        #single_files = list()
        #for folder in forg_folders[1:]:
        #    single_files.append([x for x in file_list if not os.path.exists(self.path + folder + x)])'''

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
