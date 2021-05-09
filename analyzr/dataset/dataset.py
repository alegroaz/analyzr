import re
import os

from analyzr.dataset.plate import Plate
from analyzr.dataset.well import Well
from analyzr.dataset.fov import Fov
from analyzr.dataset.image import Image

class Dataset:

    plates = dict()

    def __init__(self, path):
        self.path = path
        self.name = re.search('[\\\/](\D{3}-\D{2}\d{3})[\\\/]?', self.path).group(1)
        self.__populate__()
        #self.wells = dict()

    def __populate__(self):
        for root, dirs, files in os.walk(self.path):

            for file in files:
                if file.endswith(".nd2"):
                    folder = re.search("[\\\/]((\D\d+)+)", root).group(1)
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