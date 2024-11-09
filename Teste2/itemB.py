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
    return 1/7 * ((((a + b) - (d + c))/w) + (((-2*w) + a - b)/np.power(w, 2)))

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

plt.figure(figsize=(10, 8))

# Gráficos para cada valor de N
for i, N in enumerate(N_values):
    plt.subplot(2, 2, i+1)
    
    # Onda original x(t)
    plt.plot(t_vals, x_t(t_vals), label='x(t) Original', color='blue')
    
    # Aproximação truncada da série de Fourier
    plt.plot(t_vals, x_t_approx(t_vals, N), label=f'Aproximação N={N}', color='orange')
    
    plt.title(f'Aproximação com N={N}')
    plt.xlabel('t')
    plt.ylabel('x(t)')
    plt.legend()

plt.tight_layout()

plt.savefig('ItemB.png')


