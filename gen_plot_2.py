from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
import scipy.special as sci_sp

from TP2.lagrange import *
import  TP2.poly as chbp

PLOTD = Path("plots")

N_START=1
N_STOP=60
N_STEP=2
def gen_plot(f, chf, name, n, start=-1, end=1):
    X = np.linspace(start, end, 1000)
    F =  LagrangeInterpolate_cheb(f, n, start, end)

    err1 = get_errrs(X, f, F)
    err2 = get_errrs(X, f, chf)

    fig, (ax1, ax2) = plt.subplots(2, 1)

    ax1.plot(X, f(X))
    ax1.plot(X, F(X), color="orange", label="Interpolierende", linestyle="solid")
    ax1.plot(X, chf(X), color="green", label="Bestapproximierende", linestyle="dashed")
    ax1.legend()
    
    ax2.plot(X, err1, color="orange", linestyle="solid")
    ax2.plot(X, err2, color="green", linestyle="dashed")

    fig.savefig(PLOTD/(name + ".2.pdf"))

def get_errrs(X, f, F):
    return (f(X) - F(X))

gen_plot(lambda x: np.sin(np.pi/2 * x), chbp.sinpih ,"sinph", n=9)
gen_plot(np.atan, chbp.arctan, "atan", n=15)
gen_plot(lambda x: sci_sp.gamma(x+1), chbp.gammap1, "gamma", n=8,start=0, end=1)
