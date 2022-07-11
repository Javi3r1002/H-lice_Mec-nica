import numpy as np
import matplotlib.pyplot as plt
import math
from mpl_toolkits.mplot3d import Axes3D
from math import pi

fig = plt.figure()
ax1 = fig.add_subplot(111, projection='3d')

R = 1
a = .5
Ang = np.arange(0,2*pi, .01)


x = []
y = []
z = []

for i in Ang:
	x.append(R*math.cos(i))
	y.append(R*math.sin(i))
	z.append(((a*R)/(np.sqrt(1-a**2)))*i)

ax1.scatter(x,y,z)
plt.show()

