{'stack':{'type':'Stack',
          'name':'Template',
    'backgrounds': [
    {'type':'Background',
          'name':'bgTemplate',
          'title':'Standard Template with File->Exit menu',
          'position':(62, 187),
          'size':(400, 300),
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

{'type':'Button', 
    'name':'Button1', 
    'position':(99, 75), 
    'size':(110, 50), 
    'label':'Button1', 
    },

] # end components
} # end background
] # end backgrounds
} }
