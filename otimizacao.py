# -*- coding: utf-8 -*-
from fem import fem

def objective(xyz):
    D1=xyz[0]
    D2=xyz[1]
    D3=xyz[1]
    L1=100
    L2=L1
    L3=L1
    Ro=1.76
    M=Ro*(L1*(0.138012*D1+0.015595)+L2*(0.138012*D2+0.015595)+L3*(0.138012*D3+0.015595))
    return M


#Starting guess
xyz_start= [10,10,10]

#Constraints
#Fator de segurança
FS=1.5
#Tensao de escoamento
Tensao_escoamento=275
def restricao1(x):

    return Tensao_escoamento-fem(x)*FS

cons={'type':'ineq','fun':lambda xyz: restricao1(xyz)}
#Optimizing

a=(2,10)
b=(2,10)
c=(2,10)

bnds=(a,b,c)

from scipy.optimize import minimize


result=minimize(objective, xyz_start, method='SLSQP',bounds=bnds, options={'ftol': 1e-9,"disp": True}, constraints=cons)
print(result)

