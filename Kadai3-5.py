import numpy as np
import matplotlib.pyplot as plt 
import math


x = np.arange(-4, 4, 0.1) #ⅹの範囲
Range = np.arange(2.000, 4.000, 0.001) #aの範囲
optimal_base = 0
plt.ion() #インタラクティブウィンドウを開く

for base in Range:
     
    #base = input("Please input base: ")
    y1 = np.power(base, x) #y1=a^x
    y2 = math.log(base) * np.power(base, x) #y2=lna*a^x
    
    plt.plot(x, y1, color = "red")
    plt.plot(x, y2, color = "blue")
    if round(math.e, 3) == round(base, 3):#y1=y2の場合、optimal baseを記録できる
        optimal_base = round(base, 3)
    else:
        print("base =", round(base, 3), "optimal base =", optimal_base)#terminalにctrl+Cを入力して中止
    
    plt.show()
    plt.pause(0.02)
    plt.clf()