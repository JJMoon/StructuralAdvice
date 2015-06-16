class Sect:
    """Structural Geometry. Root of H, C, Pipe, Tube..."""
    
    def __init__(self):
        self.area = self.zx = self.zy = self.Ix = self.Iy = 0 # in cm
    
    def setProp(self, Area, Zx, Zy, pIx, pIy, ix, iy, ib):
        self.area = Area
        self.zx = Zx
        self.zy = Zy
        self.Ix = pIx
        self.Iy = pIy
        self.ix = ix
        self.ix = ix
        self.ib = ib



class HSect(Sect):
    """H Section ex) H 150 x 50 x 4 x 6 makeHSections() """

    def __init__(self, Depth, Width, tw, tf):
        self.width = Width  # in mm 
        self.depth = Depth
        self.thkF = tf
        self.thkW = tw
      
# Section List..
H100x50x4x6 =   HSect       (100,   50,     4,  6)
H100x50x4x6.setProp         (9.94,  32.6,   5.04,   163.,    12.6, 4.05, 1.13, 1.31)
H150x150x7x10 = HSect       (150,   150,    7,  10)
H150x150x7x10.setProp       (40.14, 219.,   75.1,   1640.,   563., 6.39, 3.75, 4.12)


# Section Array

HSecArr = []
HSecArr.append(H100x50x4x6)
HSecArr.append(H150x150x7x10)

# from Section import *

  
