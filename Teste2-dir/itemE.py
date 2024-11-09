import numpy as np
import matplotlib.pyplot as plt

# Parâmetros do circuito
R = 100e3  # 100 kOhms
C = 1e-6   # 1 uF
omega_c = 1 / (R * C)  # Frequência de corte

# Função de transferência H(jω)
def H_jw(omega):
    return 1 / (1 - 1j * (omega_c / omega))

# Intervalo de frequências ω
omega_vals = np.logspace(-2, 4, 500) 

# Calcula módulo e fase de H(jω)
H_vals = H_jw(omega_vals)
mod_H = np.abs(H_vals)  # Módulo
fase_H = np.angle(H_vals)  # Fase

# Plotando o módulo de H(jω)
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.semilogx(omega_vals, mod_H)
plt.title('Módulo de H(jω)')
plt.xlabel('ω (rad/s)')
plt.ylabel('|H(jω)|')
plt.grid(True)

# Plotando a fase de H(jω)
plt.subplot(1, 2, 2)
plt.semilogx(omega_vals, fase_H)
plt.title('Fase de H(jω)')
plt.xlabel('ω (rad/s)')
plt.ylabel('Fase de H(jω) (rad)')
plt.grid(True)

plt.tight_layout()
plt.savefig("ItemE.png")
