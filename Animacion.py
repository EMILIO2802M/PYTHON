import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.widgets import Button

# Parámetros
t_a = np.linspace(-2, 6, 100)   # Para la función a
t_b = np.linspace(0, 2 * np.pi, 100)  # Para la función b
t_c = np.linspace(0, 10, 100)   # Para la función c
t_d = np.linspace(0, 10, 100)   # Para la función d
t_e = np.linspace(0, 2 * np.pi, 100)  # Para la función e

# Funciones paramétricas
# a
x_a = np.sqrt(2 * t_a + 4)
y_a = 2 * t_a + 1

# b
x_b = 4 * np.cos(t_b)
y_b = 3 * np.sin(t_b)

# c
x_c = t_c
y_c = 2 * t_c**2 - 3

# d
x_d = 3 * t_d - 2
y_d = 18 * t_d**2 - 24 * t_d + 6

# e
x_e = 3 * np.cos(t_e) + np.cos(3 * t_e)
y_e = 3 * np.sin(t_e) - np.sin(3 * t_e)

# Configuración de la figura
fig, ax = plt.subplots(figsize=(10, 10))
lines = []
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#FFD133']  # Colores vibrantes para cada función
linestyles = ['-', '--', '-.', ':', '-']  # Estilos de línea variados

# Inicializar las líneas
for i, (x, y) in enumerate(zip(
    [x_a, x_b, x_c, x_d, x_e],
    [y_a, y_b, y_c, y_d, y_e]
)):
    line, = ax.plot([], [], lw=3, color=colors[i], linestyle=linestyles[i], label=f'Función {chr(97+i)}')  # chr(97) = 'a'
    lines.append(line)

# Configuración del gráfico
ax.set_xlim(-20, 20)
ax.set_ylim(-20, 20)
ax.set_title("Animación de Funciones Paramétricas", fontsize=20, fontweight='bold', color='navy')
ax.set_xlabel("x(t)", fontsize=14)
ax.set_ylabel("y(t)", fontsize=14)
ax.legend(loc='upper left', fontsize=10, shadow=True, fancybox=True, framealpha=0.8)
ax.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.5)

# Fondo colorido
fig.patch.set_facecolor('#f2f2f2')  # Fondo de la figura
ax.set_facecolor('#e6f7ff')  # Fondo del gráfico

# Crear un gradiente de fondo
gradient = np.linspace(0, 1, 100).reshape(1, -1)
ax.imshow(gradient, aspect='auto', cmap='Blues', extent=[-20, 20, -20, 20], alpha=0.1)

# Agregar un marco alrededor del gráfico
for spine in ax.spines.values():
    spine.set_visible(True)
    spine.set_linewidth(2)
    spine.set_color('#333333')

# Funciones de inicialización y actualización para la animación
def init():
    for line in lines:
        line.set_data([], [])
    return lines

def update(frame):
    for i, line in enumerate(lines):
        line.set_data(eval(f'x_{chr(97+i)}[:frame]'), eval(f'y_{chr(97+i)}[:frame]'))
    return lines

# Crear la animación
ani = animation.FuncAnimation(fig, update, frames=100, init_func=init, blit=True, repeat=False)

# Función para mostrar/ocultar líneas individuales
def toggle_line(label):
    idx = ord(label) - 97  # Convierte 'a'-'e' en índices 0-4
    line = lines[idx]
    line.set_visible(not line.get_visible())
    plt.draw()

# Función para mostrar/ocultar todas las líneas
all_visible = True
def toggle_all(event):
    global all_visible
    for line in lines:
        line.set_visible(not all_visible)
    all_visible = not all_visible
    plt.draw()

# Crear botones para cada línea
button_axes = plt.axes([0.83, 0.7, 0.13, 0.25])  # Área para los botones de funciones
buttons = []
for i, label in enumerate(['a', 'b', 'c', 'd', 'e']):
    ax_button = plt.axes([0.85, 0.7 - i * 0.06, 0.1, 0.04])  # Ajustar posición de cada botón
    button = Button(ax_button, f'Función {label}', color='#e6f7ff', hovercolor='#ccf2ff')
    button.on_clicked(lambda _, lbl=label: toggle_line(lbl))
    buttons.append(button)

# Botón para mostrar/ocultar todas
ax_button_all = plt.axes([0.85, 0.05, 0.1, 0.04])
button_all = Button(ax_button_all, 'Mostrar/Ocultar Todas', color='#e6f7ff', hovercolor='#ccf2ff')
button_all.on_clicked(toggle_all)

# Mostrar el gráfico
plt.tight_layout()
plt.show()


