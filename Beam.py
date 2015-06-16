# Beam Class
'Beam Class'

class Beam:
    def __init__ (self):
        self.Name = 'No Name'   # Name "B1, G1"
        self.Material = 'Material'
        self.Section = 'imsy'   # Section Class
        self.Type = 'G'         # 'G'irder, 'B'eam
        self.Forces = [ [0,0,0],  [0,0,0],  [0,0,0] ] 
            # MaxMom, MinMom, Shear
        
        
from BeamStl import *
