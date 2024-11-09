import numpy as np
import matplotlib.pyplot as plt

# Definindo constantes
T = 7
w0 = 2 * np.pi / T

# Definindo a função original x(t)
def x_t(t):
    return np.where(np.logical_and(t >= -2, t < -1), -1,
           np.where(np.logical_and(t >= -1, t < 0), t + 1,
           np.where(np.logical_and(t >= 0, t < 1), t - 1,
           np.where(np.logical_and(t >= 1, t < 2), 1, 0))))

def ak(k):
    w = (1j * w0 * k)
    a = np.power(np.e, w)
    b = np.power(np.e, -w)
    c = np.power(np.e, -2*w)
    d = np.power(np.e, 2*w)
    if(k!=0):
        return 1/7 * ((((a + b) - (d + c))/w) + (((-2*w) + a - b)/np.power(w, 2)))
    elif(k==0):
        return 0

# Função para aproximar x(t) usando a série de Fourier truncada
def x_t_approx(t, N):
    x_approx = np.zeros_like(t, dtype=complex)
    #ak
    for k in range(-N, N+1):
        if k!=0:
            x_approx += ak(k) * np.exp(1j * k * w0 * t)
        elif(k==0):
            x_approx += 0 #a0=0
    return np.real(x_approx)  # Tomando a parte real

# Intervalo de tempo para plotar a função
t_vals = np.linspace(-3.5, 3.5, 1000)

# Valores de N para a aproximação
N_values = [1, 10, 20, 50]

# Função para calcular os coeficientes a_k para valores de k
def calc_ak_vals(N):
    a_k_vals = []
    k_vals = np.arange(-N, N+1)
    for k in k_vals:
        a_k_vals.append(np.abs(ak(k)))  # Calcula o módulo de a_k
    return k_vals, a_k_vals

# Calculando a_k e gerando gráfico para N=50
N_max = 50
k_vals, a_k_vals = calc_ak_vals(30)

# Gráfico do módulo dos coeficientes |a_k| em função de ω = k*ω0
omega_vals = k_vals * w0

plt.figure(figsize=(8, 6))
plt.stem(omega_vals, a_k_vals)
plt.title(f'Módulo dos coeficientes |a_k| em função de ω para N={N_max}')
plt.xlabel('ω (rad/s)')
plt.ylabel('|a_k|')
plt.grid(True)
plt.savefig("ItemD.png")
