import sympy

x = sympy.symbols('x')
fx = sympy.sin(x)
taylor_expansion = fx.series(x, 0, 10)

print(taylor_expansion)


