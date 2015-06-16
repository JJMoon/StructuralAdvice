from Beam import *
# Beam Class
'Steel Beam Class'

class BeamStl(Beam):
    def __init__ (self):
        self.Lcomp=0        # meter
        self.M1=0           # 4 Design
        self.M2=0           # 4 Design M1 > M2
        self.Cm=0
        self.fbEqua=0       # 1 or 2
