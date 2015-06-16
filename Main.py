import sys
from Tkinter import *
from SteelBeamDlg import *
from Material import * #import All Material related classes
from Beam import * #import All Material related classes
#from Section import * #import All Material related classes
from Compo import *

'This is Advice Main Module'

# global is OK in this file...
global Gobject
Gobject = GlobalObj()

class App:
    def __init__ (self, master):
        self.mast = master
        menubar = Menu(master)

        # Sub Menu '''Manage'''
        ManMenu = Menu(menubar, tearoff=0)       
        ManMenu.add_command(label="Open")
        ManMenu.add_command(label="Save")
        ManMenu.add_separator()
        ManMenu.add_command(label="Load")
        ManMenu.add_command(label="Code")
        ManMenu.add_command(label="Steel", command=self.MatSteel)
        ManMenu.add_command(label="Concrete")
        ManMenu.add_separator()

        # Sub Menu '''Analysis'''
        AnalysMenu = Menu(menubar, tearoff=0)       
        AnalysMenu.add_command(label="Simple Beam")
        AnalysMenu.add_command(label="Frame")

        # Sub Menu '''Steel'''
        SteelMenu = Menu(menubar, tearoff=0)       
        SteelMenu.add_command(label="Beam", command=self.SteelBeam)
        SteelMenu.add_command(label="Column")
        SteelMenu.add_command(label="Brace")
        SteelMenu.add_command(label="Connection")
        SteelMenu.add_separator()
    
        # Sub Menu '''Concrete'''
        ConcMenu = Menu(menubar, tearoff=0)       
        ConcMenu.add_command(label="Beam")
        ConcMenu.add_command(label="Column")
        ConcMenu.add_command(label="Footing")
        ConcMenu.add_command(label="Re-Wall")
        ConcMenu.add_separator()

        # Main Menus
        menubar.add_cascade(label="Manage", menu=ManMenu)
        menubar.add_cascade(label="Analysis", menu=AnalysMenu)
        menubar.add_cascade(label="Steel", menu=SteelMenu)
        menubar.add_cascade(label="RC", menu=ConcMenu)
        master.config(menu=menubar)

    def MatSteel(self):
        MatStlDlg = MatSteelDlg(self.mast, Gobject)
        self.mast.wait_window(MatStlDlg.top)

    def SteelBeam(self):        
        StlList = ASDStlBeamList(self.mast, Gobject)
        self.mast.wait_window(StlList.top)
    
if __name__ == '__main__':
    root = Tk()
    app = App(root)
    root.mainloop()

