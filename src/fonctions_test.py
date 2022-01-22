# -*- coding: utf-8 -*-

import numpy as np

# On définit ici des fonctions qui permettent de vérifier la précision
# et l'ordre de convergence des formules de quadrature. Pour chaque
# fonction, on définit donc sa primitive.

degre = 0 # degré des polynôme

def monome(x):
    """fonction monome x^k, pour vérifier l'ordre théorique des
    quadratures. Par défaut k=0.

    """
    return x**degre

def primitive_monome(x):
    """primitive de la fonction x^k. Par défaut k=0."""

    return x**(degre+1)/(degre+1.)

# Définir ici les autres fonctions utilisées pour des tests et leurs
# primitives si elles sont connues

def absol(x):
    """fonction valeur absolue |x|."""

    return np.abs(x)

def primitive_absol(x):
    """primitive de la fonction |x|."""

    return 0.5*x*np.abs(x)

def cosinus(x):
    """fonction cosinus cos(x)."""

    return np.cos(x)

def primitive_cosinus(x):
    """primitive de la fonction cos(x)."""

    return np.sin(x)

def expo(x):
    """fonction exponentielle exp(x)."""

    return np.exp(x)

def primitive_expo(x):
    """primitive de la fonction exp(x)."""

    return np.exp(x)

def deriv_arctan(x):
    """fonction deriv de l'arctan deriv_arctan(x)."""

    return 1/(1+x**2)

def arctangente(x):
    """primitive de la fonction deriv_arctan(x)."""

    return np.arctan(x)
