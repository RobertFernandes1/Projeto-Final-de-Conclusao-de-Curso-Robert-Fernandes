from fem01 import fem01
from fem02 import fem02
from fem03 import fem03
from fem04 import fem04
from fem05 import fem05

import numpy as np
def objective(xyz):
    D1=  xyz[0]
    D2=  xyz[1]
    D3=  xyz[2]
    D4 = xyz[3]
    D5 = xyz[4]
    D6 = xyz[5]
    D7 = xyz[6]
    D8 = xyz[7]
    D9 = xyz[8]
    D10 = xyz[9]
    D11 = xyz[10]
    D12 = xyz[11]
    D13 = xyz[12]
    D14 = xyz[13]
    D15 = xyz[14]

    Di1=(0.7558*xyz[0]-1.2229)
    Di2=(0.7558*xyz[1]-1.2229)
    Di3=(0.7558*xyz[2]-1.2229)
    Di4 = 0.7558 * xyz[3] - 1.2229
    Di5 = 0.7558 * xyz[4] - 1.2229
    Di6 = 0.7558 * xyz[5] - 1.2229
    Di7 = 0.7558 * xyz[6] - 1.2229
    Di8 = 0.7558 * xyz[7] - 1.2229
    Di9 = 0.7558 * xyz[8] - 1.2229
    Di10 = 0.7558 * xyz[9] - 1.2229
    Di11 = 0.7558 * xyz[10] - 1.2229
    Di12 = 0.7558 * xyz[11] - 1.2229
    Di13 = 0.7558 * xyz[12] - 1.2229
    Di14 = 0.7558 * xyz[13] - 1.2229
    Di15 = 0.7558 * xyz[14] - 1.2229

    L1=579.3029136816075
    L2=80.06613828579466
    L3=487.28224264793397
    L4=401.9335349283511
    L5=24.934684678174705
    L6=19.995191922059668
    L7=29.063938136460433
    L8=20.0
    L9=25.0
    L10=25.0
    L11=20.0
    L12=476.3842255994629
    L13=476.3842255994629
    L14=409.9981884106319
    L15=409.9981884106319

    A1=(np.pi/4)*((D1**2)-(Di1**2))
    A2=(np.pi/4)*((D2**2)-(Di2**2))
    A3=(np.pi/4)*((D3**2)-(Di3**2))
    A4 = (np.pi/4) * ((D4**2) - (Di4**2))
    A5 = (np.pi/4) * ((D5**2) - (Di5**2))
    A6 = (np.pi/4) * ((D6**2) - (Di6**2))
    A7 = (np.pi/4) * ((D7**2) - (Di7**2))
    A8 = (np.pi/4) * ((D8**2) - (Di8**2))
    A9 = (np.pi/4) * ((D9**2) - (Di9**2))
    A10 = (np.pi/4) * ((D10**2) - (Di10**2))
    A11 = (np.pi/4) * ((D11**2) - (Di11**2))
    A12 = (np.pi/4) * ((D12**2) - (Di12**2))
    A13 = (np.pi/4) * ((D13**2) - (Di13**2))
    A14 = (np.pi/4) * ((D14**2) - (Di14**2))
    A15 = (np.pi/4) * ((D15**2) - (Di15**2))

    #Ro=0.0000027
    Ro=0.0027
    M = Ro * (L1*A1 + L2*A2 + L3*A3 + L4*A4 + L5*A5 + L6*A6 + L7*A7 + L8*A8 + L9*A9 + L10*A10 + L11*A11 + L12*A12 + L13*A13 + L14*A14 + L15*A15)

    return M


#Starting guess
xyz_start= [7.5,7.5,7.5,7.5,7.5,7.5,7.5,7.5,7.5,7.5,7.5,7.5,7.5,7.5,7.5]

#Constraints
#Fator de segurança
FS=1.5
#Tensao de escoamento
Tensao_escoamento=275

#Restricoes de limite de escoamento
def restricao1(x):
    return Tensao_escoamento-fem01(x)*FS

def restricao2(x):
    return Tensao_escoamento-fem02(x)*FS

def restricao3(x):
    return Tensao_escoamento-fem03(x)*FS

def restricao4(x):
    return Tensao_escoamento-fem04(x)*FS

def restricao5(x):
    return Tensao_escoamento-fem05(x)*FS

#Restricoes geometricas do quadro

#soldagem
#Tubo 1 e 2
def restricao6(x):
    D1=x[0]
    D2=x[1]
    return D2-D1

#Tubo 3 e 2
def restricao7(x):
    D2=x[1]
    D3=x[2]
    return D2-D3

#Tubo 3 e 4
def restricao8(x):
    D3=x[2]
    D4=x[3]
    return D4-D3

#Tubo 12 e 4
def restricao9(x):
    D12=x[11]
    D4=x[3]
    return D4-D12
#Tubo 14 e 8
def restricao10(x):
    D14=x[13]
    D8=x[7]
    return D8-D14

#simetria

#Tubo 7 e 4
def restricao11(x):
    D7=x[6]
    D4=x[3]
    return D7-D4

#Tubo 6 e 2
def restricao12(x):
    D6=x[5]
    D2=x[1]
    return D6-D2

#Tubo 5 e 2
def restricao13(x):
    D5=x[4]
    D2=x[1]
    return D5-D2

#Tubo 9 e 8
def restricao14(x):
    D9=x[8]
    D8=x[7]
    return D9-D8

#Tubo 10 e 8
def restricao15(x):
    D10=x[9]
    D8=x[7]
    return D10-D8

#Tubo 11 e 8
def restricao16(x):
    D11=x[10]
    D8=x[7]
    return D11-D8

#Tubo 13 e 12
def restricao17(x):
    D13=x[12]
    D12=x[11]
    return D13-D12

#Tubo 14 e 12
def restricao18(x):
    D14=x[13]
    D12=x[11]
    return D14-D12

#Tubo 15 e 12
def restricao19(x):
    D15=x[14]
    D12=x[11]
    return D15-D12



cons1={'type':'ineq','fun':lambda xyz: restricao1(xyz)}
cons2={'type':'ineq','fun':lambda xyz: restricao2(xyz)}
cons3={'type':'ineq','fun':lambda xyz: restricao3(xyz)}
cons4={'type':'ineq','fun':lambda xyz: restricao4(xyz)}
cons5={'type':'ineq','fun':lambda xyz: restricao5(xyz)}

cons6={'type':'ineq','fun':lambda xyz: restricao6(xyz)}
cons7={'type':'ineq','fun':lambda xyz: restricao7(xyz)}
cons8={'type':'ineq','fun':lambda xyz: restricao8(xyz)}
cons9={'type':'ineq','fun':lambda xyz: restricao9(xyz)}
cons10={'type':'ineq','fun':lambda xyz: restricao10(xyz)}

cons11={'type':'eq','fun':lambda xyz: restricao11(xyz)}
cons12={'type':'eq','fun':lambda xyz: restricao12(xyz)}
cons13={'type': 'eq', 'fun': lambda xyz: restricao13(xyz)}
cons14={'type': 'eq', 'fun': lambda xyz: restricao14(xyz)}
cons15={'type': 'eq', 'fun': lambda xyz: restricao15(xyz)}
cons16={'type': 'eq', 'fun': lambda xyz: restricao16(xyz)}
cons17={'type': 'eq', 'fun': lambda xyz: restricao17(xyz)}
cons18={'type': 'eq', 'fun': lambda xyz: restricao18(xyz)}
cons19={'type': 'eq', 'fun': lambda xyz: restricao19(xyz)}

con=[cons1,cons2,cons3,cons4,cons5,cons6,cons7,cons8,cons9,cons10, cons11, cons12, cons13, cons14, cons15, cons16, cons17, cons18, cons19]
#con=[cons1,cons2,cons3,cons4,cons5]

#Optimizing

a=(7.5,50)

bnds=(a,a,a,a,a,a,a,a,a,a,a,a,a,a,a)

from scipy.optimize import minimize

result=minimize(objective, xyz_start, method='SLSQP',bounds=bnds, options={'ftol': 1e-9,"disp": True,"maxiter":10000}, constraints=con)
print(result)


