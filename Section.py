from Tkinter import *
# Section Class
'Section Class'

class Section:
    def __init__ (self):
        self.Name = 'No Name'   # Name "B1, G1"
        self.Type = 'none'      # H, Rect, Pipe, Tube, L, Channel
        # Mechanical Properties
        self.Ix = 0     # cm4
        self.Iy = 0     # cm4
        self.Zx = 0     # cm3
        self.Zy = 0     # cm3
        self.ix = 0     # cm
        self.iy = 0     # cm
        self.ib = 0     # cm
        self.Area = 0   # cm2
        self.UnitWeight = 0  # kg/m
        self.Width = 0  # mm (B)
        self.Depth = 0  # mm (H)

        

class SectionH (Section):
    def __init__ (self):
        self.ThkWeb = 0     # mm Web Thickness
        self.ThkFlange = 0  # mm Flange Thickness
        
    def SetProp(self, N, Ix, Iy, Zx, Zy, ix, iy, ib, Area, UWeit, D, W, T1, T2):
        self.Name = N
        self.Ix = Ix
        self.Iy = Iy
        self.Zx = Zx
        self.Zy = Zy
        self.ix = ix
        self.iy = iy
        self.ib = ib
        self.Area = Area
        self.UnitWeight = UWeit
        self.Depth = D
        self.Width = W
        self.ThkWeb = T1
        self.ThkFlange = T2


class SectionP (Section):
    def __init__ (self):
        self.Rad = 0    # mm (radius)    
        
        
        
class SectionSelectDlg:
    def __init__(self, parent, Gobject):
        # Global member Set..
        self.GObject = Gobject    
        DTC = self.GObject.Opt.DlgTxtClr # Dialog Text Color
        top = self.top = Toplevel(parent)
                
        Gobject.SectionList
        
        self.SecList = Listbox(top, selectmode = SINGLE)

        for item in Gobject.SectionList:
            self.SecList.insert(END, item.Name)
        self.SecList.pack()

        self.SecList.bind("<Button-1>", self.SetRtnValue)
        self.SecList.bind("<Leave>", self.SetRtnValue)        
        self.SecList.bind("<Key>", self.SetRtnValue)        
        
#    def __del__(self): self.index = self.SecList.curselection()
        
        
        
    def SetRtnValue(self, event):
        self.index = self.SecList.curselection()
        
