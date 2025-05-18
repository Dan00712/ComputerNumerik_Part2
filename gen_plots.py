from pathlib import Path
import matplotlib.pyplot as plt
from TP2.lagrange import *
import TP2.poly as chp
import numpy as np
import scipy.special as sci_sp

def generate_plot(f, c_poly, N, fname, ylabel="", start=-1, end=1, cheberchev=True):
    #calculate reference data
    X = np.linspace(start, end, N)
    Yint = f(X)

    # for cheberchev nodes
    X_c = (start+end)/2 + (end -start)/2*np.cos(np.array([np.pi/N * j for j in range(N+1)]))
    Y_c  = f(X_c)

    # generate lagrange polynomial
    F  = L_interpolate(X, Yint)
    F2 = L_interpolate(X_c, Y_c) 

    # higher resolution for plot
    Xc = np.linspace(start, end, N*10)

    # calc test polynomials
    Yref = f(Xc)
    Ylap = F(Xc)
    Ylap2 = F2(Xc)
    Y_cheb = c_poly(Xc)

    fig, (ax1, ax2) = plt.subplots(2,1, figsize=(10, 6))

    ax1.set_ylabel(ylabel)
    ax1.scatter(X, Yint, label="Lineare Punkte")
    ax1.scatter(X_c, Y_c, label="Cheberchev Knoten")
    ax1.legend()
    ax1.plot(Xc, Ylap, label="Lagrange Interpolation")
    ax1.plot(Xc, Ylap2, label="Lagrange Interpolation | Cheberchev Knoten")
    if cheberchev:
        ax1.plot(Xc, Y_cheb, label="Cheberchev Polynome")

    ax2.set_xlabel("$x$")
    ax2.set_ylabel("relative error")
    ax2.plot(Xc, (Yref - Ylap)/Yref, label="Lagrange Interpolation")
    ax2.plot(Xc, (Yref -Ylap2)/Yref, label="Lagrange Interpolation | Cheberchev Knoten")
    if cheberchev:
        ax2.plot(Xc, (Yref - Y_cheb)/Yref, label="Cheberchev Polynome")

    ax1.legend()
    print(fname)
    plt.savefig(Path('plots/')/(fname+'.pdf'))
    with (Path('data/')/(fname+'.csv')).open('w') as f:
        print(r'Interpolation Method, $||\Delta y_i||_{\infty}$', file=f)
        print(f'Lagrange, {((Yref -Ylap)/Yref).max()}', file=f)
        print(f'Lagrange (Tcheberchev Knoten), {((Yref -Ylap2)/Yref).max()}', file=f)
        print(f'Chebychev Polynome, {((Yref -Y_cheb)/Yref).max()}', file=f)


generate_plot(
    lambda x: np.sin(np.pi/2 *x),
    chp.sinpih,
    13,
    "sinpi",
    r"$sin(\pi/2 \cdot x )$"
)
generate_plot(
    np.arctan,
    chp.arctan,
    15,
    "arctan",
    r"$arctan(x)$"
)
generate_plot(
    lambda x: sci_sp.gamma(x+1),
    chp.gammap1,
    15,
    "gamma",
    r"$\Gamma(x+1) = x!$",
    start=0,
    end=1
)
