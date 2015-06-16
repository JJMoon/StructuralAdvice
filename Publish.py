# M_ : MathML
# H_ : HTML
# from Publish import *


class aLine:
    Name = 'aLine'
    def __init__(self, Astring=''):
        self.S = Astring + '\n'
    
    def indent(self, Size=2):
        self.S = (Size * ' ') + self.S
        
    def Markup(self, Mark, Content, Prop=''):
        self.S = '<' + Mark
        if Prop == '':
            self.S += '>'
        else:
            self.S += ' ' + Prop + '>'
        self.S += Content
        self.S += '</' + Mark + '> \n'


class aCluster:
    Name = 'aCluster'
    def __init__(self, IndentSize=2):
        self.L = [] # List of aLine
        self.IndentSize = IndentSize
        
    def indent(self, Size=2):
        for mem in self.L:
            mem.indent(Size*self.IndentSize)
    def ResetList(self):
        del self.L
        self.L = []
    
    def __add__(self, other): # return new object
        robject=aCluster()
        
        for mem in self.L:
            robject.L.append(mem)
        for mem in other.L:
            robject.L.append(mem)
            
        return robject
           
            
    def Markup(self, Mark, Content, Prop='', Indent=0):
        
        if Content.Name == 'aCluster': # protect from self reference
            ContentCl = aCluster()
            for each in Content.L:
                ContentCl.L.append(each)
        self.ResetList()
    
        str = '<' + Mark
        if Prop == '':
            str += '>'
        else:
            str += ' ' + Prop + '>'
        self.L.insert(0, aLine(str))
        
        if Content.Name == 'aLine':
            self.L.append(Content)
            Content.indent(self.IndentSize) # Apply Default Indent
        if Content.Name == 'aCluster':
            for eachCl in ContentCl.L:
                eachCl.indent(self.IndentSize)
                self.L.append(eachCl)
        
        self.L.append(aLine('</'+ Mark + '>'))

        for mem in self.L:
            mem.indent(Indent*self.IndentSize)

    def Publish(self):
        rvalue = ''
        for mem in self.L:
            rvalue += mem.S
        return rvalue
    def Print(self): 
        for mem in self.L: 
            print mem.S
        
def testCluster(indent):
    al = aLine()
    al.Markup('p', 'New content', 'class=asdf')
    ac = aCluster()
    ac.Markup('td', al, 'prop', 1)
    
    ac.Markup('tr', ac, 'classasdfsdf', indent)
    ac.Markup('table', ac, 'table propclassasdfsdf', 1)
    
    rv = ac.Publish()
    print rv


def H_PrintHead(StyleRef, Title):
    str = """
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2//EN">
<html>
<head>
"""
    str += '<title>' + Title + '</title> \n'
    # <meta name="generator" content="Namo WebEditor v4.0">
    str += '<link rel="stylesheet" href="' + StyleRef + '"> \n'
    str += '</head>'
    return str

def H_Header(border, Company, Title, PageNum):
# border : border thickness
# Company : Name
# ob = H_Header(1, "Company", 'Title', 24)


    al = aLine()
    al.Markup('p', Company, 'class="Title1"')
    col1 = aCluster()
    col1.Markup('td', al, 'width="50%"')
    
    al = aLine(); col2 = aCluster()
    al.Markup('p', 'Project Name :', 'class="Small"')
    col2.L.append(al)
    al = aLine()
    al.Markup('p', Title, 'class="Title1"')
    col2.L.append(al)
    col2.Markup('td', col2, 'width="25%"')
    
    al = aLine(); col3 = aCluster()
    al.Markup('p', 'Page Number :', 'class="Small"')
    col3.L.append(al)
    al = aLine()
    al.Markup('p', str(PageNum), 'class="Title1"')
    col3.L.append(al)
    col3.Markup('td', col3, 'width="25%"')
    
    robject = aCluster()
    robject.Markup('table', col1 + col2 + col3, 'border="' + str(border) + '" width="100%"')
    
    return robject

    
    
# from Publish import *
