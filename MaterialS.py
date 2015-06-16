from Tkinter import *
from Material import *
from Debug import *

'Steel Material Class'

class MaterialS (Material):
    def __init__ (self):
        self.F = 2.4        # Strength          ton/cm2
        self.E = 2100       # Elastic Modulus   ton/cm2
        self.Den = 7.8      # Density           ton/m3
        self.Type = 'S'     # C: Concrete, S: Steel, M: Composite
        
class MatSteelDlg:
    def __init__ (self, parent, GlobalObject):
        self.GObj = GlobalObject

        top = self.top = Toplevel(parent)
        
        Label(top, text="Fy (t,cm)").grid(row=0)
        Label(top, text="E  (t,cm)").grid(row=1)
        Label(top, text="Density (t,m)").grid(row=2)
                
        self.Fy = Entry(top) # debugMes = MessageDlg(str(self.GObj.MatS.F))
        self.Fy.insert(0, self.GObj.MatS.F)
        self.Fy.grid(row=0, column=1)

        self.E = Entry(top)
        self.E.insert(0, self.GObj.MatS.E)
        self.E.grid(row=1, column=1)
        self.Den = Entry(top)
        self.Den.insert(0, self.GObj.MatS.Den)
        self.Den.grid(row=2, column=1)
        
        # Buttons        
        OkBtn=Button(top, text="Apply Properties", command = self.Save)
        OkBtn.pack()
        OkBtn.grid(row=3, column=1)
        
    def Save(self):
        self.GObj.MatS.F =      self.Fy.get()
        self.GObj.MatS.E =      self.E.get()
        self.GObj.MatS.Den =    self.Den.get()

        

