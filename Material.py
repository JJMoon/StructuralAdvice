
'Material Class'

class Material:
    def __init__ (self):
        self.F = 0.1        # Strength          ton/cm2
        self.E = 100        # Elastic Modulus   ton/cm2
        self.Den = 1.0      # Density           ton/m3
        self.Type = 'C'     # C: Concrete, S: Steel, M: Composite
        
    def SetProp(F, E, Den, Type):
        self.F = F
        self.E = E
        self.Den = Den
        self.Type = Type


from MaterialS import *
