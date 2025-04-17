import numpy as np
import matplotlib.pyplot as plt

# a) X(t) = e^t, Y(t) = cos(t) en t = pi/4
t_a = np.pi / 4
X_a = np.exp(t_a)
Y_a = np.cos(t_a)

# Derivadas
X_a_prime = np.exp(t_a)
Y_a_prime = -np.sin(t_a)

# Pendiente de la tangente
m_a = Y_a_prime / X_a_prime

# Ecuación de la tangente
def tangent_a(x):
    return m_a * (x - X_a) + Y_a

# Gráfica
t_vals = np.linspace(0, 2, 100)
X_vals_a = np.exp(t_vals)
Y_vals_a = np.cos(t_vals)
plt.figure(figsize=(10, 6))
plt.plot(X_vals_a, Y_vals_a, label='Curva: X(t) = e^t, Y(t) = cos(t)')
plt.plot(X_vals_a, tangent_a(X_vals_a), label='Tangente', linestyle='--')
plt.scatter([X_a], [Y_a], color='red')  # Punto de tangencia
plt.text(X_a, Y_a, f'({X_a:.2f}, {Y_a:.2f})', fontsize=12, verticalalignment='bottom')
plt.title('Gráfica de la curva y la tangente a(t)')
plt.xlabel('X')
plt.ylabel('Y')
plt.axhline(0, color='black',linewidth=0.5, ls='--')
plt.axvline(0, color='black',linewidth=0.5, ls='--')
plt.grid()
plt.legend()
plt.show()

# b) X(t) = 3t^2, Y(t) = t^3 en t = 2
t_b = 2
X_b = 3 * t_b**2
Y_b = t_b**3

# Derivadas
X_b_prime = 6 * t_b
Y_b_prime = 3 * t_b**2

# Pendiente de la tangente
m_b = Y_b_prime / X_b_prime

# Ecuación de la tangente
def tangent_b(x):
    return m_b * (x - X_b) + Y_b

# Gráfica
t_vals_b = np.linspace(0, 3, 100)
X_vals_b = 3 * t_vals_b**2
Y_vals_b = t_vals_b**3
plt.figure(figsize=(10, 6))
plt.plot(X_vals_b, Y_vals_b, label='Curva: X(t) = 3t^2, Y(t) = t^3')
plt.plot(X_vals_b, tangent_b(X_vals_b), label='Tangente', linestyle='--')
plt.scatter([X_b], [Y_b], color='red')  # Punto de tangencia
plt.text(X_b, Y_b, f'({X_b}, {Y_b})', fontsize=12, verticalalignment='bottom')
plt.title('Gráfica de la curva y la tangente b(t)')
plt.xlabel('X')
plt.ylabel('Y')
plt.axhline(0, color='black',linewidth=0.5, ls='--')
plt.axvline(0, color='black',linewidth=0.5, ls='--')
plt.grid()
plt.legend()
plt.show()

# c) X(t) = t*sin(t), Y(t) = 4t en t = pi/2
t_c = np.pi / 2
X_c = t_c * np.sin(t_c)
Y_c = 4 * t_c

# Derivadas
X_c_prime = np.sin(t_c) + t_c * np.cos(t_c)
Y_c_prime = 4

# Pendiente de la tangente
m_c = Y_c_prime / X_c_prime

# Ecuación de la tangente
def tangent_c(x):
    return m_c * (x - X_c) + Y_c

# Gráfica
t_vals_c = np.linspace(0, 3, 100)
X_vals_c = t_vals_c * np.sin(t_vals_c)
Y_vals_c = 4 * t_vals_c
plt.figure(figsize=(10, 6))
plt.plot(X_vals_c, Y_vals_c, label='Curva: X(t) = t*sin(t), Y(t) = 4t')
plt.plot(X_vals_c, tangent_c(X_vals_c), label='Tangente', linestyle='--')
plt.scatter([X_c], [Y_c], color='red')  # Punto de tangencia
plt.text(X_c, Y_c, f'({X_c:.2f}, {Y_c:.2f})', fontsize=12, verticalalignment='bottom')
plt.title('Gráfica de la curva y la tangente c(t)')
plt.xlabel('X')
plt.ylabel('Y')
plt.axhline(0, color='black',linewidth=0.5, ls='--')
plt.axvline(0, color='black',linewidth=0.5, ls='--')
plt.grid()
plt.legend()
plt.show()

# d) X(t) = t^2, Y(t) = e^t en t = 1
t_d = 1
X_d = t_d**2
Y_d = np.exp(t_d)

# Derivadas
X_d_prime = 2 * t_d
Y_d_prime = np.exp(t_d)

# Pendiente de la tangente
m_d = Y_d_prime / X_d_prime

# Ecuación de la tangente
def tangent_d(x):
    return m_d * (x - X_d) + Y_d

# Gráfica
t_vals_d = np.linspace(0, 2, 100)
X_vals_d = t_vals_d**2
Y_vals_d = np.exp(t_vals_d)
plt.figure(figsize=(10, 6))
plt.plot(X_vals_d, Y_vals_d, label='Curva: X(t) = t^2, Y(t) = e^t')
plt.plot(X_vals_d, tangent_d(X_vals_d), label='Tangente', linestyle='--')
plt.scatter([X_d], [Y_d], color='red')  # Punto de tangencia
plt.text(X_d, Y_d, f'({X_d:.2f}, {Y_d:.2f})', fontsize=12, verticalalignment='bottom')
plt.title('Gráfica de la curva y la tangente d(t)')
plt.xlabel('X')
plt.ylabel('Y')
plt.axhline(0, color='black',linewidth=0.5, ls='--')
plt.axvline(0, color='black',linewidth=0.5, ls='--')
plt.grid()
plt.legend()
plt.show()