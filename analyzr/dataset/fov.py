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