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

# Definindo a função para o FPB ideal
def ideal_filter(w, wc):
    return np.where(np.abs(w) <= wc, 1, 0)

# Função para o filtro de Chebyshev (usando as funções dos itens anteriores)
def chebyshev_response(w, wc, n, epsilon):
    Tn = calcula_coeficientes(w, wc, n)
    return 1 / np.sqrt(1 + epsilon**2 * Tn**2)

# Função para o filtro de Butterworth
def butterworth_response(w, wc, n):
    return 1 / np.sqrt(1 + (w / wc)**(2 * n))

# Parâmetros dos filtros
wc = 10  # frequência de corte

# Frequência de amostra
w = np.linspace(0, 20, 500)

# Calculando as respostas dos filtros
H_ideal = ideal_filter(w, wc)
H_chebyshev = chebyshev_response(w, wc, n=4, epsilon=0.6)
H_butterworth = butterworth_response(w, wc, n=2)

# Plotando as respostas em frequência dos filtros
plt.figure(figsize=(10, 6))
plt.plot(w, H_ideal, label="Filtro Ideal")
plt.plot(w, H_chebyshev, label="Filtro de Chebyshev (ε=0.6, n=4)")
plt.plot(w, H_butterworth, label="Filtro de Butterworth (n=2)")
plt.title("Respostas em frequência dos filtros (item e)")
plt.xlabel("Frequência (rad/s)")
plt.ylabel("|H(jω)|")
plt.legend()
plt.grid(True)
plt.savefig('itemE-1.png')


# Transformada de Fourier para x(t)
def X_w(w):
    return (4 * np.pi / 15) * np.sinc((4 * np.pi * w) / 30 / np.pi)

# Cálculo de |X(jw)|
X_abs = np.abs(X_w(w))

# Filtragem do sinal X(jω) com cada filtro
Y_ideal = X_abs * H_ideal
Y_chebyshev = X_abs * H_chebyshev
Y_butterworth = X_abs * H_butterworth

# Plotando os módulos das saídas dos filtros
plt.figure(figsize=(10, 6))
plt.plot(w, Y_ideal, label="Saída do Filtro Ideal")
plt.plot(w, Y_chebyshev, label="Saída do Filtro Chebyshev (ε=0.6, n=4)")
plt.plot(w, Y_butterworth, label="Saída do Filtro Butterworth (n=2)")
plt.title("Módulo do espectro na saída dos filtros (item e)")
plt.xlabel("Frequência (rad/s)")
plt.ylabel("|Y(jω)|")
plt.legend()
plt.grid(True)
plt.savefig('itemE-2.png')
