import numpy as np
import matplotlib.pyplot as plt

# Configuración de la gráfica
fig, axs = plt.subplots(3, 2, figsize=(15, 15))
fig.suptitle('Figuras Paramétricas', fontsize=20, fontweight='bold')

# Parámetros comunes
t = np.linspace(0, 2*np.pi, 400)
a = 1  # Constante arbitraria para algunas figuras
colors = ['#FF5733', '#33C1FF', '#9CFF33', '#FF33EC', '#33FF57', '#FFC300']  # Paleta de colores
lw = 2.5  # Grosor de línea

# 1. Circunferencia
r = 1
x_circ = r * np.cos(t)
y_circ = r * np.sin(t)
axs[0, 0].plot(x_circ, y_circ, color=colors[0], lw=lw)
axs[0, 0].set_title('Circunferencia', fontsize=14, fontweight='bold')
axs[0, 0].set_aspect('equal')
axs[0, 0].grid(True, which='both')

# 2. Cicloide
r = 1
x_cicloide = r * (t - np.sin(t))
y_cicloide = r * (1 - np.cos(t))
axs[0, 1].plot(x_cicloide, y_cicloide, color=colors[1], lw=lw)
axs[0, 1].set_title('Cicloide', fontsize=14, fontweight='bold')
axs[0, 1].set_aspect('equal')
axs[0, 1].grid(True, which='both')

# 3. Hipocicloide
R = 5
r = 3
x_hipo = (R - r) * np.cos(t) + r * np.cos((R - r) / r * t)
y_hipo = (R - r) * np.sin(t) - r * np.sin((R - r) / r * t)
axs[1, 0].plot(x_hipo, y_hipo, color=colors[2], lw=lw)
axs[1, 0].set_title('Hipocicloide', fontsize=14, fontweight='bold')
axs[1, 0].set_aspect('equal')
axs[1, 0].grid(True, which='both')

# 4. Astroide
x_astroide = a * np.cos(t)**3
y_astroide = a * np.sin(t)**3
axs[1, 1].plot(x_astroide, y_astroide, color=colors[3], lw=lw)
axs[1, 1].set_title('Astroide', fontsize=14, fontweight='bold')
axs[1, 1].set_aspect('equal')
axs[1, 1].grid(True, which='both')

# 5. Lemniscata
x_lem = (a * np.cos(t)) / (1 + np.sin(t)**2)
y_lem = (a * np.cos(t) * np.sin(t)) / (1 + np.sin(t)**2)
axs[2, 0].plot(x_lem, y_lem, color=colors[4], lw=lw)
axs[2, 0].set_title('Lemniscata', fontsize=14, fontweight='bold')
axs[2, 0].set_aspect('equal')
axs[2, 0].grid(True, which='both')

# 6. Cardioide
x_cardioide = a * (1 - np.cos(t)) * np.cos(t)
y_cardioide = a * (1 - np.cos(t)) * np.sin(t)
axs[2, 1].plot(x_cardioide, y_cardioide, color=colors[5], lw=lw)
axs[2, 1].set_title('Cardioide', fontsize=14, fontweight='bold')
axs[2, 1].set_aspect('equal')
axs[2, 1].grid(True, which='both')

# Ajustes de diseño
for ax in axs.flat:
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

plt.tight_layout(pad=3.0)
plt.subplots_adjust(top=0.92, hspace=0.5)
plt.show()
