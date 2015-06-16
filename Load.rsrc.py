{'stack':{'type':'Stack',
          'name':'Template',
    'backgrounds': [
    {'type':'Background',
          'name':'bgTemplate',
          'title':'Standard Template with File->Exit menu',
          'position':(49, 103),
          'size':(378, 406),
          'style':['resizeable'],

        'menubar': {'type':'MenuBar',
         'menus': [
             {'type':'Menu',
             'name':'menuFile',
             'label':'&File',
             'items': [
                  {'type':'MenuItem',
                   'name':'menuFileExit',
                   'label':'E&xit',
                  },
              ]
             },
         ]
     },
         'components': [

{'type':'StaticText', 
    'name':'StaticText4', 
    'position':(225, 70), 
    'size':(89, -1), 
    'text':'tonf/sqr m', 
    },

{'type':'StaticText', 
    'name':'TotalDeadLoad', 
    'position':(125, 70), 
    'text':'1111', 
    },

{'type':'Button', 
    'name':'Cancel', 
    'position':(170, 230), 
    'label':'Cancel', 
    },

{'type':'Button', 
    'name':'OK', 
    'position':(65, 230), 
    'label':'OK', 
    },

{'type':'Button', 
    'name':'DeadDel', 
    'position':(200, 190), 
    'size':(57, -1), 
    'label':'Delete', 
    },

{'type':'Button', 
    'name':'DeadEdit', 
    'position':(135, 190), 
    'size':(57, -1), 
    'label':'Edit', 
    },

{'type':'Button', 
    'name':'Button1', 
    'position':(65, 190), 
    'size':(62, -1), 
    'label':'Add', 
    },

{'type':'StaticText', 
    'name':'StaticText3', 
    'position':(60, 50), 
    'text':'Usage :', 
    },

{'type':'TextField', 
    'name':'TextField2', 
    'position':(115, 45), 
    },

{'type':'StaticText', 
    'name':'tonf/sqr m', 
    'position':(225, 30), 
    'size':(92, -1), 
    'text':'tonf/sqr m', 
    },

{'type':'List', 
    'name':'List1', 
    'position':(55, 90), 
    'size':(219, 86), 
    'items':[], 
    },

{'type':'StaticText', 
    'name':'StaticText2', 
    'position':(30, 70), 
    'text':'Dead Load :', 
    },

{'type':'StaticText', 
    'name':'StaticText1', 
    'position':(30, 30), 
    'size':(74, -1), 
    'text':'Live Load :', 
    },

{'type':'TextField', 
    'name':'TextField1', 
    'position':(115, 25), 
    },

] # end components
} # end background
] # end backgrounds
} }
