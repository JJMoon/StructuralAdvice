from anygui import *


def designGirt(Fy, span, spacing, deadLoad, windLoad, sagRodSpan, Zx, Zy) :
# Fy: t/cm2, span: m, spacing:m, Load: t/m2, sag: m
# Z: cm3

    if Fy * Zx * Zy <= 1e-100: # simple non zero check
        return -1
        
    wx = windLoad * spacing # wind load
    wy = deadLoad * spacing # self load
    
    Mx = wx * pow(span,2) / 8
    My = wy * pow(span,2) / 8
    
    ft = Fy / 1.5 # Allowable Tension Stress
    
    StressX = Mx / Zx
    StressY = My / Zy
    
    if StressY/ft <= 1.0:
        DeadCheck = 'OK'
    else:
        DeadCheck = 'NG'
        
    if StressX/(1.5*ft) + StressY/(1.5*ft)  <= 1.0:
        WindCheck = 'OK'
    else:
        WindCheck = 'NG'
        
    # Display Part
    
    # wx, wy
    stringa = 'Wind Load(%.3f) * Spacing(%.3f) = wx (%.3f)' % (windLoad, spacing, wx)
    lblwx = Label(text=stringa, position=(100,100), size=(400,100))
    lblwy = Label(text=stringa, position=(100,150), size=(400,100))
    
    
    MainWin = Window()
    MainApp = Application()
    
    MainWin.title = 'Structural Advice'
    MainWin.size =(800, 600)
    
    MainWin.add(lblwx, direction='right')

    MainWin.add(lblwy, direction='right')

    
    MainApp.add(MainWin)
    MainApp.run()
        
    
    
if __name__ == '__main__':
    designGirt(2.4, 4.5, 0.85, 0.032, 0.064, 4.5, 16.10, 6.06)

