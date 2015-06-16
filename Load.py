#!/usr/bin/python

"""
Load
"""

from PythonCardPrototype import model, res, dialog
import os, sys
from wxPython import wx
     
# 4 debugging
# from Load import *

class Load(model.CustomDialog):
    def __init__(self, parent):
        path = os.path.join(parent.stack.app.applicationDirectory, \
                            model.internationalResourceName('Load'))
        aDialogRsrc = res.ResourceFile(path).getResource()
        #model.CustomDialog.__init__(self, parent, aDialogRsrc)

    def on_openBackground(self, event):
        #self.parent = self.GetParent()
        pass


def load(parent):
    dlg = Load(parent)
    dlg.showModal()
    dlg.destroy()


class aLoad:
    def __init__ (self, name='', type='', value=0.):
        self.Name = name        # Name "Concrete", 
        self.Type = type        # Dead, Live
        self.Value = float(value)      # Load tonf/m2

class GravityLoad:
    def __init__ (self):
        self.Name = ''          # Name "Office, Classroom"
        self.DeadList = []
        self.Live = aLoad()
        
    def getLive(self):
        return self.Live.Value

    def getDead(self):
        rvalue = 0.0
        for item in self.DeadList:
            rvalue += item.Value
        return rvalue
    def addDead(self, name, value):
        aDead = aLoad(name, 'D', value)
        self.DeadList.append(aDead)
    def setLive(self, name, value):
        self.Live.Name = name
        self.Live.Value = float(value)


def TestLoad():
    aSet = GravityLoad()
    aSet.addDead('Concrete', 288.0)

