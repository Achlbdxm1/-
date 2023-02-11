import numpy as np
import matplotlib.pyplot as plt 

x = np.arange(-4, 4, 0.1)#xの範囲

y1 = np.power(1, x)
y2 = np.power(2, x)
y3 = np.power(3, x)

f, ax = plt.subplots(2,2)#複数の図を組み合わせる
plt.subplot(221)
plt.plot(x, y1)
ax[0][0].set_title("f(x)=1^x")

plt.subplot(222)
plt.plot(x, y2)
ax[0][1].set_title("f(x)=2^x")

plt.subplot(223)
plt.plot(x, y3)
ax[1][0].set_title("f(x)=3^x")

plt.tight_layout()#軸とタイトルが重ならないようにする
plt.show()