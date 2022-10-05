from sympy import *


x = Symbol('x')
y = Symbol('y')
z = Symbol('z')

exp = ["(1+2*y)/-3", "(15-x)/-4"]


def systems_jacobi(expressions, symbols_vector, start_vector, accuracy=10, break_after=200):
    expressions = sympify(expressions)
    vector = list(start_vector)
    prev_vector = None
    operation_counter = 0
    while prev_vector != vector:
        print(operation_counter, vector)
        if operation_counter >= break_after:
            print("Maximum operations exceeded!")
            break
        prev_vector = list(vector)
        for i in range(len(vector)):
            this_exp = expressions[i]
            for sym, val in zip(symbols_vector, list(prev_vector)):
                this_exp = this_exp.subs(sym, val)
            vector[i] = N(this_exp, accuracy)
        operation_counter += 1
    return vector


def systems_gauss_seidel(expressions, symbols_vector, start_vector, accuracy=10, break_after=200):
    expressions = sympify(expressions)
    vector = list(start_vector)
    prev_vector = None
    operation_counter = 0
    while prev_vector != vector:
        print(operation_counter, vector)
        if operation_counter >= break_after:
            print("Maximum operations exceeded!")
            break
        prev_vector = list(vector)
        for i in range(len(vector) - 1):
            this_exp = expressions[i]
            for sym, val in zip(symbols_vector, prev_vector):
                this_exp = this_exp.subs(sym, val)
            vector[i] = N(this_exp, accuracy)
        this_exp = expressions[len(vector) - 1]
        for i in range(len(vector) - 1):
            this_exp = this_exp.subs(symbols_vector[i], vector[i])
        vector[len(vector) - 1] = N(this_exp, accuracy)
        operation_counter += 1
    return vector


systems_jacobi(exp, (x, y), (0, 0), accuracy=5)
systems_gauss_seidel(exp, (x, y), (0, 0), accuracy=5)
