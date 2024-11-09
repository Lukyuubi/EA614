import numpy as np
import matplotlib.pyplot as plt

def calcula_coeficientes(w,wc,n):
    Tn = np.zeros((w.size,))
    #determina os valores dos coeficientes segundo as expressões padronizadas
    Tn[abs(w) < wc] = np.cos(n*np.arccos(w[abs(w) < wc] / wc))
    Tn[abs(w) >= wc] = np.cosh(n*np.arccosh(w[abs(w) >= wc] / wc))
    return Tn

# Função para calcular a resposta em frequência de Butterworth
def butterworth_response(w, wc, n):
    return 1 / np.sqrt(1 + (w / wc)**(2 * n))

# Frequência de amostra
w = np.linspace(0, 20, 500)

# Parâmetros do item c
wc = 10

plt.figure(figsize=(10, 6))
for n in range(1, 6):
    Habs = butterworth_response(w, wc, n)
    plt.plot(w, Habs, label=f"n={n}")
plt.title("Resposta em frequência do filtro de Butterworth (item c)")
plt.xlabel("Frequência (rad/s)")
plt.ylabel("|H(jω)|")
plt.legend()
plt.grid(True)
plt.savefig('ItemC.png')