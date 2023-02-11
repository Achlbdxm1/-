from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from matplotlib import pyplot as plt
plt.rcParams['axes.unicode_minus'] = False


n = np.arange(1, 99, 1)
def us(x):
    q = 0
    for k in n:
        q += (1 / k) * np.sin(2 * k * x)#関数化する
    return q

t = np.arange(-5, 5, 0.01)
y = []
for i in t:
    y_l = np.pi / 2 - us(i)
    y.append(y_l)

plt.plot(t, y)
plt.xlabel("x")
plt.ylabel("y")
plt.show()