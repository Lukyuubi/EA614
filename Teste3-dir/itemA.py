import numpy as np
import matplotlib.pyplot as plt
""" Funções auxiliares para a resolução do exercício """

""" Rotina que calcula os coeficientes do polinômio de Chebyshev de maneira não-recursiva 

Parâmetros: w - vetor de frequências (sugestão: usar um vetor com amostras de 0 a 20 rad/s)
            wc - freq. de corte do filtro (em rad/s)
            n - ordem do filtro de Chebyshev
Saída:      Tn - vetor com os coeficientes calculados do polinômio de Chebyshev (possui o mesmo tamanho que w)

""" 
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

wc=10
epsilon = 0.2
plt.figure(figsize=(10, 6))

for n in range(1, 6):
    Habs = chebyshev_response(w, wc, n, epsilon)
    plt.plot(w, Habs, label=f"n={n}")

plt.title("Resposta em frequência do filtro de Chebyshev (item a)")
plt.xlabel("Frequência (rad/s)")
plt.ylabel("|H(jω)|")
plt.legend()
plt.grid(True)
plt.savefig('ItemA.png')
