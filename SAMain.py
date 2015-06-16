#!/usr/bin/python

"""
__version__ = "$Revision: 1.5 $"
__date__ = "$Date: 2002/03/08 01:43:29 $"
"""
from PythonCardPrototype import model, res, dialog
import os, sys

import Load 

# KEA 2001-12-11
# if you want to build a standalone executable using py2exe
# then uncomment the import line below
# due to the way the dynamic imports of components work, each
# component that an app uses needs to be imported statically when
# doing a py2exe build
#from PythonCardPrototype.components import textfield

class Main(model.Background):

    def on_menuGravity_select(self, event):
        self.GLoad = Load.load(self)




if __name__ == '__main__':
    app = model.PythonCardApp(Main)
    app.MainLoop()
