'Components .. Global Objects'
from Material import *
from Section import *
from Debug import MessageDlg
from Options import Option

class GlobalObj:
    def __init__ (self):
        self.Opt = Option()
        
        self.MatS = MaterialS()
        
        self.StlBmList = []
        
        # Sections..
        self.SectionList = []
        self.SetSectionH()
        
        # Members
        # Beams
        self.BeamList = []
        
        # debugMes = MessageDlg(str(self.MatS.F))
        
    def SetSectionH(self):
        # N, Ix, Iy, Zx, Zy, 
        # ix, iy, ib, Area, UWeit, D, W, T1, T2)
        aSec = SectionH()
        aSec.SetProp('100x50x4x6', 163, 12.6, 32.6, 5.04, \
          4.05, 1.13, 1.31, 9.940, 7.8, 100, 50, 4, 6)
        self.SectionList.append(aSec)
        aSec = SectionH()
        aSec.SetProp('100x100x6x8', 383, 134, 76.5, 26.7, \
          4.18, 2.47, 2.73, 21.9, 17.2, 100, 100, 6, 8)
        self.SectionList.append(aSec)
        aSec = SectionH()
        aSec.SetProp('175x90x5x8', 1210, 97.5, 139, 21.7, \
          7.26, 2.06, 2.38, 23.04, 18.1, 175, 90, 5, 8)
        self.SectionList.append(aSec)
        aSec = SectionH()
        aSec.SetProp('300x200x8x12', 11300, 1600, 771, 160, \
          12.5, 4.71, 5.32, 72.38, 56.8, 300, 200, 8, 12)
        self.SectionList.append(aSec)
        aSec = SectionH()
        aSec.SetProp('300x300x10x15', 20400, 6750, 1360, 450, \
          13.1, 7.51, 8.23, 119.8, 94, 300, 300, 10, 15)
        self.SectionList.append(aSec)
        aSec = SectionH()
        aSec.SetProp('496x199x9x14', 41900, 1840, 1690, 185, \
          20.3, 4.27, 5.08, 101.3, 79.5, 496, 199, 9, 14)
        self.SectionList.append(aSec)
      
        

        

