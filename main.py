from sympy import *
import calculo_numerico as cn


x = Symbol('x')
y = Symbol('y')
z = Symbol('z')


# EJERCICIOS UNIDAD I

# ___________________
# 1) a)
"""
f = sympify("E**x+x**2-4")
alpha1 = cn.newton_raphson(func=f, start=1, accu=5)
alpha2 = cn.newton_raphson(f, -2, accu=5)
print("alpha1:", alpha1, "alpha2:", alpha2)
"""

# ___________________
# 1) b)
"""
f = sympify("E**x+-15*x**2")
alpha1 = cn.newton_raphson(func=f, start=1, accu=5)
alpha2 = cn.newton_raphson(f, -1, accu=5)
alpha3 = cn.newton_raphson(f, 6, accu=5)
print("alpha1:", alpha1, "alpha2:", alpha2, "alpha3:", alpha3)
"""

# ___________________
# 1) c)
"""
f = sympify("cos(x)-x/2")
alpha1 = cn.newton_raphson(func=f, start=1.5, accu=5)
print("alpha1:", alpha1)
"""

# ___________________
# 6) a)
"""
g = sympify("sqrt(3*(E**(-x)))")
alpha = cn.punto_fijo(g, 1.5, accu=5, max_iters=100)
print(alpha)
"""

# ___________________
# 6) b)
"""
g = sympify("E**(1/x)")
alpha = cn.punto_fijo(g, 2, accu=5, max_iters=100)
print(alpha)
"""

# ___________________
# 6) c)
"""
g1 = sympify("sqrt(2*cos(x))")
g2 = sympify("-sqrt(2*cos(x))")
alpha1 = cn.punto_fijo(g1, 1.5, accu=5, max_iters=100)
alpha2 = cn.punto_fijo(g2, -1.5, accu=5, max_iters=100)
print("alpha1:", alpha1, "alpha2:", alpha2)
"""

# ___________________
# 10) a)
"""
f = sympify("x**2-E**x+3")
alpha = cn.bolzano(func=f, start=0, end=10, accu=5)
print("alpha:", alpha)
"""

# ___________________
# 10) b)
"""
f = sympify("x-E**abs(x)+5")
alpha1 = cn.bolzano(f, 0, 3, accu=5)
alpha2 = cn.bolzano(f, -3, 0, accu=5)
print("alpha1:", alpha1, "alpha2:", alpha2)
"""

# ___________________
# 10) c)
"""
f = sympify("x-2**(-x)")
alpha = cn.bolzano(func=f, start=0, end=2, accu=4)
print("alpha:", alpha)
"""

# ___________________
# Ejemplo clase 8 de SEP
"""
f = sympify("x**2-7*x+6")
alpha1 = cn.bolzano(f, 0, 2, accu=5)
alpha2 = cn.bolzano(f, 4, 7, accu=5)
print("alpha1:", alpha1, "alpha2:", alpha2)
"""

# ___________________
# 12)
"""
f = sympify("tan(x)-cos(x)")
alpha = cn.bolzano(f, 0, 4, accu=5)
g_prima = sympify("tan(x)").diff(x).subs(x, alpha)
h_prima = sympify("cos(x)").diff(x).subs(x, alpha)
print(N(g_prima, 5), -1/N(h_prima, 5))  # si g' y h' son perpendiculares en alpha, el resultado debe ser igual
"""
# ______________________________________


# EJERCICIOS UNIDAD II

# ___________________
# 9) a)
"""
exp = ["(1+2*y)/5", "(15-x)/7"]
cn.systems_gauss_seidel(expressions=exp, symbols_vector=(x, y),  start_vector=(0.2, 2), accuracy=5, break_after=100)
"""

# ___________________
# 11) a)
"""
exp = ["(26+2*y-4*z)/8", "(-3-x+4*z)/7", "(48-2*x+3*y)/16"]
cn.systems_gauss_seidel(exp, (x, y, z),  (3, 0, 3), accuracy=4, break_after=100)
"""

# ___________________
# 11) b)
"""
exp = ["(2+y)/2", "(1-z)/3", "(9-3*x+y)/6"]
cn.systems_gauss_seidel(exp, (x, y, z),  (1, 1/3, 1.5), accuracy=4, break_after=100)
"""

# ___________________
# 11) c)
exp = ["(4+2*y-z)/4", "(-2-z)/4", "(9-x+y)/6"]
cn.systems_gauss_seidel(exp, (x, y, z),  (1, -0.5, 1.5), accuracy=4, break_after=100)
