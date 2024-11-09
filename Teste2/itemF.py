import numpy as np
import matplotlib.pyplot as plt

# Parâmetros do circuito
R = 100e3  # 100 kOhms
C = 1e-6   # 1 uF
omega_c = 1 / (R * C)  # Frequência de corte
T = 7
w0 = 2 * np.pi / T

# Função de transferência H(jω)
def H_jw(omega):
    if(omega!=0):
        return 1 / (1 - 1j * (omega_c / omega))
    elif(omega==0):
        return 0

# Função para calcular os coeficientes a_k da série de Fourier
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

# Função para calcular a saída do sistema LIT
def y_t_approx(t, N):
    y_approx = np.zeros_like(t, dtype=complex)
    for k in range(-N, N):
        a_k = ak(k)
        omega_k = k * w0
        # Resposta em frequência multiplicada pelo coeficiente a_k
        y_approx += a_k * H_jw(omega_k) * np.exp(1j * omega_k * t)
    return np.real(y_approx)  # Tomando a parte real

# Intervalo de tempo
t_vals = np.linspace(-3.5, 3.5, 1000)

# Número de harmônicos
N_max = 50

# Calcula a saída do sistema LIT para N=50
y_vals = y_t_approx(t_vals, N_max)

#Plotando a saída do sistema
plt.figure(figsize=(8, 6))
plt.plot(t_vals, y_vals, label='y(t) - Saída do Sistema', color='green')
plt.title('Saída do Sistema LIT com N=50')
plt.xlabel('t')
plt.ylabel('y(t)')
plt.grid(True)
plt.legend()
plt.savefig("ItemF.png")
