import numpy as np
import matplotlib.pyplot as plt
from sympy import true

A = 1
a0 = A/2
n = 20
m = 50
def potencia_m(A, a0, n):
    pm = []
    aux = a0**2
    for i in range(1,n+1,1):
        aux = aux + (A/(i*np.pi))**2
        pm.append(aux)
    return pm

def potencia(A, a0, n):
    pot = a0**2
    for i in range(1, n+1, 1):
       pot = pot + (A/(i*np.pi))**2
    return pot

potM = potencia_m(A, a0, n)
pot = potencia(A, a0, m)

relation_potM_pot = []
for i in range(len(potM)):
    relation_potM_pot.append(potM[i]/pot)

def plot_relation_potM_pot(n, relation):
    plt.plot(n, relation)
    plt.grid(True, which='both')
    plt.xlabel("m Armonicos")
    plt.ylabel("Pm/P")
    plt.title("Relacion de potencia de la señal Diente de Sierra")
    plt.show()

plot_relation_potM_pot(range(1,n+1,1), relation_potM_pot)
