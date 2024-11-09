import numpy as np
import matplotlib.pyplot as plt

def calcula_coeficientes(w,wc,n):
    Tn = np.zeros((w.size,))
    #determina os valores dos coeficientes segundo as expressões padronizadas
    Tn[abs(w) < wc] = np.cos(n*np.arccos(w[abs(w) < wc] / wc))
    Tn[abs(w) >= wc] = np.cosh(n*np.arccosh(w[abs(w) >= wc] / wc))
    return Tn

def chebyshev_response(w, wc, n, epsilon):
    Tn = calcula_coeficientes(w, wc, n)
    return 1 / np.sqrt(1 + epsilon**2 * Tn**2)

# Frequência de amostra
w = np.linspace(0, 20, 500)

# Parâmetros do item b 
wc = 10
n = 3
epsilons = [0.1, 0.3, 0.5, 0.7, 0.9]

for epsilon in epsilons:
    Habs = chebyshev_response(w, wc, n, epsilon)
    plt.plot(w, Habs, label=f"ε={epsilon}")
plt.title("Resposta em frequência do filtro de Chebyshev (item b)")
plt.xlabel("Frequência (rad/s)")
plt.ylabel("|H(jω)|")
plt.legend()
plt.grid(True)
plt.savefig('ItemB.png')