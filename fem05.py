#Rear wheel braking
def fem05(Diametros):
    import numpy as np
    
    #Pontos barra 1
    x1=0
    y1=0
    z1=0
    
    x2=400.07
    y2=418.97   
    z2=0

    L=((x2-x1)**(2)+(y2-y1)**(2)+(z2-z1)**(2))**(1/2)
    l=(x2-x1)/L
    m=(y2-y1)/L
    n=(z2-z1)/L
    D=(l**2+m**2)**(1/2)
    L1=L
    
    lmbd=np.zeros((3,3))
    lmbd[0]=[l,m,n]
    lmbd[1]=[-m/D,l/D,0]
    lmbd[2]=[-l*n/D,-m*n/D,D]

    T=np.zeros((12,12))
    T[0:3,0:3]=lmbd
    T[3:6,3:6]=lmbd
    T[6:9,6:9]=lmbd
    T[9:12,9:12]=lmbd

    T1=T
    Tt=T.transpose()

    # Matriz de rigidez Local
    Di=(0.7558*Diametros[0]-1.2229)
    A=(np.pi/4)*((Diametros[0]**2)-(Di**2))#Tirei a raiz
    A1=A
    E=69000
    #L=1
    Iy=(np.pi/64)*(Diametros[0]**4-Di**4)
    Iz=(np.pi/64)*(Diametros[0]**4-Di**4)#Di esta dando complexo
    G=25800
    J=(np.pi/32)*(Diametros[0]**4-Di**4)

    #Diagonal principal

    Kch=np.zeros((12,12))
    Kch[(0,0)]=A*E/L
    Kch[(1,1)]=12*E*Iz/L**3
    Kch[(2,2)]=12*E*Iy/L**3
    Kch[(3,3)]=G*J/L
    Kch[(4,4)]=4*E*Iy/L
    Kch[(5,5)]=4*E*Iz/L

    Kch[(6,6)]=A*E/L
    Kch[(7,7)]=12*E*Iz/L**3
    Kch[(8,8)]=12*E*Iy/L**3
    Kch[(9,9)]=G*J/L
    Kch[(10,10)]=4*E*Iy/L
    Kch[(11,11)]=4*E*Iz/L

    #Segundo quadrante
    Kch[1,5]=6*E*Iz/L**2
    Kch[2,4]=-6*E*Iy/L**2
    Kch[4,2]=-6*E*Iy/L**2
    Kch[5,1]=6*E*Iz/L**2

    #Primeiro quadrante
    Kch[(0,6)]=-Kch[(0,0)]
    Kch[(1,7)]=-Kch[(1,1)]
    Kch[(2,8)]=-Kch[(2,2)]
    Kch[(3,9)]=-Kch[(3,3)]
    Kch[(4,10)]=Kch[(4,4)]/2
    Kch[(5,11)]=Kch[(4,4)]/2

    Kch[(1,11)]=Kch[1,5]
    Kch[(2,10)]=Kch[2,4]
    Kch[(3,9)]=-Kch[(3,3)]
    Kch[(4,8)]=-Kch[(2,4)]
    Kch[(5,7)]=-Kch[(5,1)]

    #Terceiro Quadrante

    Kch[6,0]=Kch[(0,6)]
    Kch[7,1]=Kch[(1,7)]
    Kch[8,2]=Kch[(2,8)]
    Kch[9,3]=Kch[(3,9)]
    Kch[10,4]=Kch[(4,10)]
    Kch[11,5]=Kch[(5,11)]

    Kch[(7,5)]=-Kch[(1,11)]
    Kch[(8,4)]=-Kch[(2,10)]
    Kch[(9,3)]=Kch[(3,9)]
    Kch[(10,2)]=-Kch[(4,8)]
    Kch[(11,1)]=-Kch[(5,7)]

    #Quarto Quadrante

    Kch[(7,11)]=-Kch[1,5]
    Kch[(8,10)]=-Kch[2,4]
    Kch[(10,8)]=-Kch[(2,4)]
    Kch[(11,7)]=-Kch[(5,1)]

    Kch1=Kch
    Iy1=Iy
    J1=J
    #Matriz de rigidez global barra 1

    K=np.dot(Tt, Kch)
    K1=np.dot(K,T)

    K1_global=np.zeros((78,78))
    K1_global[:12,:12]=K1[:,:]
    
    ###############################################################################################
    #Pontos barra 2
    x1=400.07
    y1=418.97
    z1=0
    
    x2=375 
    y2=495.01
    z2=0

    L=((x2-x1)**(2)+(y2-y1)**(2)+(z2-z1)**(2))**(1/2)

    l=(x2-x1)/L

    m=(y2-y1)/L

    n=(z2-z1)/L

    D=(l**2+m**2)**(1/2)
    L2=L
    

    lmbd=np.zeros((3,3))
    lmbd[0]=[l,m,n]
    lmbd[1]=[-m/D,l/D,0]
    lmbd[2]=[-l*n/D,-m*n/D,D]

    T=np.zeros((12,12))

    T[0:3,0:3]=lmbd
    T[3:6,3:6]=lmbd
    T[6:9,6:9]=lmbd
    T[9:12,9:12]=lmbd

    T2=T
    Tt=T.transpose()

    # Matriz de rigidez Local
    Di=(0.7558*Diametros[1]-1.2229)
    A=(np.pi/4)*((Diametros[1]**2)-(Di**2))
    A2=A
    E=69000
    #L=1
    Iy=(np.pi/64)*(Diametros[1]**4-Di**4)
    Iz=(np.pi/64)*(Diametros[1]**4-Di**4)
    G=25800
    J=(np.pi/32)*(Diametros[1]**4-Di**4)

    #Diagonal principal

    Kch=np.zeros((12,12))
    Kch[(0,0)]=A*E/L
    Kch[(1,1)]=12*E*Iz/L**3
    Kch[(2,2)]=12*E*Iy/L**3
    Kch[(3,3)]=G*J/L
    Kch[(4,4)]=4*E*Iy/L
    Kch[(5,5)]=4*E*Iz/L

    Kch[(6,6)]=A*E/L
    Kch[(7,7)]=12*E*Iz/L**3
    Kch[(8,8)]=12*E*Iy/L**3
    Kch[(9,9)]=G*J/L
    Kch[(10,10)]=4*E*Iy/L
    Kch[(11,11)]=4*E*Iz/L

    #Segundo quadrante
    Kch[1,5]=6*E*Iz/L**2
    Kch[2,4]=-6*E*Iy/L**2
    Kch[4,2]=-6*E*Iy/L**2
    Kch[5,1]=6*E*Iz/L**2

    #Primeiro quadrante
    Kch[(0,6)]=-Kch[(0,0)]
    Kch[(1,7)]=-Kch[(1,1)]
    Kch[(2,8)]=-Kch[(2,2)]
    Kch[(3,9)]=-Kch[(3,3)]
    Kch[(4,10)]=Kch[(4,4)]/2
    Kch[(5,11)]=Kch[(4,4)]/2

    Kch[(1,11)]=Kch[1,5]
    Kch[(2,10)]=Kch[2,4]
    Kch[(3,9)]=-Kch[(3,3)]
    Kch[(4,8)]=-Kch[(2,4)]
    Kch[(5,7)]=-Kch[(5,1)]

    #Terceiro Quadrante

    Kch[6,0]=Kch[(0,6)]
    Kch[7,1]=Kch[(1,7)]
    Kch[8,2]=Kch[(2,8)]
    Kch[9,3]=Kch[(3,9)]
    Kch[10,4]=Kch[(4,10)]
    Kch[11,5]=Kch[(5,11)]

    Kch[(7,5)]=-Kch[(1,11)]
    Kch[(8,4)]=-Kch[(2,10)]
    Kch[(9,3)]=Kch[(3,9)]
    Kch[(10,2)]=-Kch[(4,8)]
    Kch[(11,1)]=-Kch[(5,7)]

    #Quarto Quadrante

    Kch[(7,11)]=-Kch[1,5]
    Kch[(8,10)]=-Kch[2,4]
    Kch[(10,8)]=-Kch[(2,4)]
    Kch[(11,7)]=-Kch[(5,1)]
    kch2=Kch
    Iy2=Iy
    J2=J
    #Matriz de rigidez global

    K=np.dot(Tt, Kch)
    K2=np.dot(K,T)

    K2_global=np.zeros((78,78))

    K2_global[6:18,6:18]=K2[:,:]

    ####################################################

    #Lambda

    #Pontos barra 3
    x1=375
    y1=495.01
    z1=0
    
    x2=-100.64
    y2=389.13
    z2=0

    L=((x2-x1)**(2)+(y2-y1)**(2)+(z2-z1)**(2))**(1/2)

    l=(x2-x1)/L

    m=(y2-y1)/L

    n=(z2-z1)/L

    D=(l**2+m**2)**(1/2)
    L3=L
    
    lmbd=np.zeros((3,3))

    lmbd[0]=[l,m,n]
    lmbd[1]=[-m/D,l/D,0]
    lmbd[2]=[-l*n/D,-m*n/D,D]

    T=np.zeros((12,12))

    T[0:3,0:3]=lmbd
    T[3:6,3:6]=lmbd
    T[6:9,6:9]=lmbd
    T[9:12,9:12]=lmbd

    T3=T
    Tt=T.transpose()


    # Matriz de rigidez Local
    Di=(0.7558*Diametros[2]-1.2229)
    A=(np.pi/4)*((Diametros[2]**2)-(Di**2))
    A3=A
    E=69000
    #L=1
    Iy=(np.pi/64)*(Diametros[2]**4-Di**4)
    Iz=(np.pi/64)*(Diametros[2]**4-Di**4)
    G=25800
    J=(np.pi/32)*(Diametros[2]**4-Di**4)

    #Diagonal principal

    Kch=np.zeros((12,12))
    Kch[(0,0)]=A*E/L
    Kch[(1,1)]=12*E*Iz/L**3
    Kch[(2,2)]=12*E*Iy/L**3
    Kch[(3,3)]=G*J/L
    Kch[(4,4)]=4*E*Iy/L
    Kch[(5,5)]=4*E*Iz/L

    Kch[(6,6)]=A*E/L
    Kch[(7,7)]=12*E*Iz/L**3
    Kch[(8,8)]=12*E*Iy/L**3
    Kch[(9,9)]=G*J/L
    Kch[(10,10)]=4*E*Iy/L
    Kch[(11,11)]=4*E*Iz/L

    #Segundo quadrante
    Kch[1,5]=6*E*Iz/L**2
    Kch[2,4]=-6*E*Iy/L**2
    Kch[4,2]=-6*E*Iy/L**2
    Kch[5,1]=6*E*Iz/L**2

    #Primeiro quadrante
    Kch[(0,6)]=-Kch[(0,0)]
    Kch[(1,7)]=-Kch[(1,1)]
    Kch[(2,8)]=-Kch[(2,2)]
    Kch[(3,9)]=-Kch[(3,3)]
    Kch[(4,10)]=Kch[(4,4)]/2
    Kch[(5,11)]=Kch[(4,4)]/2

    Kch[(1,11)]=Kch[1,5]
    Kch[(2,10)]=Kch[2,4]
    Kch[(3,9)]=-Kch[(3,3)]
    Kch[(4,8)]=-Kch[(2,4)]
    Kch[(5,7)]=-Kch[(5,1)]

    #Terceiro Quadrante

    Kch[6,0]=Kch[(0,6)]
    Kch[7,1]=Kch[(1,7)]
    Kch[8,2]=Kch[(2,8)]
    Kch[9,3]=Kch[(3,9)]
    Kch[10,4]=Kch[(4,10)]
    Kch[11,5]=Kch[(5,11)]

    Kch[(7,5)]=-Kch[(1,11)]
    Kch[(8,4)]=-Kch[(2,10)]
    Kch[(9,3)]=Kch[(3,9)]
    Kch[(10,2)]=-Kch[(4,8)]
    Kch[(11,1)]=-Kch[(5,7)]

    #Quarto Quadrante

    Kch[(7,11)]=-Kch[1,5]
    Kch[(8,10)]=-Kch[2,4]
    Kch[(10,8)]=-Kch[(2,4)]
    Kch[(11,7)]=-Kch[(5,1)]

    kch3=Kch
    Iy3=Iy
    J3=J
    #Matriz de rigidez global

    K=np.dot(Tt, Kch)
    K3=np.dot(K,T)

    K3_global=np.zeros((78,78))

    K3_global[12:24,12:24]=K3[:,:]

    #
    #
    #
    #
    ####################################################

    #Lambda

    #Pontos barra 4
    x1=-100.64
    y1=389.13
    z1=0
    
    x2=0
    y2=0
    z2=0

    L=((x2-x1)**(2)+(y2-y1)**(2)+(z2-z1)**(2))**(1/2)

    l=(x2-x1)/L

    m=(y2-y1)/L

    n=(z2-z1)/L

    D=(l**2+m**2)**(1/2)
    L4=L
    
    lmbd=np.zeros((3,3))

    lmbd[0]=[l,m,n]
    lmbd[1]=[-m/D,l/D,0]
    lmbd[2]=[-l*n/D,-m*n/D,D]

    T=np.zeros((12,12))

    T[0:3,0:3]=lmbd
    T[3:6,3:6]=lmbd
    T[6:9,6:9]=lmbd
    T[9:12,9:12]=lmbd

    T4=T
    Tt=T.transpose()


    # Matriz de rigidez Local
    Di=(0.7558*Diametros[3]-1.2229)
    A=(np.pi/4)*((Diametros[3]**2)-(Di**2))
    A4=A
    E=69000
    #L=1
    Iy=(np.pi/64)*(Diametros[3]**4-Di**4)
    Iz=(np.pi/64)*(Diametros[3]**4-Di**4)
    G=25800
    J=(np.pi/32)*(Diametros[3]**4-Di**4)

    #Diagonal principal

    Kch=np.zeros((12,12))
    Kch[(0,0)]=A*E/L
    Kch[(1,1)]=12*E*Iz/L**3
    Kch[(2,2)]=12*E*Iy/L**3
    Kch[(3,3)]=G*J/L
    Kch[(4,4)]=4*E*Iy/L
    Kch[(5,5)]=4*E*Iz/L

    Kch[(6,6)]=A*E/L
    Kch[(7,7)]=12*E*Iz/L**3
    Kch[(8,8)]=12*E*Iy/L**3
    Kch[(9,9)]=G*J/L
    Kch[(10,10)]=4*E*Iy/L
    Kch[(11,11)]=4*E*Iz/L

    #Segundo quadrante
    Kch[1,5]=6*E*Iz/L**2
    Kch[2,4]=-6*E*Iy/L**2
    Kch[4,2]=-6*E*Iy/L**2
    Kch[5,1]=6*E*Iz/L**2

    #Primeiro quadrante
    Kch[(0,6)]=-Kch[(0,0)]
    Kch[(1,7)]=-Kch[(1,1)]
    Kch[(2,8)]=-Kch[(2,2)]
    Kch[(3,9)]=-Kch[(3,3)]
    Kch[(4,10)]=Kch[(4,4)]/2
    Kch[(5,11)]=Kch[(4,4)]/2

    Kch[(1,11)]=Kch[1,5]
    Kch[(2,10)]=Kch[2,4]
    Kch[(3,9)]=-Kch[(3,3)]
    Kch[(4,8)]=-Kch[(2,4)]
    Kch[(5,7)]=-Kch[(5,1)]

    #Terceiro Quadrante

    Kch[6,0]=Kch[(0,6)]
    Kch[7,1]=Kch[(1,7)]
    Kch[8,2]=Kch[(2,8)]
    Kch[9,3]=Kch[(3,9)]
    Kch[10,4]=Kch[(4,10)]
    Kch[11,5]=Kch[(5,11)]

    Kch[(7,5)]=-Kch[(1,11)]
    Kch[(8,4)]=-Kch[(2,10)]
    Kch[(9,3)]=Kch[(3,9)]
    Kch[(10,2)]=-Kch[(4,8)]
    Kch[(11,1)]=-Kch[(5,7)]

    #Quarto Quadrante

    Kch[(7,11)]=-Kch[1,5]
    Kch[(8,10)]=-Kch[2,4]
    Kch[(10,8)]=-Kch[(2,4)]
    Kch[(11,7)]=-Kch[(5,1)]

    kch4=Kch
    Iy4=Iy
    J4=J
    #Matriz de rigidez global

    K=np.dot(Tt, Kch)
    K4=np.dot(K,T)

    K4_global=np.zeros((78,78))
    K4_global[:6,:6]=K4[6:,6:]#F1
    K4_global[:6,18:24]=K4[6:,:6]#F1

    K4_global[18:24,:6]=K4[:6,6:]#F4
    K4_global[18:24,18:24]=K4[:6,:6]#F4


    #
    #
    #
    ##############################################################
    #Pontos barra 5
    x1=407.88
    y1=395.29
    z1=0
    
    x2=400.07
    y2=418.97
    z2=0

    L=((x2-x1)**(2)+(y2-y1)**(2)+(z2-z1)**(2))**(1/2)

    l=(x2-x1)/L

    m=(y2-y1)/L

    n=(z2-z1)/L

    D=(l**2+m**2)**(1/2)
    L5=L
    
    lmbd=np.zeros((3,3))

    lmbd[0]=[l,m,n]
    lmbd[1]=[-m/D,l/D,0]
    lmbd[2]=[-l*n/D,-m*n/D,D]

    T=np.zeros((12,12))

    T[0:3,0:3]=lmbd
    T[3:6,3:6]=lmbd
    T[6:9,6:9]=lmbd
    T[9:12,9:12]=lmbd

    T5=T
    Tt=T.transpose()

    # Matriz de rigidez Local
    #Diametros[4]=Diametros[1]
    Di=(0.7558*Diametros[4]-1.2229)
    A=(np.pi/4)*((Diametros[4]**2)-(Di**2))#Tirei a raiz
    A5=A
    E=69000
    #L=1
    Iy=(np.pi/64)*(Diametros[4]**4-Di**4)
    Iz=(np.pi/64)*(Diametros[4]**4-Di**4)#Di esta dando complexo
    G=25800
    J=(np.pi/32)*(Diametros[4]**4-Di**4)

    #Diagonal principal

    Kch=np.zeros((12,12))
    Kch[(0,0)]=A*E/L


    Kch[(1,1)]=12*E*Iz/L**3
    Kch[(2,2)]=12*E*Iy/L**3
    Kch[(3,3)]=G*J/L
    Kch[(4,4)]=4*E*Iy/L
    Kch[(5,5)]=4*E*Iz/L

    Kch[(6,6)]=A*E/L
    Kch[(7,7)]=12*E*Iz/L**3
    Kch[(8,8)]=12*E*Iy/L**3
    Kch[(9,9)]=G*J/L
    Kch[(10,10)]=4*E*Iy/L
    Kch[(11,11)]=4*E*Iz/L

    #Segundo quadrante
    Kch[1,5]=6*E*Iz/L**2
    Kch[2,4]=-6*E*Iy/L**2
    Kch[4,2]=-6*E*Iy/L**2
    Kch[5,1]=6*E*Iz/L**2

    #Primeiro quadrante
    Kch[(0,6)]=-Kch[(0,0)]
    Kch[(1,7)]=-Kch[(1,1)]
    Kch[(2,8)]=-Kch[(2,2)]
    Kch[(3,9)]=-Kch[(3,3)]
    Kch[(4,10)]=Kch[(4,4)]/2
    Kch[(5,11)]=Kch[(4,4)]/2

    Kch[(1,11)]=Kch[1,5]
    Kch[(2,10)]=Kch[2,4]
    Kch[(3,9)]=-Kch[(3,3)]
    Kch[(4,8)]=-Kch[(2,4)]
    Kch[(5,7)]=-Kch[(5,1)]

    #Terceiro Quadrante

    Kch[6,0]=Kch[(0,6)]
    Kch[7,1]=Kch[(1,7)]
    Kch[8,2]=Kch[(2,8)]
    Kch[9,3]=Kch[(3,9)]
    Kch[10,4]=Kch[(4,10)]
    Kch[11,5]=Kch[(5,11)]

    Kch[(7,5)]=-Kch[(1,11)]
    Kch[(8,4)]=-Kch[(2,10)]
    Kch[(9,3)]=Kch[(3,9)]
    Kch[(10,2)]=-Kch[(4,8)]
    Kch[(11,1)]=-Kch[(5,7)]

    #Quarto Quadrante

    Kch[(7,11)]=-Kch[1,5]
    Kch[(8,10)]=-Kch[2,4]
    Kch[(10,8)]=-Kch[(2,4)]
    Kch[(11,7)]=-Kch[(5,1)]

    Kch5=Kch
    Iy5=Iy
    J5=J
    #Matriz de rigidez global barra 1

    K=np.dot(Tt, Kch)
    K5=np.dot(K,T)

    K5_global=np.zeros((78,78))
    K5_global[6:12,6:12]=K5[6:,6:]#2
    K5_global[6:12,24:30]=K5[6:,:6]#2

    K5_global[24:30,24:30]=K5[:6,:6]#5
    K5_global[24:30,6:12]=K5[:6,6:]#5

    ###############################################################################################
    #Pontos barra 6
    x1=375
    y1=495.01
    z1=0
    
    x2=368.74
    y2=514
    z2=0

    L=((x2-x1)**(2)+(y2-y1)**(2)+(z2-z1)**(2))**(1/2)

    l=(x2-x1)/L

    m=(y2-y1)/L

    n=(z2-z1)/L

    D=(l**2+m**2)**(1/2)
    L6=L
    
    lmbd=np.zeros((3,3))
    lmbd[0]=[l,m,n]
    lmbd[1]=[-m/D,l/D,0]
    lmbd[2]=[-l*n/D,-m*n/D,D]

    T=np.zeros((12,12))

    T[0:3,0:3]=lmbd
    T[3:6,3:6]=lmbd
    T[6:9,6:9]=lmbd
    T[9:12,9:12]=lmbd

    T6=T
    Tt=T.transpose()

    # Matriz de rigidez Local
    #Diametros[5]=Diametros[1]
    Di=(0.7558*Diametros[5]-1.2229)
    A=(np.pi/4)*((Diametros[5]**2)-(Di**2))
    A6=A
    E=69000
    #L=1
    Iy=(np.pi/64)*(Diametros[5]**4-Di**4)
    Iz=(np.pi/64)*(Diametros[5]**4-Di**4)
    G=25800
    J=(np.pi/32)*(Diametros[5]**4-Di**4)

    #Diagonal principal

    Kch=np.zeros((12,12))
    Kch[(0,0)]=A*E/L
    Kch[(1,1)]=12*E*Iz/L**3
    Kch[(2,2)]=12*E*Iy/L**3
    Kch[(3,3)]=G*J/L
    Kch[(4,4)]=4*E*Iy/L
    Kch[(5,5)]=4*E*Iz/L

    Kch[(6,6)]=A*E/L
    Kch[(7,7)]=12*E*Iz/L**3
    Kch[(8,8)]=12*E*Iy/L**3
    Kch[(9,9)]=G*J/L
    Kch[(10,10)]=4*E*Iy/L
    Kch[(11,11)]=4*E*Iz/L

    #Segundo quadrante
    Kch[1,5]=6*E*Iz/L**2
    Kch[2,4]=-6*E*Iy/L**2
    Kch[4,2]=-6*E*Iy/L**2
    Kch[5,1]=6*E*Iz/L**2

    #Primeiro quadrante
    Kch[(0,6)]=-Kch[(0,0)]
    Kch[(1,7)]=-Kch[(1,1)]
    Kch[(2,8)]=-Kch[(2,2)]
    Kch[(3,9)]=-Kch[(3,3)]
    Kch[(4,10)]=Kch[(4,4)]/2
    Kch[(5,11)]=Kch[(4,4)]/2

    Kch[(1,11)]=Kch[1,5]
    Kch[(2,10)]=Kch[2,4]
    Kch[(3,9)]=-Kch[(3,3)]
    Kch[(4,8)]=-Kch[(2,4)]
    Kch[(5,7)]=-Kch[(5,1)]

    #Terceiro Quadrante

    Kch[6,0]=Kch[(0,6)]
    Kch[7,1]=Kch[(1,7)]
    Kch[8,2]=Kch[(2,8)]
    Kch[9,3]=Kch[(3,9)]
    Kch[10,4]=Kch[(4,10)]
    Kch[11,5]=Kch[(5,11)]

    Kch[(7,5)]=-Kch[(1,11)]
    Kch[(8,4)]=-Kch[(2,10)]
    Kch[(9,3)]=Kch[(3,9)]
    Kch[(10,2)]=-Kch[(4,8)]
    Kch[(11,1)]=-Kch[(5,7)]

    #Quarto Quadrante

    Kch[(7,11)]=-Kch[1,5]
    Kch[(8,10)]=-Kch[2,4]
    Kch[(10,8)]=-Kch[(2,4)]
    Kch[(11,7)]=-Kch[(5,1)]
    Kch6=Kch
    Iy6=Iy
    J6=J
    #Matriz de rigidez global

    K=np.dot(Tt, Kch)
    K6=np.dot(K,T)

    K6_global=np.zeros((78,78))
    K6_global[12:18,12:18]=K6[:6,:6]#3
    K6_global[12:18,30:36]=K6[:6,6:]#3

    K6_global[30:36,30:36]=K6[6:,6:]#6
    K6_global[30:36,12:18]=K6[6:,:6]#6

    ####################################################

    #Lambda

    #Pontos barra 7
    x1=-100.64
    y1=389.13
    z1=0
    
    x2=-107.91
    y2=417.27
    z2=0

    L=((x2-x1)**(2)+(y2-y1)**(2)+(z2-z1)**(2))**(1/2)

    l=(x2-x1)/L

    m=(y2-y1)/L

    n=(z2-z1)/L

    D=(l**2+m**2)**(1/2)
    L7=L
    
    lmbd=np.zeros((3,3))

    lmbd[0]=[l,m,n]
    lmbd[1]=[-m/D,l/D,0]
    lmbd[2]=[-l*n/D,-m*n/D,D]

    T=np.zeros((12,12))

    T[0:3,0:3]=lmbd
    T[3:6,3:6]=lmbd
    T[6:9,6:9]=lmbd
    T[9:12,9:12]=lmbd

    T7=T
    Tt=T.transpose()


    # Matriz de rigidez Local
    #Diametros[6]=Diametros[3]
    Di=(0.7558*Diametros[6]-1.2229)

    A=(np.pi/4)*((Diametros[6]**2)-(Di**2))
    A7=A
    E=69000
    #L=1
    Iy=(np.pi/64)*(Diametros[6]**4-Di**4)
    Iz=(np.pi/64)*(Diametros[6]**4-Di**4)
    G=25800
    J=(np.pi/32)*(Diametros[6]**4-Di**4)

    #Diagonal principal

    Kch=np.zeros((12,12))
    Kch[(0,0)]=A*E/L
    Kch[(1,1)]=12*E*Iz/L**3
    Kch[(2,2)]=12*E*Iy/L**3
    Kch[(3,3)]=G*J/L
    Kch[(4,4)]=4*E*Iy/L
    Kch[(5,5)]=4*E*Iz/L

    Kch[(6,6)]=A*E/L
    Kch[(7,7)]=12*E*Iz/L**3
    Kch[(8,8)]=12*E*Iy/L**3
    Kch[(9,9)]=G*J/L
    Kch[(10,10)]=4*E*Iy/L
    Kch[(11,11)]=4*E*Iz/L

    #Segundo quadrante
    Kch[1,5]=6*E*Iz/L**2
    Kch[2,4]=-6*E*Iy/L**2
    Kch[4,2]=-6*E*Iy/L**2
    Kch[5,1]=6*E*Iz/L**2

    #Primeiro quadrante
    Kch[(0,6)]=-Kch[(0,0)]
    Kch[(1,7)]=-Kch[(1,1)]
    Kch[(2,8)]=-Kch[(2,2)]
    Kch[(3,9)]=-Kch[(3,3)]
    Kch[(4,10)]=Kch[(4,4)]/2
    Kch[(5,11)]=Kch[(4,4)]/2

    Kch[(1,11)]=Kch[1,5]
    Kch[(2,10)]=Kch[2,4]
    Kch[(3,9)]=-Kch[(3,3)]
    Kch[(4,8)]=-Kch[(2,4)]
    Kch[(5,7)]=-Kch[(5,1)]

    #Terceiro Quadrante

    Kch[6,0]=Kch[(0,6)]
    Kch[7,1]=Kch[(1,7)]
    Kch[8,2]=Kch[(2,8)]
    Kch[9,3]=Kch[(3,9)]
    Kch[10,4]=Kch[(4,10)]
    Kch[11,5]=Kch[(5,11)]

    Kch[(7,5)]=-Kch[(1,11)]
    Kch[(8,4)]=-Kch[(2,10)]
    Kch[(9,3)]=Kch[(3,9)]
    Kch[(10,2)]=-Kch[(4,8)]
    Kch[(11,1)]=-Kch[(5,7)]

    #Quarto Quadrante

    Kch[(7,11)]=-Kch[1,5]
    Kch[(8,10)]=-Kch[2,4]
    Kch[(10,8)]=-Kch[(2,4)]
    Kch[(11,7)]=-Kch[(5,1)]

    Kch7=Kch
    Iy7=Iy
    J7=J
    #Matriz de rigidez global

    K=np.dot(Tt, Kch)
    K7=np.dot(K,T)

    K7_global=np.zeros((78,78))
    K7_global[18:24,18:24]=K7[:6,:6]#4
    K7_global[18:24,36:42]=K7[:6,6:]#4

    K7_global[36:42,36:42]=K7[6:,6:]#7
    K7_global[36:42,18:24]=K7[6:,:6]#7

    ####################################################
    #Pontos barra 8
    x1=0
    y1=0
    z1=45
    
    x2=0
    y2=0
    z2=25

    L=((x2-x1)**(2)+(y2-y1)**(2)+(z2-z1)**(2))**(1/2)

    l=(x2-x1)/L

    m=(y2-y1)/L

    n=(z2-z1)/L

    D=(l**2+m**2)**(1/2)
    L8=L
    
    lmbd=np.zeros((3,3))

    lmbd=np.zeros((3,3))
    lmbd[0,2]=-1
    lmbd[1,1]=1
    lmbd[2,0]=1


    T=np.zeros((12,12))

    T[0:3,0:3]=lmbd
    T[3:6,3:6]=lmbd
    T[6:9,6:9]=lmbd
    T[9:12,9:12]=lmbd

    T8=T
    Tt=T.transpose()

    # Matriz de rigidez Local
    Di=(0.7558*Diametros[7]-1.2229)
    
    A=(np.pi/4)*((Diametros[7]**2)-(Di**2))#Tirei a raiz
    A8=A
    E=69000
    #L=1
    Iy=(np.pi/64)*(Diametros[7]**4-Di**4)
    Iz=(np.pi/64)*(Diametros[7]**4-Di**4)#Di esta dando complexo
    G=25800
    J=(np.pi/32)*(Diametros[7]**4-Di**4)

    #Diagonal principal

    Kch=np.zeros((12,12))
    Kch[(0,0)]=A*E/L


    Kch[(1,1)]=12*E*Iz/L**3
    Kch[(2,2)]=12*E*Iy/L**3
    Kch[(3,3)]=G*J/L
    Kch[(4,4)]=4*E*Iy/L
    Kch[(5,5)]=4*E*Iz/L

    Kch[(6,6)]=A*E/L
    Kch[(7,7)]=12*E*Iz/L**3
    Kch[(8,8)]=12*E*Iy/L**3
    Kch[(9,9)]=G*J/L
    Kch[(10,10)]=4*E*Iy/L
    Kch[(11,11)]=4*E*Iz/L

    #Segundo quadrante
    Kch[1,5]=6*E*Iz/L**2
    Kch[2,4]=-6*E*Iy/L**2
    Kch[4,2]=-6*E*Iy/L**2
    Kch[5,1]=6*E*Iz/L**2

    #Primeiro quadrante
    Kch[(0,6)]=-Kch[(0,0)]
    Kch[(1,7)]=-Kch[(1,1)]
    Kch[(2,8)]=-Kch[(2,2)]
    Kch[(3,9)]=-Kch[(3,3)]
    Kch[(4,10)]=Kch[(4,4)]/2
    Kch[(5,11)]=Kch[(4,4)]/2

    Kch[(1,11)]=Kch[1,5]
    Kch[(2,10)]=Kch[2,4]
    Kch[(3,9)]=-Kch[(3,3)]
    Kch[(4,8)]=-Kch[(2,4)]
    Kch[(5,7)]=-Kch[(5,1)]

    #Terceiro Quadrante

    Kch[6,0]=Kch[(0,6)]
    Kch[7,1]=Kch[(1,7)]
    Kch[8,2]=Kch[(2,8)]
    Kch[9,3]=Kch[(3,9)]
    Kch[10,4]=Kch[(4,10)]
    Kch[11,5]=Kch[(5,11)]

    Kch[(7,5)]=-Kch[(1,11)]
    Kch[(8,4)]=-Kch[(2,10)]
    Kch[(9,3)]=Kch[(3,9)]
    Kch[(10,2)]=-Kch[(4,8)]
    Kch[(11,1)]=-Kch[(5,7)]

    #Quarto Quadrante

    Kch[(7,11)]=-Kch[1,5]
    Kch[(8,10)]=-Kch[2,4]
    Kch[(10,8)]=-Kch[(2,4)]
    Kch[(11,7)]=-Kch[(5,1)]

    Kch8=Kch
    Iy8=Iy
    J8=J
    #Matriz de rigidez global barra 1

    K=np.dot(Tt, Kch)
    K8=np.dot(K,T)

    K8_global=np.zeros((78,78))
    K8_global[42:48,42:48]=K8[:6,:6]#8
    K8_global[42:48,48:54]=K8[:6,6:]#8

    K8_global[48:54,48:54]=K8[6:,6:]#9
    K8_global[48:54,42:48]=K8[6:,:6]#9

    ###############################################################################################
    #Pontos barra 9
    x1=0
    y1=0
    z1=25
    
    x2=0
    y2=0
    z2=0

    L=((x2-x1)**(2)+(y2-y1)**(2)+(z2-z1)**(2))**(1/2)

    l=(x2-x1)/L

    m=(y2-y1)/L

    n=(z2-z1)/L

    D=(l**2+m**2)**(1/2)
    L9=L
    
    lmbd=np.zeros((3,3))
    lmbd[0,2]=-1
    lmbd[1,1]=1
    lmbd[2,0]=1

    T=np.zeros((12,12))

    T[0:3,0:3]=lmbd
    T[3:6,3:6]=lmbd
    T[6:9,6:9]=lmbd
    T[9:12,9:12]=lmbd

    T9=T
    Tt=T.transpose()

    # Matriz de rigidez Local
    #Diametros[8]=Diametros[7]
    Di=(0.7558*Diametros[8]-1.2229)

    A=(np.pi/4)*((Diametros[8]**2)-(Di**2))
    A9=A
    E=69000
    #L=1
    Iy=(np.pi/64)*(Diametros[8]**4-Di**4)
    Iz=(np.pi/64)*(Diametros[8]**4-Di**4)
    G=25800
    J=(np.pi/32)*(Diametros[8]**4-Di**4)

    #Diagonal principal

    Kch=np.zeros((12,12))
    Kch[(0,0)]=A*E/L
    Kch[(1,1)]=12*E*Iz/L**3
    Kch[(2,2)]=12*E*Iy/L**3
    Kch[(3,3)]=G*J/L
    Kch[(4,4)]=4*E*Iy/L
    Kch[(5,5)]=4*E*Iz/L

    Kch[(6,6)]=A*E/L
    Kch[(7,7)]=12*E*Iz/L**3
    Kch[(8,8)]=12*E*Iy/L**3
    Kch[(9,9)]=G*J/L
    Kch[(10,10)]=4*E*Iy/L
    Kch[(11,11)]=4*E*Iz/L

    #Segundo quadrante
    Kch[1,5]=6*E*Iz/L**2
    Kch[2,4]=-6*E*Iy/L**2
    Kch[4,2]=-6*E*Iy/L**2
    Kch[5,1]=6*E*Iz/L**2

    #Primeiro quadrante
    Kch[(0,6)]=-Kch[(0,0)]
    Kch[(1,7)]=-Kch[(1,1)]
    Kch[(2,8)]=-Kch[(2,2)]
    Kch[(3,9)]=-Kch[(3,3)]
    Kch[(4,10)]=Kch[(4,4)]/2
    Kch[(5,11)]=Kch[(4,4)]/2

    Kch[(1,11)]=Kch[1,5]
    Kch[(2,10)]=Kch[2,4]
    Kch[(3,9)]=-Kch[(3,3)]
    Kch[(4,8)]=-Kch[(2,4)]
    Kch[(5,7)]=-Kch[(5,1)]

    #Terceiro Quadrante

    Kch[6,0]=Kch[(0,6)]
    Kch[7,1]=Kch[(1,7)]
    Kch[8,2]=Kch[(2,8)]
    Kch[9,3]=Kch[(3,9)]
    Kch[10,4]=Kch[(4,10)]
    Kch[11,5]=Kch[(5,11)]

    Kch[(7,5)]=-Kch[(1,11)]
    Kch[(8,4)]=-Kch[(2,10)]
    Kch[(9,3)]=Kch[(3,9)]
    Kch[(10,2)]=-Kch[(4,8)]
    Kch[(11,1)]=-Kch[(5,7)]

    #Quarto Quadrante

    Kch[(7,11)]=-Kch[1,5]
    Kch[(8,10)]=-Kch[2,4]
    Kch[(10,8)]=-Kch[(2,4)]
    Kch[(11,7)]=-Kch[(5,1)]
    Kch9=Kch
    Iy9=Iy
    J9=J
    #Matriz de rigidez global

    K=np.dot(Tt, Kch)
    K9=np.dot(K,T)

    K9_global=np.zeros((78,78))
    K9_global[48:54,48:54]=K9[:6,:6]#
    K9_global[48:54,:6]=   K9[:6,6:]#

    K9_global[:6,:6]=      K9[6:,6:]#
    K9_global[:6,48:54]=   K9[6:,:6]#


    ####################################################

    #Lambda

    #Pontos barra 10

    x1=0
    y1=0
    z1=0
    
    x2=0
    y2=0
    z2=-25


    L=((x2-x1)**(2)+(y2-y1)**(2)+(z2-z1)**(2))**(1/2)

    l=(x2-x1)/L

    m=(y2-y1)/L

    n=(z2-z1)/L

    D=(l**2+m**2)**(1/2)
    L10=L
    
    lmbd=np.zeros((3,3))

    lmbd=np.zeros((3,3))
    lmbd[0,2]=-1
    lmbd[1,1]=1
    lmbd[2,0]=1

    T=np.zeros((12,12))

    T[0:3,0:3]=lmbd
    T[3:6,3:6]=lmbd
    T[6:9,6:9]=lmbd
    T[9:12,9:12]=lmbd

    T10=T
    Tt=T.transpose()


    # Matriz de rigidez Local
    #Diametros[9]=Diametros[7]
    Di=(0.7558*Diametros[9]-1.2229)

    A=(np.pi/4)*((Diametros[9]**2)-(Di**2))
    A10=A
    E=69000
    #L=1
    Iy=(np.pi/64)*(Diametros[9]**4-Di**4)
    Iz=(np.pi/64)*(Diametros[9]**4-Di**4)
    G=25800
    J=(np.pi/32)*(Diametros[9]**4-Di**4)

    #Diagonal principal

    Kch=np.zeros((12,12))
    Kch[(0,0)]=A*E/L
    Kch[(1,1)]=12*E*Iz/L**3
    Kch[(2,2)]=12*E*Iy/L**3
    Kch[(3,3)]=G*J/L
    Kch[(4,4)]=4*E*Iy/L
    Kch[(5,5)]=4*E*Iz/L

    Kch[(6,6)]=A*E/L
    Kch[(7,7)]=12*E*Iz/L**3
    Kch[(8,8)]=12*E*Iy/L**3
    Kch[(9,9)]=G*J/L
    Kch[(10,10)]=4*E*Iy/L
    Kch[(11,11)]=4*E*Iz/L

    #Segundo quadrante
    Kch[1,5]=6*E*Iz/L**2
    Kch[2,4]=-6*E*Iy/L**2
    Kch[4,2]=-6*E*Iy/L**2
    Kch[5,1]=6*E*Iz/L**2

    #Primeiro quadrante
    Kch[(0,6)]=-Kch[(0,0)]
    Kch[(1,7)]=-Kch[(1,1)]
    Kch[(2,8)]=-Kch[(2,2)]
    Kch[(3,9)]=-Kch[(3,3)]
    Kch[(4,10)]=Kch[(4,4)]/2
    Kch[(5,11)]=Kch[(4,4)]/2

    Kch[(1,11)]=Kch[1,5]
    Kch[(2,10)]=Kch[2,4]
    Kch[(3,9)]=-Kch[(3,3)]
    Kch[(4,8)]=-Kch[(2,4)]
    Kch[(5,7)]=-Kch[(5,1)]

    #Terceiro Quadrante

    Kch[6,0]=Kch[(0,6)]
    Kch[7,1]=Kch[(1,7)]
    Kch[8,2]=Kch[(2,8)]
    Kch[9,3]=Kch[(3,9)]
    Kch[10,4]=Kch[(4,10)]
    Kch[11,5]=Kch[(5,11)]

    Kch[(7,5)]=-Kch[(1,11)]
    Kch[(8,4)]=-Kch[(2,10)]
    Kch[(9,3)]=Kch[(3,9)]
    Kch[(10,2)]=-Kch[(4,8)]
    Kch[(11,1)]=-Kch[(5,7)]

    #Quarto Quadrante

    Kch[(7,11)]=-Kch[1,5]
    Kch[(8,10)]=-Kch[2,4]
    Kch[(10,8)]=-Kch[(2,4)]
    Kch[(11,7)]=-Kch[(5,1)]

    Kch10=Kch
    Iy10=Iy
    J10=J
    #Matriz de rigidez global

    K=np.dot(Tt, Kch)
    K10=np.dot(K,T)

    K10_global=np.zeros((78,78))
    K10_global[:6,:6]=   K10[:6,:6]#1
    K10_global[:6,54:60]=K10[:6,6:]#1

    K10_global[54:60,54:60]=K10[6:,6:]#10
    K10_global[54:60,:6]=   K10[6:,:6]#10

    ############################################################
    #Lambda

    #Pontos barra 11
    x1=0
    y1=0    
    z1=-25
    
    x2=0
    y2=0
    z2=-45

    L=((x2-x1)**(2)+(y2-y1)**(2)+(z2-z1)**(2))**(1/2)

    l=(x2-x1)/L

    m=(y2-y1)/L

    n=(z2-z1)/L

    D=(l**2+m**2)**(1/2)
    L11=L
    
    lmbd=np.zeros((3,3))

    lmbd=np.zeros((3,3))
    lmbd[0,2]=-1
    lmbd[1,1]=1
    lmbd[2,0]=1

    T=np.zeros((12,12))

    T[0:3,0:3]=lmbd
    T[3:6,3:6]=lmbd
    T[6:9,6:9]=lmbd
    T[9:12,9:12]=lmbd

    T11=T
    Tt=T.transpose()


    # Matriz de rigidez Local
    #Diametros[10]=Diametros[7]
    Di=(0.7558*Diametros[10]-1.2229)

    A=(np.pi/4)*((Diametros[10]**2)-(Di**2))
    A11=A
    E=69000
    #L=1
    Iy=(np.pi/64)*(Diametros[10]**4-Di**4)
    Iz=(np.pi/64)*(Diametros[10]**4-Di**4)
    G=25800
    J=(np.pi/32)*(Diametros[10]**4-Di**4)

    #Diagonal principal

    Kch=np.zeros((12,12))
    Kch[(0,0)]=A*E/L
    Kch[(1,1)]=12*E*Iz/L**3
    Kch[(2,2)]=12*E*Iy/L**3
    Kch[(3,3)]=G*J/L
    Kch[(4,4)]=4*E*Iy/L
    Kch[(5,5)]=4*E*Iz/L

    Kch[(6,6)]=A*E/L
    Kch[(7,7)]=12*E*Iz/L**3
    Kch[(8,8)]=12*E*Iy/L**3
    Kch[(9,9)]=G*J/L
    Kch[(10,10)]=4*E*Iy/L
    Kch[(11,11)]=4*E*Iz/L

    #Segundo quadrante
    Kch[1,5]=6*E*Iz/L**2
    Kch[2,4]=-6*E*Iy/L**2
    Kch[4,2]=-6*E*Iy/L**2
    Kch[5,1]=6*E*Iz/L**2

    #Primeiro quadrante
    Kch[(0,6)]=-Kch[(0,0)]
    Kch[(1,7)]=-Kch[(1,1)]
    Kch[(2,8)]=-Kch[(2,2)]
    Kch[(3,9)]=-Kch[(3,3)]
    Kch[(4,10)]=Kch[(4,4)]/2
    Kch[(5,11)]=Kch[(4,4)]/2

    Kch[(1,11)]=Kch[1,5]
    Kch[(2,10)]=Kch[2,4]
    Kch[(3,9)]=-Kch[(3,3)]
    Kch[(4,8)]=-Kch[(2,4)]
    Kch[(5,7)]=-Kch[(5,1)]

    #Terceiro Quadrante

    Kch[6,0]=Kch[(0,6)]
    Kch[7,1]=Kch[(1,7)]
    Kch[8,2]=Kch[(2,8)]
    Kch[9,3]=Kch[(3,9)]
    Kch[10,4]=Kch[(4,10)]
    Kch[11,5]=Kch[(5,11)]

    Kch[(7,5)]=-Kch[(1,11)]
    Kch[(8,4)]=-Kch[(2,10)]
    Kch[(9,3)]=Kch[(3,9)]
    Kch[(10,2)]=-Kch[(4,8)]
    Kch[(11,1)]=-Kch[(5,7)]

    #Quarto Quadrante

    Kch[(7,11)]=-Kch[1,5]
    Kch[(8,10)]=-Kch[2,4]
    Kch[(10,8)]=-Kch[(2,4)]
    Kch[(11,7)]=-Kch[(5,1)]

    Kch11=Kch
    Iy11=Iy
    J11=J
    #Matriz de rigidez global

    K=np.dot(Tt, Kch)
    K11=np.dot(K,T)

    K11_global=np.zeros((78,78))
    K11_global[54:60,54:60]=K11[:6,:6]#10
    K11_global[54:60,60:66]=K11[:6,6:]#10

    K11_global[60:66,60:66]=K11[6:,6:]#11
    K11_global[60:66,54:60]=K11[6:,:6]#11

    ####################################################
    #Pontos barra 12
    x1=-100.64
    y1=389.13   
    z1=0
    
    x2=-406.66
    y2=30.33
    z2=67.5

    L=((x2-x1)**(2)+(y2-y1)**(2)+(z2-z1)**(2))**(1/2)

    l=(x2-x1)/L

    m=(y2-y1)/L

    n=(z2-z1)/L

    D=(l**2+m**2)**(1/2)
    L12=L
    
    lmbd=np.zeros((3,3))
    lmbd[0]=[l,m,n]
    lmbd[1]=[-m/D,l/D,0]
    lmbd[2]=[-l*n/D,-m*n/D,D]

    T=np.zeros((12,12))

    T[0:3,0:3]=lmbd
    T[3:6,3:6]=lmbd
    T[6:9,6:9]=lmbd
    T[9:12,9:12]=lmbd

    T12=T
    Tt=T.transpose()

    # Matriz de rigidez Local
    Di=(0.7558*Diametros[11]-1.2229)

    A=(np.pi/4)*((Diametros[11]**2)-(Di**2))
    A12=A
    E=69000
    #L=1
    Iy=(np.pi/64)*(Diametros[11]**4-Di**4)
    Iz=(np.pi/64)*(Diametros[11]**4-Di**4)
    G=25800
    J=(np.pi/32)*(Diametros[11]**4-Di**4)

    #Diagonal principal

    Kch=np.zeros((12,12))
    Kch[(0,0)]=A*E/L
    Kch[(1,1)]=12*E*Iz/L**3
    Kch[(2,2)]=12*E*Iy/L**3
    Kch[(3,3)]=G*J/L
    Kch[(4,4)]=4*E*Iy/L
    Kch[(5,5)]=4*E*Iz/L

    Kch[(6,6)]=A*E/L
    Kch[(7,7)]=12*E*Iz/L**3
    Kch[(8,8)]=12*E*Iy/L**3
    Kch[(9,9)]=G*J/L
    Kch[(10,10)]=4*E*Iy/L
    Kch[(11,11)]=4*E*Iz/L

    #Segundo quadrante
    Kch[1,5]=6*E*Iz/L**2
    Kch[2,4]=-6*E*Iy/L**2
    Kch[4,2]=-6*E*Iy/L**2
    Kch[5,1]=6*E*Iz/L**2

    #Primeiro quadrante
    Kch[(0,6)]=-Kch[(0,0)]
    Kch[(1,7)]=-Kch[(1,1)]
    Kch[(2,8)]=-Kch[(2,2)]
    Kch[(3,9)]=-Kch[(3,3)]
    Kch[(4,10)]=Kch[(4,4)]/2
    Kch[(5,11)]=Kch[(4,4)]/2

    Kch[(1,11)]=Kch[1,5]
    Kch[(2,10)]=Kch[2,4]
    Kch[(3,9)]=-Kch[(3,3)]
    Kch[(4,8)]=-Kch[(2,4)]
    Kch[(5,7)]=-Kch[(5,1)]

    #Terceiro Quadrante

    Kch[6,0]=Kch[(0,6)]
    Kch[7,1]=Kch[(1,7)]
    Kch[8,2]=Kch[(2,8)]
    Kch[9,3]=Kch[(3,9)]
    Kch[10,4]=Kch[(4,10)]
    Kch[11,5]=Kch[(5,11)]

    Kch[(7,5)]=-Kch[(1,11)]
    Kch[(8,4)]=-Kch[(2,10)]
    Kch[(9,3)]=Kch[(3,9)]
    Kch[(10,2)]=-Kch[(4,8)]
    Kch[(11,1)]=-Kch[(5,7)]

    #Quarto Quadrante

    Kch[(7,11)]=-Kch[1,5]
    Kch[(8,10)]=-Kch[2,4]
    Kch[(10,8)]=-Kch[(2,4)]
    Kch[(11,7)]=-Kch[(5,1)]
    Kch12=Kch
    Iy12=Iy
    J12=J
    #Matriz de rigidez global

    K=np.dot(Tt, Kch)
    K12=np.dot(K,T)

    K12_global=np.zeros((78,78))
    K12_global[18:24,18:24]=K12[:6,:6]#14
    K12_global[18:24,72:78]=K12[:6,6:]#14

    K12_global[72:78,72:78]=K12[6:,6:]#13
    K12_global[72:78,18:24]=K12[6:,:6]#13

    ############################################
    #Pontos barra 13
    x1=-100.64
    y1=389.13   
    z1=0
    
    x2=-406.66
    y2=30.33
    z2=-67.5

    L=((x2-x1)**(2)+(y2-y1)**(2)+(z2-z1)**(2))**(1/2)

    l=(x2-x1)/L

    m=(y2-y1)/L

    n=(z2-z1)/L

    D=(l**2+m**2)**(1/2)
    L13=L
    
    lmbd=np.zeros((3,3))

    lmbd[0]=[l,m,n]
    lmbd[1]=[-m/D,l/D,0]
    lmbd[2]=[-l*n/D,-m*n/D,D]

    T=np.zeros((12,12))

    T[0:3,0:3]=lmbd
    T[3:6,3:6]=lmbd
    T[6:9,6:9]=lmbd
    T[9:12,9:12]=lmbd

    T13=T
    Tt=T.transpose()

    # Matriz de rigidez Local
    #Diametros[12]=Diametros[11]
    Di=(0.7558*Diametros[12]-1.2229)
    
    A=(np.pi/4)*((Diametros[12]**2)-(Di**2))#Tirei a raiz
    A13=A
    E=69000
    #L=1
    Iy=(np.pi/64)*(Diametros[12]**4-Di**4)
    Iz=(np.pi/64)*(Diametros[12]**4-Di**4)#Di esta dando complexo
    G=25800
    J=(np.pi/32)*(Diametros[12]**4-Di**4)

    #Diagonal principal

    Kch=np.zeros((12,12))
    Kch[(0,0)]=A*E/L


    Kch[(1,1)]=12*E*Iz/L**3
    Kch[(2,2)]=12*E*Iy/L**3
    Kch[(3,3)]=G*J/L
    Kch[(4,4)]=4*E*Iy/L
    Kch[(5,5)]=4*E*Iz/L

    Kch[(6,6)]=A*E/L
    Kch[(7,7)]=12*E*Iz/L**3
    Kch[(8,8)]=12*E*Iy/L**3
    Kch[(9,9)]=G*J/L
    Kch[(10,10)]=4*E*Iy/L
    Kch[(11,11)]=4*E*Iz/L

    #Segundo quadrante
    Kch[1,5]=6*E*Iz/L**2
    Kch[2,4]=-6*E*Iy/L**2
    Kch[4,2]=-6*E*Iy/L**2
    Kch[5,1]=6*E*Iz/L**2

    #Primeiro quadrante
    Kch[(0,6)]=-Kch[(0,0)]
    Kch[(1,7)]=-Kch[(1,1)]
    Kch[(2,8)]=-Kch[(2,2)]
    Kch[(3,9)]=-Kch[(3,3)]
    Kch[(4,10)]=Kch[(4,4)]/2
    Kch[(5,11)]=Kch[(4,4)]/2

    Kch[(1,11)]=Kch[1,5]
    Kch[(2,10)]=Kch[2,4]
    Kch[(3,9)]=-Kch[(3,3)]
    Kch[(4,8)]=-Kch[(2,4)]
    Kch[(5,7)]=-Kch[(5,1)]

    #Terceiro Quadrante

    Kch[6,0]=Kch[(0,6)]
    Kch[7,1]=Kch[(1,7)]
    Kch[8,2]=Kch[(2,8)]
    Kch[9,3]=Kch[(3,9)]
    Kch[10,4]=Kch[(4,10)]
    Kch[11,5]=Kch[(5,11)]

    Kch[(7,5)]=-Kch[(1,11)]
    Kch[(8,4)]=-Kch[(2,10)]
    Kch[(9,3)]=Kch[(3,9)]
    Kch[(10,2)]=-Kch[(4,8)]
    Kch[(11,1)]=-Kch[(5,7)]

    #Quarto Quadrante

    Kch[(7,11)]=-Kch[1,5]
    Kch[(8,10)]=-Kch[2,4]
    Kch[(10,8)]=-Kch[(2,4)]
    Kch[(11,7)]=-Kch[(5,1)]

    Kch13=Kch
    Iy13=Iy
    J13=J
    #Matriz de rigidez global barra 1

    K=np.dot(Tt, Kch)
    K13=np.dot(K,T)

    K13_global=np.zeros((78,78))
    K13_global[18:24,18:24]=K13[:6,:6]
    K13_global[18:24,66:72]=K13[:6,6:]

    K13_global[66:72,66:72]=K13[6:,6:]
    K13_global[66:72,18:24]=K13[6:,:6]


    ###############################################################################################

    #Lambda

    #Pontos barra 14
    x1=0
    y1=0   
    z1=25
    
    x2=-406.66
    y2=30.33
    z2=67.5

    L=((x2-x1)**(2)+(y2-y1)**(2)+(z2-z1)**(2))**(1/2)

    l=(x2-x1)/L

    m=(y2-y1)/L

    n=(z2-z1)/L

    D=(l**2+m**2)**(1/2)
    L14=L
    
    lmbd=np.zeros((3,3))

    lmbd[0]=[l,m,n]
    lmbd[1]=[-m/D,l/D,0]
    lmbd[2]=[-l*n/D,-m*n/D,D]

    T=np.zeros((12,12))

    T[0:3,0:3]=lmbd
    T[3:6,3:6]=lmbd
    T[6:9,6:9]=lmbd
    T[9:12,9:12]=lmbd

    T14=T
    Tt=T.transpose()


    # Matriz de rigidez Local

    Di=(0.7558*Diametros[13]-1.2229)

    A=(np.pi/4)*((Diametros[13]**2)-(Di**2))
    A14=A
    E=69000
    #L=1
    Iy=(np.pi/64)*(Diametros[13]**4-Di**4)
    Iz=(np.pi/64)*(Diametros[13]**4-Di**4)
    G=25800
    J=(np.pi/32)*(Diametros[13]**4-Di**4)

    #Diagonal principal

    Kch=np.zeros((12,12))
    Kch[(0,0)]=A*E/L
    Kch[(1,1)]=12*E*Iz/L**3
    Kch[(2,2)]=12*E*Iy/L**3
    Kch[(3,3)]=G*J/L
    Kch[(4,4)]=4*E*Iy/L
    Kch[(5,5)]=4*E*Iz/L

    Kch[(6,6)]=A*E/L
    Kch[(7,7)]=12*E*Iz/L**3
    Kch[(8,8)]=12*E*Iy/L**3
    Kch[(9,9)]=G*J/L
    Kch[(10,10)]=4*E*Iy/L
    Kch[(11,11)]=4*E*Iz/L

    #Segundo quadrante
    Kch[1,5]=6*E*Iz/L**2
    Kch[2,4]=-6*E*Iy/L**2
    Kch[4,2]=-6*E*Iy/L**2
    Kch[5,1]=6*E*Iz/L**2

    #Primeiro quadrante
    Kch[(0,6)]=-Kch[(0,0)]
    Kch[(1,7)]=-Kch[(1,1)]
    Kch[(2,8)]=-Kch[(2,2)]
    Kch[(3,9)]=-Kch[(3,3)]
    Kch[(4,10)]=Kch[(4,4)]/2
    Kch[(5,11)]=Kch[(4,4)]/2

    Kch[(1,11)]=Kch[1,5]
    Kch[(2,10)]=Kch[2,4]
    Kch[(3,9)]=-Kch[(3,3)]
    Kch[(4,8)]=-Kch[(2,4)]
    Kch[(5,7)]=-Kch[(5,1)]

    #Terceiro Quadrante

    Kch[6,0]=Kch[(0,6)]
    Kch[7,1]=Kch[(1,7)]
    Kch[8,2]=Kch[(2,8)]
    Kch[9,3]=Kch[(3,9)]
    Kch[10,4]=Kch[(4,10)]
    Kch[11,5]=Kch[(5,11)]

    Kch[(7,5)]=-Kch[(1,11)]
    Kch[(8,4)]=-Kch[(2,10)]
    Kch[(9,3)]=Kch[(3,9)]
    Kch[(10,2)]=-Kch[(4,8)]
    Kch[(11,1)]=-Kch[(5,7)]

    #Quarto Quadrante

    Kch[(7,11)]=-Kch[1,5]
    Kch[(8,10)]=-Kch[2,4]
    Kch[(10,8)]=-Kch[(2,4)]
    Kch[(11,7)]=-Kch[(5,1)]

    Kch14=Kch
    Iy14=Iy
    J14=J
    #Matriz de rigidez global

    K=np.dot(Tt, Kch)
    K14=np.dot(K,T)

    K14_global=np.zeros((78,78))
    K14_global[42:48, 42:48]=K14[:6,:6]
    K14_global[42:48,72:78]=K14[:6,6:]

    K14_global[72:78, 72:78]=K14[6:,6:]
    K14_global[72:78, 42:48]=K14[6:,:6]

    ####################################################

    #Lambda

    #Pontos barra 15
    x1=0
    y1=0
    z1=-25
    
    x2=-406.66
    y2=30.33
    z2=-67.5

    L=((x2-x1)**(2)+(y2-y1)**(2)+(z2-z1)**(2))**(1/2)

    l=(x2-x1)/L

    m=(y2-y1)/L

    n=(z2-z1)/L

    D=(l**2+m**2)**(1/2)
    L15=L
    
    lmbd=np.zeros((3,3))

    lmbd[0]=[l,m,n]
    lmbd[1]=[-m/D,l/D,0]
    lmbd[2]=[-l*n/D,-m*n/D,D]

    T=np.zeros((12,12))

    T[0:3,0:3]=lmbd
    T[3:6,3:6]=lmbd
    T[6:9,6:9]=lmbd
    T[9:12,9:12]=lmbd

    T15=T
    Tt=T.transpose()


    # Matriz de rigidez Local
    #Diametros[14]=Diametros[13]
    Di=(0.7558*Diametros[14]-1.2229)

    A=(np.pi/4)*((Diametros[14]**2)-(Di**2))
    A15=A
    E=69000
    #L=1
    Iy=(np.pi/64)*(Diametros[14]**4-Di**4)
    Iz=(np.pi/64)*(Diametros[14]**4-Di**4)
    G=25800
    J=(np.pi/32)*(Diametros[14]**4-Di**4)

    #Diagonal principal

    Kch=np.zeros((12,12))
    Kch[(0,0)]=A*E/L
    Kch[(1,1)]=12*E*Iz/L**3
    Kch[(2,2)]=12*E*Iy/L**3
    Kch[(3,3)]=G*J/L
    Kch[(4,4)]=4*E*Iy/L
    Kch[(5,5)]=4*E*Iz/L

    Kch[(6,6)]=A*E/L
    Kch[(7,7)]=12*E*Iz/L**3
    Kch[(8,8)]=12*E*Iy/L**3
    Kch[(9,9)]=G*J/L
    Kch[(10,10)]=4*E*Iy/L
    Kch[(11,11)]=4*E*Iz/L

    #Segundo quadrante
    Kch[1,5]=6*E*Iz/L**2
    Kch[2,4]=-6*E*Iy/L**2
    Kch[4,2]=-6*E*Iy/L**2
    Kch[5,1]=6*E*Iz/L**2

    #Primeiro quadrante
    Kch[(0,6)]=-Kch[(0,0)]
    Kch[(1,7)]=-Kch[(1,1)]
    Kch[(2,8)]=-Kch[(2,2)]
    Kch[(3,9)]=-Kch[(3,3)]
    Kch[(4,10)]=Kch[(4,4)]/2
    Kch[(5,11)]=Kch[(4,4)]/2

    Kch[(1,11)]=Kch[1,5]
    Kch[(2,10)]=Kch[2,4]
    Kch[(3,9)]=-Kch[(3,3)]
    Kch[(4,8)]=-Kch[(2,4)]
    Kch[(5,7)]=-Kch[(5,1)]

    #Terceiro Quadrante

    Kch[6,0]=Kch[(0,6)]
    Kch[7,1]=Kch[(1,7)]
    Kch[8,2]=Kch[(2,8)]
    Kch[9,3]=Kch[(3,9)]
    Kch[10,4]=Kch[(4,10)]
    Kch[11,5]=Kch[(5,11)]

    Kch[(7,5)]=-Kch[(1,11)]
    Kch[(8,4)]=-Kch[(2,10)]
    Kch[(9,3)]=Kch[(3,9)]
    Kch[(10,2)]=-Kch[(4,8)]
    Kch[(11,1)]=-Kch[(5,7)]

    #Quarto Quadrante

    Kch[(7,11)]=-Kch[1,5]
    Kch[(8,10)]=-Kch[2,4]
    Kch[(10,8)]=-Kch[(2,4)]
    Kch[(11,7)]=-Kch[(5,1)]

    Kch15=Kch
    Iy15=Iy
    J15=J
    #Matriz de rigidez global

    K=np.dot(Tt, Kch)
    K15=np.dot(K,T)

    K15_global=np.zeros((78,78))
    K15_global[54:60,54:60]=K15[:6,:6]
    K15_global[54:60,66:72]=K15[:6,6:]

    K15_global[66:72,66:72]=K15[6:,6:]
    K15_global[66:72,54:60]=K15[6:,:6]

    ###################################################3

    #Tive que adaptaar pro ultimo caso 
    #Preciso tirar 4 pontos
    K_global=K1_global+ K2_global+ K3_global+ K4_global+ K5_global+ K6_global+ K7_global+ K8_global+ K9_global+ K10_global+ K11_global+ K12_global+ K13_global+ K14_global+ K15_global
    K_global_reduzida=K_global[6:,6:]#Tirei o 1
    K_global_reduzida=np.delete(np.delete(K_global_reduzida, slice(36,42), 0), slice(36,42), 1)#Tirei 8
    K_global_reduzida=np.delete(np.delete(K_global_reduzida, slice(36,42), 0), slice(36,42), 1)#Tirei 9
    K_global_reduzida=np.delete(np.delete(K_global_reduzida, slice(36,42), 0), slice(36,42), 1)#Tirei 10
    K_global_reduzida=np.delete(np.delete(K_global_reduzida, slice(36,42), 0), slice(36,42), 1)#Tirei 11
    

    ####################################################
    #Forcas: Static Start-up
    
    f_reduzida=np.zeros(48)
    
    #Força na roda
    f_reduzida[-6]=-750
    f_reduzida[-12]=-750

    #Deslocamentos

    deslocamento=np.linalg.solve(K_global_reduzida, f_reduzida)

    #Forcas Locais

    #Barra1
    #Forcas e Tensões Locais
    d1=np.zeros(12)
    d1[0:6]=np.zeros(6)
    d1[6:12]=deslocamento[0:6]

    fc1=np.dot(Kch1, T1)
    fch1=np.dot(fc1,d1)
    Tn1=fch1[0]/A1#Tensao normal
   
    
    My1_1=fch1[4]
    My1_2=fch1[10]
    if My1_1>My1_2:
        Tf1y=-My1_1*Diametros[0]/(Iy1*2)
    else:
        Tf1y=-My1_2*Diametros[0]/(Iy1*2)
    Mz1_1=fch1[5]
    Mz1_2=fch1[11]
    if Mz1_1>Mz1_2:
        Tf1z=-Mz1_1*Diametros[0]/(Iy1*2)
    else:
        Tf1z=-Mz1_2*Diametros[0]/(Iy1*2)
    Tt1=(fch1[3]*Diametros[0])/(J1*2)#Tensao de torsao
    Teq1=((Tn1+Tf1y+Tf1z)**2+3*(Tt1)**2)**0.5#Tensao equivalente
    
    #Barra2
    #Forcas e Tensões Locais
    d2=np.zeros(12)
    d2[0:6]=deslocamento[0:6]
    d2[6:12]=deslocamento[6:12]
    fc2=np.dot(kch2, T2)
    fch2=np.dot(fc2,d2)
    Tn2=fch2[0]/A2#Tensao normal


    
    My2_1=fch2[4]
    My2_2=fch2[10]
    if My2_1>My2_2:
        Tf2y=-My2_1*Diametros[0]/(Iy1*2)
    else:
        Tf2y=-My2_2*Diametros[0]/(Iy1*2)
    Mz2_1=fch2[5]
    Mz2_2=fch2[11]
    if Mz2_1>Mz2_2:
        Tf2z=-Mz2_1*Diametros[0]/(Iy1*2)
    else:
        Tf2z=-Mz2_2*Diametros[0]/(Iy1*2)
    Tt2=(fch2[3]*Diametros[1])/(J2*2)
    Teq2=((Tn2+Tf2y+Tf2z)**2+3*(Tt2)**2)**0.5#Tensao equivalente

    #Barra3
    #Forcas e Tensões Locais
    d3=np.zeros(12)
    d3[0:6]=deslocamento[6:12]
    d3[6:12]=deslocamento[12:18]
    fc3=np.dot(kch3, T3)
    fch3=np.dot(fc3,d3)
    Tn3=fch3[0]/A3#Tensao normal
    

    My3_1 = fch3[4]
    My3_2 = fch3[10]
    if My3_1 > My3_2:
        Tf3y = -My3_1 * Diametros[0] / (Iy1 * 2)
    else:
        Tf3y = -My3_2 * Diametros[0] / (Iy1 * 2)
    Mz3_1 = fch3[5]
    Mz3_2 = fch3[11]
    if Mz3_1 > Mz3_2:
        Tf3z = -Mz3_1 * Diametros[0] / (Iy1 * 2)
    else:
        Tf3z = -Mz3_2 * Diametros[0] / (Iy1 * 2)
    Tt3 = (fch3[3] * Diametros[2]) / (J3 * 2)
    Teq3 = ((Tn3 + Tf3y + Tf3z) ** 2 + 3 * (Tt3) ** 2) ** 0.5  # Tensao equivalente


    #Barra4
    d4 = np.zeros(12)
    d4[:6] = deslocamento[12:18]
    d4[6:12] = np.zeros(6)
    fc4 = np.dot(kch4, T4)
    fch4 = np.dot(fc4, d4)
    Tn4 = fch4[0] / A4  # Tensao normal
    

    My4_1 = fch4[4]
    My4_2 = fch4[10]
    if My4_1 > My4_2:
        Tf4y = -My4_1 * Diametros[3] / (Iy4 * 2)
    else:
        Tf4y = -My4_2 * Diametros[3] / (Iy4 * 2)
    Mz4_1 = fch4[5]
    Mz4_2 = fch4[11]
    if Mz4_1 > Mz4_2:
        Tf4z = -Mz4_1 * Diametros[3] / (Iy4 * 2)
    else:
        Tf4z = -Mz4_2 * Diametros[3] / (Iy4 * 2)
    Tt4 = (fch4[3] * Diametros[3]) / (J4 * 2)
    Teq4 = ((Tn4 + Tf4y + Tf4z) ** 2 + 3 * (Tt4) ** 2) ** 0.5

    #Barra5
    d5 = np.zeros(12)
    d5[:6] = deslocamento[18:24]
    d5[6:12] = deslocamento[0:6]
    fc5 = np.dot(Kch5, T5)
    fch5 = np.dot(fc5, d5)
    Tn5 = fch5[0] / A5  # Tensao normal
    

    My5_1 = fch5[4]
    My5_2 = fch5[10]
    if My5_1 > My5_2:
        Tf5y = -My5_1 * Diametros[4] / (Iy5 * 2)
    else:
        Tf5y = -My5_2 * Diametros[4] / (Iy5 * 2)
    Mz5_1 = fch5[5]
    Mz5_2 = fch5[11]
    if Mz5_1 > Mz5_2:
        Tf5z = -Mz5_1 * Diametros[4] / (Iy5 * 2)
    else:
        Tf5z = -Mz5_2 * Diametros[4] / (Iy5 * 2)
    Tt5 = (fch5[3] * Diametros[4]) / (J5 * 2)
    Teq5 = ((Tn5 + Tf5y + Tf5z) ** 2 + 3 * (Tt5) ** 2) ** 0.5 

    #Barra6
    d6 = np.zeros(12)
    d6[:6] = deslocamento[6:12]
    d6[6:12] = deslocamento[24:30]
    fc6 = np.dot(Kch6, T6)
    fch6 = np.dot(fc6, d6)
    Tn6 = fch6[0] / A6  # Tensao normal
    
    My6_1 = fch6[4]
    My6_2 = fch6[10]
    if My6_1 > My6_2:
        Tf6y = -My6_1 * Diametros[5] / (Iy6 * 2)
    else:
        Tf6y = -My6_2 * Diametros[5] / (Iy6 * 2)
    Mz6_1 = fch6[5]
    Mz6_2 = fch6[11]
    if Mz6_1 > Mz6_2:
        Tf6z = -Mz6_1 * Diametros[5] / (Iy6 * 2)
    else:
        Tf6z = -Mz6_2 * Diametros[5] / (Iy6 * 2)
    Tt6 = (fch6[3] * Diametros[5]) / (J6 * 2)
    Teq6 = ((Tn6 + Tf6y + Tf6z) ** 2 + 3 * (Tt6) ** 2) ** 0.5
    
    #Barra7
    d7 = np.zeros(12)
    d7[:6] = deslocamento[12:18]
    d7[6:12] = deslocamento[30:36]
    fc7 = np.dot(Kch7, T7)
    fch7 = np.dot(fc7, d7)
    Tn7 = fch7[0] / A7  # Tensao normal
    
    # M1_7 = (fch7[4]**2 + fch7[5]**2) ** 0.5  # Momento maximo
    # M2_7 = (fch7[10]**2 + fch7[11]**2) ** 0.5  # Momento maximo
    # if M1_7>M2_7: 
    #     Tf7 = -M1_7 * Diametros[6] / (Iy7 * 2)  # Tensao de flexao
    # else:
    #     Tf7 = -M2_7 * Diametros[6] / (Iy7 * 2)  # Tensao de flexao
    # Tt7 = (fch7[3] * Diametros[6]) / (J7 * 2)  # Tensao de torsao
    # Teq7 = ((Tn7 + Tf7) ** 2 + 3 * (Tt7) ** 2) ** 0.5  # Tensao equivalente
    My7_1 = fch7[4]
    My7_2 = fch7[10]
    if My7_1 > My7_2:
        Tf7y = -My7_1 * Diametros[6] / (Iy7 * 2)
    else:
        Tf7y = -My7_2 * Diametros[6] / (Iy7 * 2)
    Mz7_1 = fch7[5]
    Mz7_2 = fch7[11]
    if Mz7_1 > Mz7_2:
        Tf7z = -Mz7_1 * Diametros[6] / (Iy7 * 2)
    else:
        Tf7z = -Mz7_2 * Diametros[6] / (Iy7 * 2)
    Tt7 = (fch7[3] * Diametros[6]) / (J7 * 2)
    Teq7 = ((Tn7 + Tf7y + Tf7z) ** 2 + 3 * (Tt7) ** 2) ** 0.5  

    #Barra8
    d8 = np.zeros(12)
    d8[:6] = np.zeros(6)
    d8[6:12] = np.zeros(6)
    fc8 = np.dot(Kch8, T8)
    fch8 = np.dot(fc8, d8)
    Tn8 = fch8[0] / A8  # Tensao normal
    
    # M1_8 = (fch8[4]**2 + fch8[5]**2) ** 0.5  # Momento maximo
    # M2_8 = (fch8[10]**2 + fch8[11]**2) ** 0.5  # Momento maximo
    # if M1_8>M2_8:
    #     Tf8 = -M1_8 * Diametros[7] / (Iy8 * 2)  # Tensao de flexao
    # else:
    #     Tf8 = -M2_8 * Diametros[7] / (Iy8 * 2)  # Tensao de flexao
    # Tt8 = (fch8[3] * Diametros[7]) / (J8 * 2)  # Tensao de torsao
    # Teq8 = ((Tn8 + Tf8) ** 2 + 3 * (Tt8) ** 2) ** 0.5  # Tensao equivalente
    My8_1 = fch8[4]
    My8_2 = fch8[10]
    if My8_1 > My8_2:
        Tf8y = -My8_1 * Diametros[7] / (Iy8 * 2)
    else:
        Tf8y = -My8_2 * Diametros[7] / (Iy8 * 2)
    Mz8_1 = fch8[5]
    Mz8_2 = fch8[11]
    if Mz8_1 > Mz8_2:
        Tf8z = -Mz8_1 * Diametros[7] / (Iy8 * 2)
    else:
        Tf8z = -Mz8_2 * Diametros[7] / (Iy8 * 2)
    Tt8 = (fch8[3] * Diametros[7]) / (J8 * 2)
    Teq8 = ((Tn8 + Tf8y + Tf8z) ** 2 + 3 * (Tt8) ** 2) ** 0.5

    # Para índice 9
    d9 = np.zeros(12)
    d9[:6] = np.zeros(6)
    d9[6:12] = np.zeros(6)
    fc9 = np.dot(Kch9, T9)
    fch9 = np.dot(fc9, d9)
    Tn9 = fch9[0] / A9  # Tensao normal
    
    # M1_9 = (fch9[4]**2 + fch9[5]**2) ** 0.5  # Momento maximo
    # M2_9 = (fch9[10]**2 + fch9[11]**2) ** 0.5  # Momento maximo
    
    # if M1_9>M2_9:
    #     Tf9 = -M1_9 * Diametros[8] / (Iy9 * 2)  # Tensao de flexao
    # else:
    #     Tf9 =-M2_9 * Diametros[8] / (Iy9 * 2)  # Tensao de flexao
    # Tt9 = (fch9[3] * Diametros[8]) / (J9 * 2)  # Tensao de torsao
    # Teq9 = ((Tn9 + Tf9) ** 2 + 3 * (Tt9) ** 2) ** 0.5  # Tensao equivalente
    My9_1 = fch9[4]
    My9_2 = fch9[10]
    if My9_1 > My9_2:
        Tf9y = -My9_1 * Diametros[8] / (Iy9 * 2)
    else:
        Tf9y = -My9_2 * Diametros[8] / (Iy9 * 2)
    Mz9_1 = fch9[5]
    Mz9_2 = fch9[11]
    if Mz9_1 > Mz9_2:
        Tf9z = -Mz9_1 * Diametros[8] / (Iy9 * 2)
    else:
        Tf9z = -Mz9_2 * Diametros[8] / (Iy9 * 2)
    Tt9 = (fch9[3] * Diametros[8]) / (J9 * 2)
    Teq9 = ((Tn9 + Tf9y + Tf9z) ** 2 + 3 * (Tt9) ** 2) ** 0.5

    # Para índice 10
    d10 = np.zeros(12)
    d10[:6] = np.zeros(6)
    d10[6:12] = np.zeros(6)
    fc10 = np.dot(Kch10, T10)
    fch10 = np.dot(fc10, d10)
    Tn10 = fch10[0] / A10  # Tensao normal
    
    My10_1 = fch10[4]
    My10_2 = fch10[10]
    if My10_1 > My10_2:
        Tf10y = -My10_1 * Diametros[9] / (Iy10 * 2)
    else:
        Tf10y = -My10_2 * Diametros[9] / (Iy10 * 2)
    Mz10_1 = fch10[5]
    Mz10_2 = fch10[11]
    if Mz10_1 > Mz10_2:
        Tf10z = -Mz10_1 * Diametros[9] / (Iy10 * 2)
    else:
        Tf10z = -Mz10_2 * Diametros[9] / (Iy10 * 2)
    Tt10 = (fch10[3] * Diametros[9]) / (J10 * 2)
    Teq10 = ((Tn10 + Tf10y + Tf10z) ** 2 + 3 * (Tt10) ** 2) ** 0.5
    # Para índice 11
    d11 = np.zeros(12)
    d11[:6] = np.zeros(6)
    d11[6:12] = np.zeros(6)
    fc11 = np.dot(Kch11, T11)
    fch11 = np.dot(fc11, d11)
    Tn11 = fch11[0] / A11  # Tensao normal
    
    # M1_11 = (fch11[4]**2 + fch11[5]**2) ** 0.5  # Momento maximo
    # M2_11 = (fch11[10]**2 + fch11[11]**2) ** 0.5  # Momento maximo
    
    # if M1_11>M2_11:
        
    #     Tf11 = -M1_11 * Diametros[10] / (Iy11 * 2)  # Tensao de flexao
    # else:
    #     Tf11 = -M2_11 * Diametros[10] / (Iy11 * 2)  # Tensao de flexao
    # Tt11 = (fch11[3] * Diametros[10]) / (J11 * 2)  # Tensao de torsao
    # Teq11 = ((Tn11 + Tf11) ** 2 + 3 * (Tt11) ** 2) ** 0.5  # Tensao equivalente
    My11_1 = fch11[4]
    My11_2 = fch11[10]
    if My11_1 > My11_2:
        Tf11y = -My11_1 * Diametros[10] / (Iy11 * 2)
    else:
        Tf11y = -My11_2 * Diametros[10] / (Iy11 * 2)
    Mz11_1 = fch11[5]
    Mz11_2 = fch11[11]
    if Mz11_1 > Mz11_2:
        Tf11z = -Mz11_1 * Diametros[10] / (Iy11 * 2)
    else:
        Tf11z = -Mz11_2 * Diametros[10] / (Iy11 * 2)
    Tt11 = (fch11[3] * Diametros[10]) / (J11 * 2)
    Teq11 = ((Tn11 + Tf11y + Tf11z) ** 2 + 3 * (Tt11) ** 2) ** 0.5

    # Para índice 12
    d12 = np.zeros(12)
    d12[:6] = deslocamento[12:18]
    d12[6:12] = deslocamento[42:48]#deslocamento[72:78]
    fc12 = np.dot(Kch12, T12)
    fch12 = np.dot(fc12, d12)
    Tn12 = fch12[0] / A12  # Tensao normal
    
    # M1_12 = (fch12[4]**2 + fch12[5]**2) ** 0.5 # Momento maximo
    # M2_12 = (fch12[10]**2 + fch12[11]**2) ** 0.5 # Momento maximo
    
    # if M1_12>M2_12:
        
    #     Tf12 = -M1_12 * Diametros[11] / (Iy12 * 2)  # Tensao de flexao
    # else:
    #     Tf12 = -M2_12 * Diametros[11] / (Iy12 * 2)  # Tensao de flexao
    # Tt12 = (fch12[3] * Diametros[11]) / (J12 * 2)  # Tensao de torsao
    # Teq12 = ((Tn12 + Tf12) ** 2 + 3 * (Tt12) ** 2) ** 0.5  # Tensao equivalente
    My12_1 = fch12[4]
    My12_2 = fch12[10]
    if My12_1 > My12_2:
        Tf12y = My12_1 * Diametros[11] / (Iy12 * 2)
    else:
        Tf12y = My12_2 * Diametros[11] / (Iy12 * 2)
    Mz12_1 = fch12[5]
    Mz12_2 = fch12[11]
    if Mz12_1 > Mz12_2:
        Tf12z = -Mz12_1 * Diametros[11] / (Iy12 * 2)
    else:
        Tf12z = -Mz12_2 * Diametros[11] / (Iy12 * 2)
    Tt12 = (fch12[3] * Diametros[11]) / (J12 * 2)
    Teq12 = ((Tn12 + Tf12y + Tf12z) ** 2 + 3 * (Tt12) ** 2) ** 0.5

    # Para índice 13
    d13 = np.zeros(12)
    d13[:6] = deslocamento[12:18]
    d13[6:12] = deslocamento[36:42]#deslocamento[66:72]
    fc13 = np.dot(Kch13, T13)
    fch13 = np.dot(fc13, d13)
    Tn13 = fch13[0] / A13  # Tensao normal
    
    # M1_13 = (fch13[4]**2 + fch13[5]**2) ** 0.5  # Momento maximo
    # M2_13 = (fch13[10]**2 + fch13[11]**2) ** 0.5
    
    # if M1_13>M2_13:
        
    #     Tf13 = -M1_13 * Diametros[12] / (Iy13 * 2)  # Tensao de flexao
    # else:
    #     Tf13 = -M2_13 * Diametros[12] / (Iy13 * 2)  # Tensao de flexao
    # Tt13 = (fch13[3] * Diametros[12]) / (J13 * 2)  # Tensao de torsao
    # Teq13 = ((Tn13 + Tf13) ** 2 + 3 * (Tt13) ** 2) ** 0.5  # Tensao equivalente
    My13_1 = fch13[4]
    My13_2 = fch13[10]
    if My13_1 > My13_2:
        Tf13y = -My13_1 * Diametros[12] / (Iy13 * 2)
    else:
        Tf13y = -My13_2 * Diametros[12] / (Iy13 * 2)
    Mz13_1 = fch13[5]
    Mz13_2 = fch13[11]
    if Mz13_1 > Mz13_2:
        Tf13z = -Mz13_1 * Diametros[12] / (Iy13 * 2)
    else:
        Tf13z = -Mz13_2 * Diametros[12] / (Iy13 * 2)
    Tt13 = (fch13[3] * Diametros[12]) / (J13 * 2)
    Teq13 = ((Tn13 + Tf13y + Tf13z) ** 2 + 3 * (Tt13) ** 2) ** 0.5
    
    # Para índice 14
    d14 = np.zeros(12)
    d14[:6] = np.zeros(6)
    d14[6:12] = deslocamento[42:48]#deslocamento[72:78]
    fc14 = np.dot(Kch14, T14)
    fch14 = np.dot(fc14, d14)
    Tn14 = fch14[0] / A14  # Tensao normal
    
    # M1_14 = (fch14[4]**2 + fch14[5]**2) ** 0.5 # Momento maximo
    # M2_14 = (fch14[10]**2 + fch14[11]**2) ** 0.5

    # if M1_14>M2_14:
    
    #     Tf14 = -M1_14 * Diametros[13] / (Iy14 * 2)  # Tensao de flexao
    # else:
    #     Tf14 = -M2_14 * Diametros[13] / (Iy14 * 2)  # Tensao de flexao
    # Tt14 = (fch14[3] * Diametros[13]) / (J14 * 2)  # Tensao de torsao
    # Teq14 = ((Tn14 + Tf14) ** 2 + 3 * (Tt14) ** 2) ** 0.5  # Tensao equivalente
    My14_1 = fch14[4]
    My14_2 = fch14[10]
    if My14_1 > My14_2:
        Tf14y = -My14_1 * Diametros[13] / (Iy14 * 2)
    else:
        Tf14y = -My14_2 * Diametros[13] / (Iy14 * 2)
    Mz14_1 = fch14[5]
    Mz14_2 = fch14[11]
    if Mz14_1 > Mz14_2:
        Tf14z = -Mz14_1 * Diametros[13] / (Iy14 * 2)
    else:
        Tf14z = -Mz14_2 * Diametros[13] / (Iy14 * 2)
    Tt14 = (fch14[3] * Diametros[13]) / (J14 * 2)
    Teq14 = ((Tn14 + Tf14y + Tf14z) ** 2 + 3 * (Tt14) ** 2) ** 0.5
    #Teq14=-Tn14 - Tf14y - Tf14z
    # Para índice 15
    d15 = np.zeros(12)
    d15[:6] = np.zeros(6)
    d15[6:12] = deslocamento[36:42]#deslocamento[66:72]
    fc15 = np.dot(Kch15, T15)
    fch15 = np.dot(fc15, d15)
    Tn15 = fch15[0] / A15  # Tensao normal
    
    # M1_15 = (fch15[4]**2 + fch15[5]**2) ** 0.5  # Momento maximo
    # M2_15=  (fch15[10]**2 + fch15[11]**2) ** 0.5
    
    # if M1_15>M2_15:
    
    #     Tf15 = -M1_15 * Diametros[14] / (Iy15 * 2)  # Tensao de flexao
        
        
    # else:
    #     Tf15 = -M2_15 * Diametros[14] / (Iy15 * 2)  # Tensao de flexao
        
    # Tt15 = (fch15[3] * Diametros[14]) / (J15 * 2)  # Tensao de torsao
        
    # Teq15 = ((Tn15 + Tf15) ** 2 + 3 * (Tt15) ** 2) ** 0.5  # Tensao equivalente
    My15_1 = fch15[4]
    My15_2 = fch15[10]
    if My15_1 > My15_2:
        Tf15y = -My15_1 * Diametros[14] / (Iy15 * 2)
    else:
        Tf15y = -My15_2 * Diametros[14] / (Iy15 * 2)
    Mz15_1 = fch15[5]
    Mz15_2 = fch15[11]
    if Mz15_1 > Mz15_2:
        Tf15z = -Mz15_1 * Diametros[14] / (Iy15 * 2)
    else:
        Tf15z = -Mz15_2 * Diametros[14] / (Iy15 * 2)
    Tt15 = (fch15[3] * Diametros[14]) / (J15 * 2)
    Teq15 = ((Tn15 + Tf15y + Tf15z) ** 2 + 3 * (Tt15) ** 2) ** 0.5
    #Teq15=-Tn15 - Tf15y - Tf15z
    #Tensoes equivalentes
    Tensoes_equivalentes=np.zeros((1,15))
    Tensoes_equivalentes=Teq1,Teq2,Teq3,Teq4,Teq5,Teq6,Teq7,Teq8,Teq9,Teq10,Teq11,Teq12,Teq13,Teq14,Teq15
    Tensao_maxima=max(Tensoes_equivalentes)
    return Tensao_maxima
    print(Tensao_maxima)
    



    
    


