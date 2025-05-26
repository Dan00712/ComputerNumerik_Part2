import numpy as np

def L_i(X, yi, i):
    def f(x):
        acc = yi
        for k, xk in enumerate(X):
            if i == k:
                continue

            acc *= (x - xk)/(X[i] - xk)     
        return acc
    return f

def L_interpolate(X, Y):
    def f(x):
        acc = 0
        for i, (xi, yi) in enumerate(zip(X, Y)):
            acc += L_i(X, yi, i)(x)
        return acc
    return f

def LagrangeInterpolate_lin(f, N:int, start=-1, end=1):
    X = np.linspace(start, end, N)
    Y = f(X)

    return L_interpolate(X, Y)

def LagrangeInterpolate_cheb(f, N:int, start=-1, end=1):
    X = (start+end)/2 + (end -start)/2*np.cos(np.array([np.pi/N * j for j in range(N+1)]))

    Y = f(X)

    return L_interpolate(X, Y)
