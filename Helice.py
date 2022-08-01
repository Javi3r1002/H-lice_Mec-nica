import numpy as np
import matplotlib.pyplot as plt
import math
from mpl_toolkits.mplot3d import Axes3D
from math import pi

fig = plt.figure()
#ax1 = fig.add_subplot(111, projection='3d')
ax1 = fig.add_subplot(111)

R = 1
a = .5
Ang = np.arange(0,10*pi, .001)


x = []
y = []
z = []

for i in Ang:
	x.append(R*math.cos(i))
	y.append(R*math.sin(i))
	z.append(((a*R)/(np.sqrt(1-a**2)))*i)

#ax1.scatter(x,y,z)
ax1.set_xlabel('Ángulo', fontsize = 15)
ax1.set_ylabel('Áltura', fontsize = 15)
#ax1.set_zlabel('z', fontsize = 15)
ax1.scatter(Ang,z)
plt.show()

