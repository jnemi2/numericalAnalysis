from sympy import *


x = Symbol('x')
y = Symbol('y')
z = Symbol('z')

f = sympify("x**5+x**4-17*x**2+15*x-1")
g = sympify("sqrt(3*E**(-x))")


def newton_raphson(func, start, accu, break_after=200):
    op_counter = 0
    deriv = diff(func, x)
    x0 = start
    xn = N(x0 - (func.subs(x, x0)/deriv.subs(x, x0)), accu)
    print("op:", op_counter, "valor:", xn)
    while str(xn) != str(x0):
        if op_counter >= break_after:
            print("Maximum operations exceeded!")
            break
        op_counter += 1
        x0 = xn
        xn = N(x0 - (func.subs(x, x0)/deriv.subs(x, x0)), accu)
        print("op:", op_counter, "valor:", xn)
    return xn


def punto_fijo(g, start, iters, accu=5):
    xn = start
    for i in range(iters):
        xn = N(g.subs(x, xn), accu)
        print("op:", i, "valor:", xn)
    return xn


def bolzano(func, start, end, accu=5, break_after=200):
    op_counter = 1
    a = start
    b = end
    c = None
    average = (x+y)/2
    prev_c = ''
    if N(func.subs(x, b), accu)*N(func.subs(x, a), accu) < 0:
        while c != prev_c:
            if op_counter >= break_after:
                print("Maximum operations exceeded!")
                break
            prev_c = c
            c = N(average.subs(x, a).subs(y, b), accu)
            print("op:", op_counter, "valor:", c)
            temp = N(func.subs(x, a), accu)*N(func.subs(x, c), accu)
            if temp < 0:
                b = c
            elif temp > 0:
                a = c
            else:
                break
            op_counter += 1
    else:
        print("No sign change detected between f(", start, ") and f(", end, ")")
    return c


# ___________________________________________________________________________

exp = ["(1+2*y)/-3", "(15-x)/-4"]


def systems_jacobi(expressions, symbols_vector, start_vector, accuracy=10, break_after=200):
    expressions = sympify(expressions)
    vector = list(start_vector)
    prev_vector = None
    op_counter = 0
    while prev_vector != vector:
        print("op:", op_counter, "valor:", vector)
        if op_counter >= break_after:
            print("Maximum operations exceeded!")
            break
        prev_vector = list(vector)
        for i in range(len(vector)):
            this_exp = expressions[i]
            for sym, val in zip(symbols_vector, prev_vector):
                this_exp = this_exp.subs(sym, val)
            vector[i] = N(this_exp, accuracy)
        op_counter += 1
    return vector


def systems_gauss_seidel(expressions, symbols_vector, start_vector, accuracy=10, break_after=200):
    expressions = sympify(expressions)
    vector = list(start_vector)
    prev_vector = None
    op_counter = 0
    while prev_vector != vector:
        print("op:", op_counter, "valor:", vector)
        if op_counter >= break_after:
            print("Maximum operations exceeded!")
            break
        prev_vector = list(vector)
        for i in range(len(vector)):
            this_exp = expressions[i]
            for sym, val in zip(symbols_vector, vector):
                this_exp = this_exp.subs(sym, val)
            vector[i] = N(this_exp, accuracy)
        op_counter += 1
    return vector


systems_jacobi(exp, (x, y), (0, 0), accuracy=5)
systems_gauss_seidel(exp, (x, y), (0, 0), accuracy=5)


# newton_raphson(f, 2, 8)
# punto_fijo(g, 1.5, 200, accu=20)
# bolzano(f, -2, -0.5, accu=7)
