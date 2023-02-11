import matplotlib.pyplot as plt
import numpy as np 

x = np.arange(-4, 4, 0.1)#xの範囲

y1 = x
y2 = x * x
y3 = x * x * x

f, ax = plt.subplots(2,2)#複数の図を組み合わせる

plt.subplot(221)
plt.plot(x, y1)
ax[0][0].set_title("f(x)=x")

plt.subplot(222)
plt.plot(x, y2)
ax[0][1].set_title("f(x)=x^2")

plt.subplot(223)
plt.plot(x, y3)
ax[1][0].set_title("f(x)=x^3")

plt.tight_layout()#軸とタイトルが重ならないようにする
plt.show()