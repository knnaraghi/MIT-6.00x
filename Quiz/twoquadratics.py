def evalQuadratic(a, b, c, x):
    return a * (x ** 2) + b * x + c

a1 = 4.54
b1 = 9.85
c1 = -5.54
x1 = -0.82
a2 = 4.36
b2 = -7.23
c2 = 0.66
x2 = -3.7

def twoQuadratics(a1, b1, c1, x1, a2, b2, c2, x2):
    '''
    a1, b1, c1: one set of coefficients of a quadratic equation
    a2, b2, c2: another set of coefficients of a quadratic equation
    x1, x2: values at which to evaluate the quadratics
    '''
    print evalQuadratic(a1, b1, c1, x1) + evalQuadratic(a2, b2, c2, x2)
