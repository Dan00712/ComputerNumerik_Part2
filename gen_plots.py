import matplotlib.pyplot as plt
from TP2.lagrange import *
import TP2.poly as chp
import numpy as np
import scipy.special as sci_sp

def generate_plot(f, c_poly, N, fname, start=0, end=1, cheberchev=True):
    #calculate reference data
    X = np.linspace(start, end, N)
    Yint = f(X)

    # for cheberchev nodes
    X_c = np.array([np.pi/N * j for j in range(N)])
    Y_c  = f(X_c)

    # generate lagrange polynomial
    F  = L_interpolate(X, Yint)
    F2 = L_interpolate(X_c, Y_c) 

    # higher resolution for plot
    Xc = np.linspace(start, end, N)

    # calc test polynomials
    Yref = f(Xc)
    Ylap = F(Xc)
    Ylap2 = F2(Xc)
    Y_cheb = c_poly(Xc)

    fig, (ax1, ax2) = plt.subplots(2,1)

    ax1.set_ylabel("$\sin(\pi/2 \cdot x)$")
    ax1.scatter(Xc, Yref)
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
    plt.savefig(fname)


generate_plot(
    lambda x: np.sin(np.pi/2 *x),
    chp.sinpih,
    13,
    "plots/sinpi.pdf"
)
generate_plot(
    np.arctan,
    chp.arctan,
    15,
    "plots/arctan.pdf",
    cheberchev=False
)
generate_plot(
    lambda x: sci_sp.gamma(x+1),
    chp.gammap1,
    15,
    "plots/gamma.pdf"
)
