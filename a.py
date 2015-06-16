#!/usr/bin/python

"""
__version__ = "$Revision: 1.5 $"
__date__ = "$Date: 2002/03/08 01:43:29 $"
"""

from PythonCardPrototype import model, res
import os
import child

# KEA 2001-12-11
# if you want to build a standalone executable using py2exe
# then uncomment the import line below
# due to the way the dynamic imports of components work, each
# component that an app uses needs to be imported statically when
# doing a py2exe build
#from PythonCardPrototype.components import textfield

class DlgA(model.Background):

    def on_openBackground(self, event):
        #path = self.stack.app.applicationDirectory
        path = os.path.join(self.stack.app.applicationDirectory, 'child')
        rsrc = res.ResourceFile(model.internationalResourceName(path)).getResource()
        self.childWindow = child.Child(self.stack, self, rsrc.stack.backgrounds[0])
        self.childWindow.SetPosition((200, 5))
        self.childWindow.Show()
        
    def on_Button1_mouseClick(self, event):
        self.Close()


if __name__ == '__main__':
    app = model.PythonCardApp(DlgA)
    app.MainLoop()
