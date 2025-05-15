

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

