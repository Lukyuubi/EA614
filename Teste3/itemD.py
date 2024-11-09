import numpy as np
import matplotlib.pyplot as plt

# Definindo a função sinc ajustada para a transformada dada
def X_w(w):
    return (4 * np.pi / 15) * np.sinc((4 * np.pi * w) / 30 / np.pi)

# Vetor de frequências de 0 a 40 rad/s
w = np.linspace(0, 40, 500)

# Cálculo de |X(jw)|
X_abs = np.abs(X_w(w))

# Plotando o módulo de X(jw)
plt.figure(figsize=(10, 6))
plt.plot(w, X_abs, label=r"$|X(j\omega)|$")
plt.title("Módulo de X(jω) para o pulso retangular (item d)")
plt.xlabel("Frequência (rad/s)")
plt.ylabel(r"$|X(j\omega)|$")
plt.grid(True)
plt.legend()
plt.savefig('ItemD.png')
