# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import quadratures as q    # nos formules de quadrature
import fonctions_test as f # nos fonctions pour faire des tests

# Ce fichier réalise l'ensemble des tests qui sont demandé dans le TP.

def quadrature_methods(primitive,function,a,b,k_max,method,liste,methode):
    I = primitive(b)-primitive(a) # intégrale exacte puisqu'on connait
                                  # une primitive
    # Boucle sur les découpages
    for i in np.arange(k_max):
        Q[i] = method(function,a,b,N[i])
        E[i] = np.abs(I-Q[i])
        print ("{:5d} {:14.8g} {:14.8g} {:14.8g}".format(N[i],I,Q[i],E[i]))

    # On peut tracer les courbes d'erreur en fonction de N, en échelles
    # logarithmiques (suivant x et y)
    plt.loglog(N,E,'+-',label="fonction {} ({})".format(liste,methode))


# Un premier exemple est donné ci-dessous, qui compare l'intégrale de la
# fonction x^k sur l'intervalle [0,1] avec sa valeur approchée par la
# méthode du point milieu. La comparaisons est faite sur des découpages
# de [0,1] en n=1, 2, 2^2, 2^3,... 2^10 sous-intervalles de même
# longueur, et pour les fonctions f(x)=1, f(x)=x et f(x)=x^2.

# Un deuxième exemple ensuite est réalisé. Celui-ci compare l'intégrale
# des différentes fonctions de fonctions_test.py sur l'intervalle [-1,1] avec
# sa valeur approchée par la méthode du point milieu dans un premier temps, et
# la méthode des trapèzes ensuite. Le découpage de l'intervalle est le même
# que pour l'exemple précédent.

plt.figure(figsize=(8,6), dpi=300)

a,b = -1., 1.           # l'intervalle
k_max = 10              # On va faire l'approximation en découpant en
                        # 2^k morceaux pour k=0,1...k_max

N = 2**np.arange(k_max) # pour avoir 2^{0,1,2,3,4...k_max} -- un tableau
                        # de type np.array
h = (b-a)/N             # c'est aussi un tableau

Q = np.zeros_like(N,dtype=np.float) # Alloue un tableau de la même
                                    # taille que N, initialisé à 0, pour
                                    # stocker les quadratures
E = np.zeros_like(N,dtype=np.float) # Même chose, pour stocker les
                                    # erreurs

nom = ['valeur absolue','cosinus','exponentielle','deriv_arctan']

# Pour le monome de degré 0,1,2: f(x) = 1,x,x^2 et ensuite les différentes
# fonctions_test
for k in np.arange(1):
    print("Test pour la fonction {}".format(nom[3]))

    # if (k==0): # Cas fonction valeur absolue
    print("Méthode du point milieu")
    quadrature_methods(f.arctangente,f.deriv_arctan,a,b,k_max,q.pt_milieu,nom[3],"pt_milieu")
    print("Méthode des trapèzes")
    quadrature_methods(f.arctangente,f.deriv_arctan,a,b,k_max,q.trap,nom[3],"trapèzes")
    print("Méthode de Simpson")
    quadrature_methods(f.arctangente,f.deriv_arctan,a,b,k_max,q.simpson,nom[3],"simpson")
    print("Méthode de GL à 2 pts")
    quadrature_methods(f.arctangente,f.deriv_arctan,a,b,k_max,q.Gauss_Leg_2,nom[3],"GL2")
    print("Méthode de GL à 3 pts")
    quadrature_methods(f.arctangente,f.deriv_arctan,a,b,k_max,q.Gauss_Leg_3,nom[3],"GL3")

    # if (k==1): # Cas fonction cosinus
    #     print("Méthode du point milieu")
    #     quadrature_methods(f.primitive_cosinus,f.cosinus,a,b,k_max,q.pt_milieu,nom[k],"pt_milieu")
    #     print("Méthode des trapèzes")
    #     quadrature_methods(f.primitive_cosinus,f.cosinus,a,b,k_max,q.trap,nom[k],"trapèzes")
    #
    # if (k==2): # Cas fonction exponentielle
    #     print("Méthode du point milieu")
    #     quadrature_methods(f.primitive_expo,f.expo,a,b,k_max,q.pt_milieu,nom[k],"pt_milieu")
    #     print("Méthode des trapèzes")
    #     quadrature_methods(f.primitive_expo,f.expo,a,b,k_max,q.trap,nom[k],"trapèzes")
    #
    # if (k==3): # Cas fonction arctangente
    #     print("Méthode du point milieu")
    #     quadrature_methods(f.arctangente,f.deriv_arctan,a,b,k_max,q.pt_milieu,nom[k],"pt_milieu")
    #     print("Méthode des trapèzes")
    #     quadrature_methods(f.arctangente,f.deriv_arctan,a,b,k_max,q.trap,nom[k],"trapèzes")

# Les huits courbes ont été tracées, on ajoute titre, légende...
plt.title("Test de convergence de toutes les méthodes vues sur la fonction dérivée de arctangente")
plt.legend()
plt.xlabel("N")
plt.ylabel("Erreur")
plt.grid()
# Utilisez une des deux lignes ci-dessous pour voir à l'écran ou enregistrer le graphique
# plt.show()
plt.savefig("../img/test_10.png", dpi=300)
