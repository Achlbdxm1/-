import sympy
import numpy as np

x = sympy.symbols('x')
fx1 = sympy.sin(x)
fx2 = sympy.cos(x)
fx3 = sympy.exp(x)

taylor_expansion_1 = fx1.series(x, 0, 17)
taylor_expansion_2 = fx2.series(x, 0, 16)
taylor_expansion_3 = fx3.series(x, 0, 18)

print("sin(x)テイラー展開: ", taylor_expansion_1)
print("cos(x)テイラー展開: ", taylor_expansion_2)
print("e^xテイラー展開: ", taylor_expansion_3)

