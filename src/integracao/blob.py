import numpy as np

class Blob:
    __statId = 0
    def __init__(self):
        self.id = self.__statId
        self.nPixel = 0
        self.pixelsY = np.array([])
        self.pixelsX = np.array([])

        self.xmax = -1
        self.xmin = 1e100

        self.ymax = -1
        self.ymin = 1e100

        self.__statId += 1

    def addPixel(self, y, x):
        self.nPixel += 1
        self.pixelsY = np.append(self.pixelsY, y)
        self.pixelsX = np.append(self.pixelsX, x)
        self.ymax = max(y, self.ymax)
        self.ymin = min(y, self.ymin)
        self.xmax = max(x, self.xmax)
        self.xmin = min(x, self.xmin)
        
    def __lt__(self, other):
        return self.xmin < other.xmin