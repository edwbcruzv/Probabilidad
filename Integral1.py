from sympy import *
from sympy.integrals.quadrature import gauss_legendre
import math


def funcion_principal(x,sigma,u):
    f=math.exp(-(1/2)*pow((x-u)/sigma,2))
    return f

def fun_iter_gaus_legendre(a,b,z,sigma,u):
    x=((b-a)*z+(b+a))/2
    return funcion_principal(x,sigma,u)


def integral_1(a,b,sigma,u,n):

    cnt=1/(sigma*math.sqrt(2*math.pi))

    z, w = gauss_legendre(n,n)
    suma_gauss_legendre=0
    for i in range(n):
        suma_gauss_legendre+=w[i]*fun_iter_gaus_legendre(a,b,z[i],sigma,u)

    suma_gauss_legendre=cnt*((b-a)/2)*suma_gauss_legendre
    print("gauss_legendre:",suma_gauss_legendre)



n=int(input("ingresar n: "))
integral_1(0,5,5,2,n)