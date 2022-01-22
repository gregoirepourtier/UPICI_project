# -*- coding: utf-8 -*-

import numpy as np

def pt_milieu(f,a,b,n):
    """Quadrature de \int_a^b f(x)dx par la méthode du point milieu sur
    [a,b] découpé en n sous-intervalles égaux.

    """

    h = (b-a)/n
    xm = a + (0.5+np.arange(n))*h
    Q = h*np.sum(f(xm))
    return Q

# Définir ci-dessous les autres méthodes de quadrature

def trap(f,a,b,n):
    """Quadrature de \int_a^b f(x)dx par la méthode des trapèzes sur
    [a,b] découpé en n sous-intervalles égaux.

    """

    h = (b-a)/n
    xm = a + np.arange(1,n)*h

    Q = h * ((f(a)+f(b))/2 + np.sum(f(xm)))

    return Q

def simpson(f,a,b,n):
    """Quadrature de \int_a^b f(x)dx par la méthode de Simpson sur
    [a,b] découpé en n sous-intervalles égaux.

    """

    h = (b-a)/n
    xm1 = a + np.arange(n)*h
    xm2 = a + (0.5+np.arange(n))*h
    xm3 = a + (1+np.arange(n))*h

    Q = (h/6) * np.sum(f(xm1) + 4*f(xm2) + f(xm3))

    return Q

def Gauss_Leg_2(f,a,b,n):
    """Quadrature de \int_a^b f(x)dx par la méthode de Gauss-Legendre à 2 points
    sur [a,b] découpé en 2 sous-intervalles irréguliers.

    """

    x0 = -1/np.sqrt(3)
    x1 = 1/np.sqrt(3)

    Q = f(x0) + f(x1)

    return Q

def Gauss_Leg_3(f,a,b,n):
    """Quadrature de \int_a^b f(x)dx par la méthode de Gauss-Legendre à 3 points
    sur [a,b] découpé en 3 sous-intervalles irréguliers.

    """

    x0 = -np.sqrt(3/5)
    x1 = 0
    x2 = np.sqrt(3/5)

    Q = (5/9)*f(x0) + (8/9)*f(x1) + (5/9)*f(x2)

    return Q
