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