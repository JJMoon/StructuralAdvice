class Section:
    """Structural Geometry. Root of H, C, Pipe, Tube..."""
    area = zx = zy = Ix = Iy = 0 # in cm
    
    
    def setProp(Area, Zx, Zy, pIx, pIy):
        area = Area
        zx = Zx
        zy = Zy
        Ix = pIx
        Iy = pIy
    


class HSection(Section):
    
    width = depth = thkF = thk = 0 # in mm
    
    def __init__(self, Depth, Width, tw, tf):
        width = Width
        depth = Depth
        thkF = tf
        thkW = tw




#H100x50x4x6 =   HSection    (100,   50,     4,  6)
#H100x50x4x6.setProp         (9.94,  32.6,   5.04,   163,    12.6)
#H150x150x7x10 = HSection    (150,   150,    7,  10)
#H100x50x4x6.setProp         (40.14, 219,    75.1,   1640,   563)

      



  
