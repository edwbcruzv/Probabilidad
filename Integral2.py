from sympy import *
from sympy.integrals.quadrature import gauss_legendre
import math




def funcion_principal(x):
    f=math.exp(-(1/2)*pow(x,2))
    return f

def fun_iter_gaus_legendre(a,b,z):
    x=((b-a)*z+(b+a))/2
    return funcion_principal(x)


def integral_principal(a,b,n):

    cnt=1/(math.sqrt(2*math.pi))

    z, w = gauss_legendre(n,n)
    suma_gauss_legendre=0
    for i in range(n):
        suma_gauss_legendre+=w[i]*fun_iter_gaus_legendre(a,b,z[i])

    suma_gauss_legendre=cnt*((b-a)/2)*suma_gauss_legendre
    #print("gauss_legendre:",suma_gauss_legendre)
    return suma_gauss_legendre

def integral_2(b0,bf,delta):

    lista=[]

    while True:
        I=integral_principal(-6,b0,20)
        #print("b=",f'{b0:.2f}',"  I=",I)
        lista.append([f'{b0:.2f}',I])
        if bf>=b0:
            break
        b0-=delta

    return lista
