def fem(Diametros):
    import numpy as np

    #Pontos barra 1
    x1=0
    x2=405.19

    y1=0
    y2=418.97

    z1=0
    z2=0

    L=((x2-x1)**(2)+(y2-y1)**(2)+(z2-z1)**(2))**(1/2)

    l=(x2-x1)/L

    m=(y2-y1)/L

    n=(z2-z1)/L

    D=(l**2+m**2)**(1/2)

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
    G=26500
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
    # #Reposiciona os elementos da matriz(Partes do ponto 1)
    # K1_global=np.zeros((78,78))
    # K1_global[:6,:6]=K1[6:,6:]
    # K1_global[:6,6:12]=K1[6:,:6]
    # #Reposiciona os elementos da matriz(Partes do ponto 2)
    # K1_global[6:12,:6]=K1[:6,6:]
    # K1_global[6:12,6:12]=K1[6:,:6]
    # # K1_global[:6,:6]=K1[6:,6:]
    # # K1_global[:6,6:12]=K1[6:,:6]

    # # K1_global[6:12,:6]=K1[:6,6:]
    # # K1_global[6:12,6:12]=K1[6:,:6]
    K1_global=np.zeros((78,78))
    K1_global[:12,:12]=K1[:,:]

    ###############################################################################################
    #Pontos barra 2
    x1=405.19
    x2=375

    y1=418.97
    y2=510.54

    z1=0
    z2=0

    L=((x2-x1)**(2)+(y2-y1)**(2)+(z2-z1)**(2))**(1/2)

    l=(x2-x1)/L

    m=(y2-y1)/L

    n=(z2-z1)/L

    D=(l**2+m**2)**(1/2)

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
    Di=(0.7558*Diametros[1]+-1.2229)
    A=(np.pi/4)*((Diametros[1]**2)-(Di**2))
    A2=A
    E=69000
    #L=1
    Iy=(np.pi/64)*(Diametros[1]**4-Di**4)
    Iz=(np.pi/64)*(Diametros[1]**4-Di**4)
    G=26500
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


    # K2_global[12:18,:6]=K2[:6,6:]
    # K2_global[12:18,12:18]=K2[6:,:6]

    # K2_global[:6,:6]=K2[6:,6:]
    # K2_global[:6,6:12]=K2[6:,:6]


    # K2_global=np.zeros((66,66))
    # K2_global[:6,:6]=K2[6:,6:]
    # K2_global[:6,6:12]=K2[6:,:6]

    # K2_global[12:18,:6]=K2[:6,6:]
    # K2_global[12:18,12:18]=K2[6:,:6]


    ####################################################

    #Lambda

    #Pontos barra 3
    x1=375
    x2=-100.64

    y1=510.54
    y2=389.13

    z1=0
    z2=0

    L=((x2-x1)**(2)+(y2-y1)**(2)+(z2-z1)**(2))**(1/2)

    l=(x2-x1)/L

    m=(y2-y1)/L

    n=(z2-z1)/L

    D=(l**2+m**2)**(1/2)

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
    G=26500
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

    # K3_global=np.zeros((24,24))
    # K3_global[:6,:6]=K3[6:,6:]
    # K3_global[:6,6:12]=K3[6:,:6]

    # K3_global[18:24,:6]=K3[:6,6:]
    # K3_global[18:24,18:24]=K3[6:,:6]
    K3_global=np.zeros((78,78))

    K3_global[12:24,12:24]=K2[:,:]

    #
    #
    #
    #
    ####################################################

    #Lambda

    #Pontos barra 4
    x1=-100.64
    x2=0

    y1=389.13
    y2=0

    z1=0
    z2=0

    L=((x2-x1)**(2)+(y2-y1)**(2)+(z2-z1)**(2))**(1/2)

    l=(x2-x1)/L

    m=(y2-y1)/L

    n=(z2-z1)/L

    D=(l**2+m**2)**(1/2)

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
    G=26500
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
    x1=407.99
    x2=405.19

    y1=410.48
    y2=418.97

    z1=0
    z2=0

    L=((x2-x1)**(2)+(y2-y1)**(2)+(z2-z1)**(2))**(1/2)

    l=(x2-x1)/L

    m=(y2-y1)/L

    n=(z2-z1)/L

    D=(l**2+m**2)**(1/2)

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
    Di=(0.7558*Diametros[4]-1.2229)
    A=(np.pi/4)*((Diametros[4]**2)-(Di**2))#Tirei a raiz
    A5=A
    E=69000
    #L=1
    Iy=(np.pi/64)*(Diametros[4]**4-Di**4)
    Iz=(np.pi/64)*(Diametros[4]**4-Di**4)#Di esta dando complexo
    G=26500
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
    K5_global[6:12,6:12]=K5[6:,6:]
    K5_global[6:12,24:30]=K5[6:,:6]

    K5_global[24:30,24:30]=K5[:6,:6]
    K5_global[24:30,6:12]=K5[:6,6:]

    ###############################################################################################
    #Pontos barra 6
    x1=375
    x2=373.86

    y1=510.54
    y2=514

    z1=0
    z2=0

    L=((x2-x1)**(2)+(y2-y1)**(2)+(z2-z1)**(2))**(1/2)

    l=(x2-x1)/L

    m=(y2-y1)/L

    n=(z2-z1)/L

    D=(l**2+m**2)**(1/2)

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
    Di=(0.7558*Diametros[5]-1.2229)
    A=(np.pi/4)*((Diametros[5]**2)-(Di**2))
    A6=A
    E=69000
    #L=1
    Iy=(np.pi/64)*(Diametros[5]**4-Di**4)
    Iz=(np.pi/64)*(Diametros[5]**4-Di**4)
    G=26500
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
    K6_global[12:18,12:18]=K6[:6,:6]
    K6_global[12:18,30:36]=K6[:6,6:]

    K6_global[30:36,30:36]=K6[6:,6:]
    K6_global[30:36,12:18]=K6[6:,:6]

    ####################################################

    #Lambda

    #Pontos barra 7
    x1=-100.64
    x2=-107.91

    y1=389.13
    y2=417.27

    z1=0
    z2=0

    L=((x2-x1)**(2)+(y2-y1)**(2)+(z2-z1)**(2))**(1/2)

    l=(x2-x1)/L

    m=(y2-y1)/L

    n=(z2-z1)/L

    D=(l**2+m**2)**(1/2)

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
    Di=(0.7558*Diametros[6]-1.2229)

    A=(np.pi/4)*((Diametros[6]**2)-(Di**2))
    A7=A
    E=69000
    #L=1
    Iy=(np.pi/64)*(Diametros[6]**4-Di**4)
    Iz=(np.pi/64)*(Diametros[6]**4-Di**4)
    G=26500
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
    K7_global[18:24,18:24]=K7[:6,:6]
    K7_global[18:24,36:42]=K7[:6,6:]

    K7_global[36:42,36:42]=K7[6:,6:]
    K7_global[36:42,18:24]=K7[6:,:6]

    ####################################################
    #Pontos barra 8
    x1=0
    x2=0

    y1=0
    y2=0

    z1=45
    z2=25

    L=((x2-x1)**(2)+(y2-y1)**(2)+(z2-z1)**(2))**(1/2)

    l=(x2-x1)/L

    m=(y2-y1)/L

    n=(z2-z1)/L

    D=(l**2+m**2)**(1/2)

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
    G=26500
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
    K8_global[42:48,42:48]=K8[:6,:6]
    K8_global[42:48,48:54]=K8[:6,6:]

    K8_global[48:54,48:54]=K8[6:,6:]
    K8_global[48:54,42:48]=K8[6:,:6]

    ###############################################################################################
    #Pontos barra 9
    x1=0
    x2=0

    y1=0
    y2=0

    z1=25
    z2=0

    L=((x2-x1)**(2)+(y2-y1)**(2)+(z2-z1)**(2))**(1/2)

    l=(x2-x1)/L

    m=(y2-y1)/L

    n=(z2-z1)/L

    D=(l**2+m**2)**(1/2)

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
    Di=(0.7558*Diametros[8]-1.2229)

    A=(np.pi/4)*((Diametros[8]**2)-(Di**2))
    A9=A
    E=69000
    #L=1
    Iy=(np.pi/64)*(Diametros[8]**4-Di**4)
    Iz=(np.pi/64)*(Diametros[8]**4-Di**4)
    G=26500
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
    K9_global[48:54,48:54]=K9[:6,:6]
    K9_global[48:54,:6]=K9[:6,6:]

    K9_global[:6,:6]=K9[6:,6:]
    K9_global[:6,48:54]=K9[6:,:6]


    ####################################################

    #Lambda

    #Pontos barra 10

    x1=0
    x2=0

    y1=0
    y2=0

    z1=0
    z2=-25


    x1=-406.66
    x2=0

    y1=30.33
    y2=0

    z1=-67.5
    z2=-25

    L=((x2-x1)**(2)+(y2-y1)**(2)+(z2-z1)**(2))**(1/2)

    l=(x2-x1)/L

    m=(y2-y1)/L

    n=(z2-z1)/L

    D=(l**2+m**2)**(1/2)

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
    Di=(0.7558*Diametros[9]-1.2229)

    A=(np.pi/4)*((Diametros[9]**2)-(Di**2))
    A10=A
    E=69000
    #L=1
    Iy=(np.pi/64)*(Diametros[9]**4-Di**4)
    Iz=(np.pi/64)*(Diametros[9]**4-Di**4)
    G=26500
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
    K10_global[:6,:6]=K10[:6,:6]
    K10_global[:6,54:60]=K10[:6,6:]

    K10_global[54:60,54:60]=K10[6:,6:]
    K10_global[54:60,:6]=K10[6:,:6]

    ############################################################
    #Lambda

    #Pontos barra 11
    x1=0
    x2=0

    y1=0
    y2=0

    z1=-25
    z2=-45

    L=((x2-x1)**(2)+(y2-y1)**(2)+(z2-z1)**(2))**(1/2)

    l=(x2-x1)/L

    m=(y2-y1)/L

    n=(z2-z1)/L

    D=(l**2+m**2)**(1/2)

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
    Di=(0.7558*Diametros[10]-1.2229)

    A=(np.pi/4)*((Diametros[10]**2)-(Di**2))
    A11=A
    E=69000
    #L=1
    Iy=(np.pi/64)*(Diametros[10]**4-Di**4)
    Iz=(np.pi/64)*(Diametros[10]**4-Di**4)
    G=26500
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
    K11_global[54:60,54:60]=K11[:6,:6]
    K11_global[54:60,60:66]=K11[:6,6:]

    K11_global[60:66,60:66]=K11[6:,6:]
    K11_global[60:66,54:60]=K11[6:,:6]

    ####################################################
    #Pontos barra 12
    x1=-100.64
    x2=-406.66

    y1=389.13
    y2=30.33

    z1=0
    z2=67.5

    L=((x2-x1)**(2)+(y2-y1)**(2)+(z2-z1)**(2))**(1/2)

    l=(x2-x1)/L

    m=(y2-y1)/L

    n=(z2-z1)/L

    D=(l**2+m**2)**(1/2)

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
    G=26500
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
    K12_global[18:24,18:24]=K12[:6,:6]
    K12_global[18:24,72:78]=K12[:6,6:]

    K12_global[72:78,72:78]=K12[6:,6:]
    K12_global[72:78,18:24]=K12[6:,:6]

    ############################################
    #Pontos barra 13
    x1=-100.64
    x2=-406.66

    y1=389.13
    y2=30.33

    z1=0
    z2=-67.5

    L=((x2-x1)**(2)+(y2-y1)**(2)+(z2-z1)**(2))**(1/2)

    l=(x2-x1)/L

    m=(y2-y1)/L

    n=(z2-z1)/L

    D=(l**2+m**2)**(1/2)

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
    Di=(0.7558*Diametros[12]-1.2229)

    A=(np.pi/4)*((Diametros[12]**2)-(Di**2))#Tirei a raiz
    A13=A
    E=69000
    #L=1
    Iy=(np.pi/64)*(Diametros[12]**4-Di**4)
    Iz=(np.pi/64)*(Diametros[12]**4-Di**4)#Di esta dando complexo
    G=26500
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
    x2=-406.66

    y1=0
    y2=30.33

    z1=25
    z2=67.5

    L=((x2-x1)**(2)+(y2-y1)**(2)+(z2-z1)**(2))**(1/2)

    l=(x2-x1)/L

    m=(y2-y1)/L

    n=(z2-z1)/L

    D=(l**2+m**2)**(1/2)

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
    G=26500
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
    x2=-406.66

    y1=0
    y2=30.33

    z1=-25
    z2=67.5

    L=((x2-x1)**(2)+(y2-y1)**(2)+(z2-z1)**(2))**(1/2)

    l=(x2-x1)/L

    m=(y2-y1)/L

    n=(z2-z1)/L

    D=(l**2+m**2)**(1/2)

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
    Di=(0.7558*Diametros[14]+-1.2229)

    A=(np.pi/4)*((Diametros[14]**2)-(Di**2))
    A15=A
    E=69000
    #L=1
    Iy=(np.pi/64)*(Diametros[14]**4-Di**4)
    Iz=(np.pi/64)*(Diametros[14]**4-Di**4)
    G=26500
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


    K_global=K1_global+ K2_global+ K3_global+ K4_global+ K5_global+ K6_global+ K7_global+ K8_global+ K9_global+ K10_global+ K11_global+ K12_global+ K13_global+ K14_global+ K15_global
    K_global_reduzida=K_global[:66,:66]


    ####################################################
    #Forcas: Static Start-up

    f=np.zeros(78)

    #f[1]=-200
    #f[19]=-700
    f[37]=-100
    f_reduzida=f[:66]

    #Deslocamentos

    #kex=np.zeros((24,24))
    #kex[0:6,0:6]=K_global[0:6,0:6]#N usei?
    deslocamento=np.linalg.solve(K_global_reduzida, f_reduzida)

    #Forcas Locais

    #Barra1
    #Forcas e Tensões Locais
    d1=np.zeros(12)
    d1[:]=deslocamento[:12]

    fc1=np.dot(Kch1, T1)
    fch1=np.dot(fc1,d1)
    Tn1=fch1[0]/A1#Tensao normal
    #Tc1=((fch1[1]**2+fch1[2]**2)**0.5)/A1 #Tensao de cisalhamento
    Mm1=((fch1[4]**2+fch1[5]**2)**0.5) #Momento maximo
    Tf1=-Mm1*Diametros[0]/(Iy1*2)#Tensao de flexao
    Tt1=(fch1[3]*Diametros[0])/(J1/2)#Tensao de torsao
    Teq1=((Tn1+Tf1)**2+3*(Tt1)**2)**0.55#Tensao equivalente
    
    #Barra2
    #Forcas e Tensões Locais
    d2=np.zeros(12)
    d2[:12]=deslocamento[6:18]
    fc2=np.dot(kch2, T2)
    fch2=np.dot(fc2,d2)
    Tn2=fch2[0]/A2#Tensao normal
    #Tc2=(fch2[1]**2+fch2[2]**2)**0.5 #Tensao de cisalhamento
    Mm2=((fch2[4]**2+fch2[5]**2)**0.5) #Momento maximo
    Tf2=-Mm2*Diametros[1]/(Iy2*2)#Tensao de flexao
    Tt2=(fch2[3]*Diametros[1])/(J1/2)#Tensao de torsao
    Teq2=((Tn2+Tf2)**2+3*(Tt2)**2)**0.55#Tensao equivalente

    #Barra3
    #Forcas e Tensões Locais
    d3=np.zeros(12)
    d3[:12]=deslocamento[12:24]
    fc3=np.dot(kch3, T3)
    fch3=np.dot(fc3,d3)
    Tn3=fch3[0]/A3#Tensao normal
    Mm3=((fch3[4]**2+fch3[5]**2)**0.5) #Momento maximo
    Tf3=-Mm3*Diametros[2]/(Iy3*2)#Tensao de flexao
    Tt3=(fch3[3]*Diametros[2])/(J1/2)#######################Mudei aqui
    Teq3=((Tn3+Tf3)**2+3*((Tt3)**2))**0.5#Tensao equivalente

    #Barra4
    d4 = np.zeros(12)
    d4[:6] = deslocamento[18:24]
    d4[6:12] = deslocamento[:6]
    fc4 = np.dot(kch4, T4)
    fch4 = np.dot(fc4, d4)
    Tn4 = fch4[0] / A4  # Tensao normal
    Mm4 = ((fch4[4]**2 + fch4[5]**2) ** 0.5 )  # Momento maximo
    Tf4 = Mm4 * Diametros[3] / (Iy4 * 2)  # Tensao de flexao
    Tt4 = (fch4[3] * Diametros[3]) / (J1 / 2)  # Tensao de torsao
    Teq4 = ((Tn4 + Tf4) ** 2 + 3 * (Tt4) ** 2) ** 0.5  # Tensao equivalente

    #Barra5
    d5 = np.zeros(12)
    d5[:6] = deslocamento[24:30]
    d5[6:12] = deslocamento[6:12]
    fc5 = np.dot(Kch5, T5)
    fch5 = np.dot(fc5, d5)
    Tn5 = fch5[0] / A5  # Tensao normal
    Mm5 = ((fch5[4]**2 + fch5[5]**2) ** 0.5)  # Momento maximo
    Tf5 = Mm5 * Diametros[4] / (Iy5 * 2)  # Tensao de flexao
    Tt5 = (fch5[3] * Diametros[4]) / (J1 / 2)  # Tensao de torsao
    Teq5 = ((Tn5 + Tf5) ** 2 + 3 * (Tt5) ** 2) ** 0.5  # Tensao equivalente

    #Barra6
    d6 = np.zeros(12)
    d6[:6] = deslocamento[12:18]
    d6[6:12] = deslocamento[30:36]
    fc6 = np.dot(Kch6, T6)
    fch6 = np.dot(fc6, d6)
    Tn6 = fch6[0] / A6  # Tensao normal
    Mm6 = (fch6[4]**2 + fch6[5]**2) ** 0.5  # Momento maximo
    Tf6 = Mm6 * Diametros[5] / (Iy6 * 2)  # Tensao de flexao
    Tt6 = (fch6[3] * Diametros[5]) / (J1 / 2)  # Tensao de torsao
    Teq6 = ((Tn6 + Tf6) ** 2 + 3 * (Tt6) ** 2) ** 0.5  # Tensao equivalente

    #Barra7
    d7 = np.zeros(12)
    d7[:6] = deslocamento[18:24]
    d7[6:12] = deslocamento[36:42]
    fc7 = np.dot(Kch7, T7)
    fch7 = np.dot(fc7, d7)
    Tn7 = fch7[0] / A7  # Tensao normal
    Mm7 = (fch7[4]**2 + fch7[5]**2) ** 0.5  # Momento maximo
    Tf7 = Mm7 * Diametros[6] / (Iy7 * 2)  # Tensao de flexao
    Tt7 = (fch7[3] * Diametros[6]) / (J1 / 2)  # Tensao de torsao
    Teq7 = ((Tn7 + Tf7) ** 2 + 3 * (Tt7) ** 2) ** 0.5  # Tensao equivalente

    #Barra8
    d8 = np.zeros(12)
    d8[:6] = deslocamento[42:48]
    d8[6:12] = deslocamento[48:54]
    fc8 = np.dot(Kch8, T8)
    fch8 = np.dot(fc8, d8)
    Tn8 = fch8[0] / A8  # Tensao normal
    Mm8 = (fch8[4]**2 + fch8[5]**2) ** 0.5  # Momento maximo
    Tf8 = Mm8 * Diametros[7] / (Iy8 * 2)  # Tensao de flexao
    Tt8 = (fch8[3] * Diametros[7]) / (J1 / 2)  # Tensao de torsao
    Teq8 = ((Tn8 + Tf8) ** 2 + 3 * (Tt8) ** 2) ** 0.5  # Tensao equivalente

    # Para índice 9
    d9 = np.zeros(12)
    d9[:6] = deslocamento[48:54]
    d9[6:12] = deslocamento[:6]
    fc9 = np.dot(Kch9, T9)
    fch9 = np.dot(fc9, d9)
    Tn9 = fch9[0] / A9  # Tensao normal
    Mm9 = (fch9[4]**2 + fch9[5]**2) ** 0.5  # Momento maximo
    Tf9 = Mm9 * Diametros[8] / (Iy9 * 2)  # Tensao de flexao
    Tt9 = (fch9[3] * Diametros[8]) / (J1 / 2)  # Tensao de torsao
    Teq9 = ((Tn9 + Tf9) ** 2 + 3 * (Tt9) ** 2) ** 0.5  # Tensao equivalente

    # Para índice 10
    d10 = np.zeros(12)
    d10[:6] = deslocamento[:6]
    d10[6:12] = deslocamento[54:60]
    fc10 = np.dot(Kch10, T10)
    fch10 = np.dot(fc10, d10)
    Tn10 = fch10[0] / A10  # Tensao normal
    Mm10 = (fch10[4]**2 + fch10[5]**2) ** 0.5  # Momento maximo
    Tf10 = Mm10 * Diametros[9] / (Iy10 * 2)  # Tensao de flexao
    Tt10 = (fch10[3] * Diametros[9]) / (J1 / 2)  # Tensao de torsao
    Teq10 = ((Tn10 + Tf10) ** 2 + 3 * (Tt10) ** 2) ** 0.5  # Tensao equivalente

    # Para índice 11
    d11 = np.zeros(12)
    d11[:6] = deslocamento[54:60]
    d11[6:12] = deslocamento[60:66]
    fc11 = np.dot(Kch11, T11)
    fch11 = np.dot(fc11, d11)
    Tn11 = fch11[0] / A11  # Tensao normal
    Mm11 = (fch11[4]**2 + fch11[5]**2) ** 0.5  # Momento maximo
    Tf11 = Mm11 * Diametros[10] / (Iy11 * 2)  # Tensao de flexao
    Tt11 = (fch11[3] * Diametros[10]) / (J1 / 2)  # Tensao de torsao
    Teq11 = ((Tn11 + Tf11) ** 2 + 3 * (Tt11) ** 2) ** 0.5  # Tensao equivalente

    # Para índice 12
    d12 = np.zeros(12)
    d12[:6] = deslocamento[18:24]
    d12[6:12] = np.zeros(6)#deslocamento[72:78]
    fc12 = np.dot(Kch12, T12)
    fch12 = np.dot(fc12, d12)
    Tn12 = fch12[0] / A12  # Tensao normal
    Mm12 = (fch12[4]**2 + fch12[5]**2) ** 0.5 # Momento maximo
    Tf12 = Mm12 * Diametros[11] / (Iy12 * 2)  # Tensao de flexao
    Tt12 = (fch12[3] * Diametros[11]) / (J1 / 2)  # Tensao de torsao
    Teq12 = ((Tn12 + Tf12) ** 2 + 3 * (Tt12) ** 2) ** 0.5  # Tensao equivalente

    # Para índice 13
    d13 = np.zeros(12)
    d13[:6] = deslocamento[18:24]
    d13[6:12] = np.zeros(6)#deslocamento[66:72]
    fc13 = np.dot(Kch13, T13)
    fch13 = np.dot(fc13, d13)
    Tn13 = fch13[0] / A13  # Tensao normal
    Mm13 = (fch13[4]**2 + fch13[5]**2) ** 0.5  # Momento maximo
    Tf13 = Mm13 * Diametros[12] / (Iy13 * 2)  # Tensao de flexao
    Tt13 = (fch13[3] * Diametros[12]) / (J1 / 2)  # Tensao de torsao
    Teq13 = ((Tn13 + Tf13) ** 2 + 3 * (Tt13) ** 2) ** 0.5  # Tensao equivalente

    # Para índice 14
    d14 = np.zeros(12)
    d14[:6] = deslocamento[42:48]
    d14[6:12] = np.zeros(6)#deslocamento[72:78]
    fc14 = np.dot(Kch14, T14)
    fch14 = np.dot(fc14, d14)
    Tn14 = fch14[0] / A14  # Tensao normal
    Mm14 = (fch14[4]**2 + fch14[5]**2) ** 0.5 # Momento maximo
    Tf14 = Mm14 * Diametros[13] / (Iy14 * 2)  # Tensao de flexao
    Tt14 = (fch14[3] * Diametros[13]) / (J1 / 2)  # Tensao de torsao
    Teq14 = ((Tn14 + Tf14) ** 2 + 3 * (Tt14) ** 2) ** 0.5  # Tensao equivalente

    # Para índice 15
    d15 = np.zeros(12)
    d15[:6] = deslocamento[54:60]
    d15[6:12] = np.zeros(6)#deslocamento[66:72]
    fc15 = np.dot(Kch15, T15)
    fch15 = np.dot(fc15, d15)
    Tn15 = fch15[0] / A15  # Tensao normal
    Mm15 = (fch15[4]**2 + fch15[5]**2) ** 0.5  # Momento maximo
    Tf15 = Mm15 * Diametros[14] / (Iy15 * 2)  # Tensao de flexao
    Tt15 = (fch15[3] * Diametros[14]) / (J1 / 2)  # Tensao de torsao
    Teq15 = ((Tn15 + Tf15) ** 2 + 3 * (Tt15) ** 2) ** 0.5  # Tensao equivalente
    print(fch12)
    print(fch13)
    #Tensoes equivalentes
    Tensoes_equivalentes=np.zeros((1,15))
    Tensoes_equivalentes=Teq1,Teq2,Teq3,Teq4,Teq5,Teq6,Teq7,Teq8,Teq9,Teq10,Teq11,Teq12,Teq13,Teq14,Teq15
    Tensao_maxima=max(Tensoes_equivalentes)
    print(Tensao_maxima)

