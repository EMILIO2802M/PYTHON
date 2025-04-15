import numpy as np
import matplotlib.pyplot as plt

# Definir una función para aproximar la longitud de arco utilizando la suma de trapecios
def longitud_arco(x, y, z, t):
    dx = np.gradient(x, t)
    dy = np.gradient(y, t)
    dz = np.gradient(z, t)
    integrand = np.sqrt(dx**2 + dy**2 + dz**2)
    return np.trapz(integrand, t)

# Definir los puntos de la curva para cada caso

# a) (2cos(t), 2sin(t), t)
t_vals_a = np.linspace(0, 2 * np.pi, 400)
x_a = 2 * np.cos(t_vals_a)
y_a = 2 * np.sin(t_vals_a)
z_a = t_vals_a
L_a = longitud_arco(x_a, y_a, z_a, t_vals_a)

# b) (1, 3t^2, t^3)
t_vals_b = np.linspace(0, 1, 400)
x_b = np.ones_like(t_vals_b)
y_b = 3 * t_vals_b**2
z_b = t_vals_b**3
L_b = longitud_arco(x_b, y_b, z_b, t_vals_b)

# c) (sin(3t), cos(3t), 2t^(3/2))
t_vals_c = np.linspace(0, 1, 400)
x_c = np.sin(3 * t_vals_c)
y_c = np.cos(3 * t_vals_c)
z_c = 2 * t_vals_c**(3/2)
L_c = longitud_arco(x_c, y_c, z_c, t_vals_c)

# d) (t, t, t^2)
t_vals_d = np.linspace(1, 2, 400)
x_d = t_vals_d
y_d = t_vals_d
z_d = t_vals_d**2
L_d = longitud_arco(x_d, y_d, z_d, t_vals_d)

# e) (t, t*sin(t), t*cos(t))
t_vals_e = np.linspace(0, np.pi, 400)
x_e = t_vals_e
y_e = t_vals_e * np.sin(t_vals_e)
z_e = t_vals_e * np.cos(t_vals_e)
L_e = longitud_arco(x_e, y_e, z_e, t_vals_e)

# Mostrar las longitudes de arco
print(f"Longitud de arco a): {L_a:.2f}")  # Debería dar aproximadamente 17.7
print(f"Longitud de arco b): {L_b:.2f}")  # Debería dar aproximadamente 16.7
print(f"Longitud de arco c): {L_c:.2f}")
print(f"Longitud de arco d): {L_d:.2f}")
print(f"Longitud de arco e): {L_e:.2f}")

# Graficar cada curva
fig = plt.figure(figsize=(16, 12))

# a) (2cos(t), 2sin(t), t)
ax1 = fig.add_subplot(231, projection='3d')
ax1.plot(x_a, y_a, z_a, color='b')
ax1.set_title('a) (2cos(t), 2sin(t), t)', pad=25)  # Ajustar la posición del título
ax1.set_xlabel('X', fontsize=12)
ax1.set_ylabel('Y', fontsize=12)
ax1.set_zlabel('Z', fontsize=12)

# b) (1, 3t^2, t^3)
ax2 = fig.add_subplot(232, projection='3d')
ax2.plot(x_b, y_b, z_b, color='g')
ax2.set_title('b) (1, 3t^2, t^3)', pad=25)  # Ajustar la posición del título
ax2.set_xlabel('X', fontsize=12)
ax2.set_ylabel('Y', fontsize=12)
ax2.set_zlabel('Z', fontsize=12)

# c) (sin(3t), cos(3t), 2t^(3/2))
ax3 = fig.add_subplot(233, projection='3d')
ax3.plot(x_c, y_c, z_c, color='r')
ax3.set_title('c) (sin(3t), cos(3t), 2t^(3/2))', pad=25)  # Ajustar la posición del título
ax3.set_xlabel('X', fontsize=12)
ax3.set_ylabel('Y', fontsize=12)
ax3.set_zlabel('Z', fontsize=12)

# d) (t, t, t^2)
ax4 = fig.add_subplot(234, projection='3d')
ax4.plot(x_d, y_d, z_d, color='purple')
ax4.set_title('d) (t, t, t^2)', pad=25)  # Ajustar la posición del título
ax4.set_xlabel('X', fontsize=12)
ax4.set_ylabel('Y', fontsize=12)
ax4.set_zlabel('Z', fontsize=12)

# e) (t, t*sin(t), t*cos(t))
ax5 = fig.add_subplot(235, projection='3d')
ax5.plot(x_e, y_e, z_e, color='orange')
ax5.set_title('e) (t, t*sin(t), t*cos(t))', pad=25)  # Ajustar la posición del título
ax5.set_xlabel('X', fontsize=12)
ax5.set_ylabel('Y', fontsize=12)
ax5.set_zlabel('Z', fontsize=12)

plt.subplots_adjust(wspace=0.4, hspace=0.4)  # Ajustar el espacio entre subgráficas
plt.show()


