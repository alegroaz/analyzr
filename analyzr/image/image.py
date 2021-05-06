import os
import re
from nd2reader import ND2Reader

class Dataset:

    plates = dict()

    def __init__(self, path):
        self.path = path
        self.name = re.search(r'\\(\D{3}-\D{2}\d{3})\\$', self.path).group(1)
        self.__populate__()
        #self.wells = dict()

    def __populate__(self):
        for root, dirs, files in os.walk(self.path):

            for file in files:
                if file.endswith(".nd2"):
                    folder = re.search(r"\\((\D\d+)+)", root).group(1)
                    sampleName, \
                    plateID, \
                    wellID, \
                    fovID = self.__extractFromPath__(file)

                    if plateID not in self.plates.keys():
                        self.plates[plateID] = Plate(plateID)
                    if wellID not in self.plates[plateID].wells.keys():
                        self.plates[plateID].wells[wellID] = Well(wellID, sampleName)
                    if fovID not in self.plates[plateID].wells[wellID].fovs.keys():
                        self.plates[plateID].wells[wellID].fovs[fovID] = Fov(fovID)

                    # Make fov.images a dict() !!!!! Need to extract the folder name from path
                    self.plates[plateID].wells[wellID].fovs[fovID].images[folder] = Image(os.path.join(root, file), sampleName, plateID, wellID, fovID, folder)

                #read = Image(os.path.join(root, file))


    def __extractFromPath__(self, filename):
        # Determines Dimensions and Sample_name
        pattern = r"(?P<sample>.+)_"
        extracted = re.search(pattern, filename)
        sampleName = extracted['sample']

        # Determines Plate ID, well ID, and FOV ID
        pattern = r"_P(?P<plate>[\d]+)(?P<well>[A-Z][\d]+)-(?P<fov>\d+)"
        extracted = re.search(pattern, filename)

        plateID = int(extracted['plate'])
        wellID = extracted['well']
        fovID = int(extracted['fov'])

        return sampleName, plateID, wellID, fovID

    def tree(self):
        prefix = ""
        for x in self.plates:
            plate = self.plates[x]
            print("Plate --> ", plate.plateID)
            plate.printChildren(prefix + " ")

class Plate:

    wells = dict()

    def __init__(self, plateID):
        self.plateID = plateID
        self.wells = dict()

        #print("Created plate ", plateID)

    def printChildren(self, prefix = ""):
        if len(self.wells) == 1:
            for x in self.wells:
                well = self.wells[x]
                print(prefix, "└── ", "Well --> ", well.wellID, " - ", well.sampleName)
        else:
            for x in self.wells:
                well = self.wells[x]
                print(prefix, "├── ", "Well --> ", well.wellID, " - ", well.sampleName)
                well.printChildren(prefix + " │    ")

class Well:

    def __init__(self, wellID, sampleName):
        self.wellID = wellID
        self.sampleName = sampleName
        self.fovs = dict()
        #print("Creaated well ", wellID)

    def printChildren(self, prefix = ""):
        if len(self.fovs) == 1:
            for x in self.fovs:
                fov = self.fovs[x]
                print(prefix, "└── ", "FOV --> ", fov.fovID)
                fov.printChildren(prefix + "    ")
        else:
            for x in self.fovs:
                fov = self.fovs[x]
                print(prefix, "├── ", "FOV --> ", fov.fovID)
                fov.printChildren(prefix + "    ")

class Fov:
    #Make it a dict() !!!!! Need to extract the folder name from path

    def __init__(self, fovID):
        self.fovID = fovID
        self.images = dict()
        #print("Created FOV ", fovID)

    def printChildren(self, prefix = ""):
        for x in self.images:
            img = self.images[x]
            print(prefix, "└── ", "Type --> ", img.folder)

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
        #print("Created image ", folder)

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
