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

# Função para calcular os coeficientes a_k da série de Fourier
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


# Função para calcular a potência média do erro P_N
def calc_potencia_erro(t_vals, N):
    # Sinal original
    x_vals = x_t(t_vals)
    
    # Aproximação truncada da série de Fourier
    x_approx_vals = x_t_approx(t_vals, N)
    
    # Calcula o erro quadrático
    erro = (x_vals - x_approx_vals)
    
    # Potência média do erro (média dos valores do erro quadrático)
    P_N = np.sum(np.abs(erro)**2)/len(t_vals)
    
    return P_N

# Intervalo de tempo para plotar a função
t_vals = np.linspace(-3.5, 3.5, 1000)

# Valores de N para a aproximação
N_values = [1, 10, 20, 50]


# Calculando P_N para diferentes valores de N
for N in N_values:
    P_N = calc_potencia_erro(t_vals, N)
    print(f'Potência média do erro para N={N}: {P_N}')