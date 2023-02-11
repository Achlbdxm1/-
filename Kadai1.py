from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from matplotlib import pyplot as plt
plt.rcParams['axes.unicode_minus'] = False

t = np.arange(-5, 5, 0.01)
y1 = []
for i in t:
    y_l = np.sin(np.pi * i)
    y1.append(y_l)

y2 = []
for i in t:
    y_2 = np.cos(np.pi / 2 + 2 * i)
    y2.append(y_2)

y3 = []
for i in t:
    y_3 = 1 - np.sin(i)
    y3.append(y_3)

y4 = []
for i in t:
    y_4 = np.cos(np.pi * i)
    y4.append(y_4)

y5 = []
for i in t:
    y_5 = np.sin(np.pi / 2 + 2 * i)
    y5.append(y_5)

fig, ax= plt.subplots(3,2)
plt.subplot(321)
plt.plot(t, y1)
ax[0][0].set_title("x(t)=sin(Πt)")

plt.subplot(322)
plt.plot(t, y2)
ax[0][1].set_title("x(t)=cos(2t+Π/2)")

plt.subplot(323)
plt.plot(t, y3)
ax[1][0].set_title("x(t)=1-sin(t)")

plt.subplot(324)
plt.plot(t, y4)
ax[1][1].set_title("x(t)=cos(Πt)")

plt.subplot(325)
plt.plot(t, y5)
ax[2][0].set_title("x(t)=sin(2t+Π/2)")

#plt.xlabel("x")
#plt.ylabel("y")
plt.tight_layout()
plt.show()