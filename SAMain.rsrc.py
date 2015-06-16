{'stack':{'type':'Stack',
          'name':'Template',
    'backgrounds': [
    {'type':'Background',
          'name':'bgTemplate',
          'title':'Standard Template with File->Exit menu',
          'position':(162, 367),
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
             {'type':'Menu',
             'name':'menuLoad',
             'label':'&Load',
             'items': [
                  {'type':'MenuItem',
                   'name':'menuGravity',
                   'label':'&Gravity Load',
                  },
              ]
             },
             {'type':'Menu',
             'name':'menuAnalysis',
             'label':'&Analysis',
             'items': [
                  {'type':'MenuItem',
                   'name':'menuSimpleBeams',
                   'label':'Simple Beams',
                  },
                  {'type':'MenuItem',
                   'name':'menuSimpleFrame',
                   'label':'Simple Frame',
                  },
              ]
             },
             {'type':'Menu',
             'name':'menuRCDesign',
             'label':'&RC Design',
             'items': [
              ]
             },
             {'type':'Menu',
             'name':'menuSTLDesign',
             'label':'&Steel Design',
             'items': [
              ]
             },
             {'type':'Menu',
             'name':'menuMMember',
             'label':'&Misc. Member Design',
             'items': [
              ]
             },
         ]
     },
         'components': [

] # end components
} # end background
] # end backgrounds
} }
