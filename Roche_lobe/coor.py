import numpy as np

M1 = 1.43
M2 = 0.94
q = M2/M1
theta = np.linspace(0, 3.14, 100)
phi = np.linspace(0, 6.28, 100)
tt, pp = np.meshgrid(theta, phi)

f = open('InputqThePhi.txt', 'w')

for i in range(len(phi)):
    for j in range(len(theta)):
        f.write('{:<25}{:<25}{:<25}'.format(q, tt[i, j], pp[i, j]))
        f.write('\n')
f.close()














































# end
