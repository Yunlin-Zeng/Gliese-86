import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

theta = np.linspace(0, 3.14, 100)
phi = np.linspace(0, 6.28, 100)
tt, pp = np.meshgrid(theta, phi)

# load the results of radius of Roche lobe at every direction
R = np.loadtxt('qThePhiR.txt', usecols=3, unpack=True)
rr = np.zeros([len(phi), len(theta)])
for i in range(len(R)):
    rr[i//len(theta), i%len(theta)] = R[i]

# express the mesh in the Cartesian coordinates
x, y, z = rr*np.sin(tt)*np.sin(pp), rr*np.sin(tt)*np.cos(pp), rr*np.cos(tt)

# Plot the surface.
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(x, y, z, cmap=plt.cm.YlGnBu_r)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

plt.show()
