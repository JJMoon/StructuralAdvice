from anygui import *
from math import *



def getCompStress(E, Fy, Lcomp, i):
# E : t/cm2, Fy: t/cm2, Moment : t.m, Lcomp(Compression side Length) : m
# BeamH : cm, Af : cm2, ib : cm, M1/M2 : Any same unit(M1:EndSect, M2:Mid)

# getCompStress(2100, 2.4, 5, 5)

    assert Lcomp > 0.1 and i > 0.1
    
    lambP = getLambdaP(E, Fy)
    lamb = Lcomp * 100 / i
    
    n = 3./2. + 2./3 * pow(lamb/lambP,2) # Safety Factor
    
    if lamb <= lambP:
        fc = (1 - 0.4 * pow(lamb/lambP,2)) * Fy / n
        str = "1-0.4"
    else:
        fc = 0.277 * Fy / pow(lamb/lambP,2)
        str = "0.277 * "
                
    return lamb, str, n, fc


def getBendStress(E, Fy, Lcomp, ib, BeamH, Af, M1, M2):
# E : t/cm2, Fy: t/cm2, Moment : t.m, Lcomp(Compression side Length) : m
# BeamH : cm, A3f : cm2, ib : cm, M1/M2 : Any same unit(M1:EndSect, M2:Mid)

#   from Steel import *
#   chkBending(2100, 2.4, 5, 5, 60, 20, -30, 20)

    assert Lcomp > 0.1 and ib > 0.1 and BeamH > 1 and Af > 0.1
    assert abs(M2) > 1e-100
    assert Af > 0.1
    

    ft = Fy/1.5
    
    if M1*M2 > 0:
        sign = 1.
    else:
        sign = -1.
    
    M1 = abs(M1) # Absolute Value
    M2 = abs(M2)
   
    Lbuck = Lcomp*100. / ib # in cm
    
    if abs(M1) < 1e-100:
        Cm = 1.
    else:
        Cm = 1.75 - 1.05 * sign * (M2/M1) + 0.3 * pow(M2/M1,2)
    
    if Cm >= 2.3:
        Cm = 2.3
        
    lambP = getLambdaP(E, Fy)
    
    fb1 = (1 - 0.4 * pow(Lbuck,2) / (Cm * pow(lambP,2)) ) * ft
    
    fb2 = 900. / (Lcomp * 100 * BeamH / Af)
    
    if fb1 > fb2:
        fb = fb1
        eqa = "1-0.4"
    else:
        fb = fb2
        eqa = "900 / "
        
    return (fb1, fb2, fb, eqa)


def getLambdaP(E, Fy):
# E: t/cm2
    return sqrt( pow(pi,2) * E / (0.6 * Fy) )


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

