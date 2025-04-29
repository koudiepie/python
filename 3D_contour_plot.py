import numpy as np
import matplotlib.pyplot as plt
fig = plt.figure()
ax = plt.axes(projection="3d")
#def z_function(x, y):
    #return np.sin(np.sqrt(x ** 2 + y ** 2))

theta = np.linspace(0, np.pi/2, 30)
phi = np.linspace(0, 2*np.pi, 60)
theta, phi = np.meshgrid(theta, phi)

r=100

X = r * np.cos(theta) * np.cos(phi)
Y = r * np.cos(theta) * np.sin(phi)
Z = r * np.sin(theta)

#x = np.linspace(-6, 6, 30)
#y = np.linspace(-6, 6, 30)
#X, Y = np.meshgrid(x, y)
#Z = z_function(X, Y)

ax.plot_wireframe(X, Y, Z, color='green')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.show()