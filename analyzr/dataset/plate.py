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