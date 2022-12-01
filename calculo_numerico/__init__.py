import sympy


def newton_raphson(func, start, accu=5, break_after=200):
    op_counter = 0
    x = sympy.Symbol("x")
    deriv = sympy.diff(func, x)
    x0 = start
    xn = sympy.N(x0 - (func.subs(x, x0)/deriv.subs(x, x0)), accu)
    print("op:", op_counter, "valor:", xn)
    while str(xn) != str(x0):
        if op_counter >= break_after:
            print("Maximum operations exceeded!")
            break
        op_counter += 1
        x0 = xn
        xn = sympy.N(x0 - (func.subs(x, x0)/deriv.subs(x, x0)), accu)
        print("op:", op_counter, "valor:", xn)
    return xn


def punto_fijo(g, start, accu=5, max_iters=200):
    x = sympy.Symbol("x")
    xn = start
    prev = None
    for i in range(max_iters):
        xn = sympy.N(g.subs(x, xn), accu)
        print("op:", i, "valor:", xn)
        if str(xn) == str(prev):
            break
        prev = xn
    return xn


def bolzano(func, start, end, accu=5, break_after=200):
    x = sympy.Symbol("x")
    y = sympy.Symbol("y")
    op_counter = 1
    a = start
    b = end
    c = None
    average = (x+y)/2
    prev_c = ''
    if sympy.N(func.subs(x, b), accu)*sympy.N(func.subs(x, a), accu) < 0:
        while c != prev_c:
            if op_counter >= break_after:
                print("Maximum operations exceeded!")
                break
            prev_c = c
            c = sympy.N(average.subs(x, a).subs(y, b), accu)
            print("op:", op_counter, "valor:", c)
            temp = sympy.N(func.subs(x, a), accu)*sympy.N(func.subs(x, c), accu)
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


# ____________________________


def systems_jacobi(expressions, symbols_vector, start_vector, accuracy=10, break_after=200):
    expressions = sympy.sympify(expressions)
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
            vector[i] = sympy.N(this_exp, accuracy)
        op_counter += 1
    return vector


def systems_gauss_seidel(expressions, symbols_vector, start_vector, accu=10, break_after=200):
    expressions = sympy.sympify(expressions)
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
            vector[i] = sympy.N(this_exp, accu)
        op_counter += 1
    return vector


# ____________________________


def trapecios(func, start, end, h, accu=10):
    x = sympy.Symbol('x')
    integral = sympy.N(func.subs(x, start), accu) + sympy.N(func.subs(x, end), accu)
    integral = h * integral / 2
    for i in range(1, int((end - start) / h)):
        integral += h * sympy.N(func.subs(x, (i*h + start)), accu)
    return integral


def simpson(func, start, end, h, accu=10):
    x = sympy.Symbol('x')
    integral = sympy.N(func.subs(x, start), accu) + sympy.N(func.subs(x, end), accu)
    for i in range(1, int((end - start) / h)):
        temp = sympy.N(func.subs(x, (i*h + start)), accu)
        if i % 2 == 0:
            integral += 2 * temp
        else:
            integral += 4 * temp
    return integral * h / 3

# ____________________________


def euler(fun, xini, vinit, paso, vtp):
    x = sympy.Symbol('x')
    y = sympy.Symbol('y')
    wn = vinit
    i = xini
    while i < vtp:
        wn = wn + paso * fun.subs({x: i, y: wn})
        i += paso
        print(f"{wn}")


def taylor(fun, xini, vinit, paso, vtp):
    x = sympy.Symbol('x')
    y = sympy.Symbol('y')
    wn = vinit
    i = xini
    contador = 0
    while i < (vtp-paso):
        wn = wn + fun.subs({x: i, y: wn}) * paso + (1/2) * (sympy.diff(fun, x).subs({x: i, y: wn})
                                                            + sympy.diff(fun, y).subs({x: i, y: wn})
                                                            * fun.subs({x: i, y: wn})) * (paso**2)
        i += paso
        contador += 1
        print(f"w{contador} = {wn}")