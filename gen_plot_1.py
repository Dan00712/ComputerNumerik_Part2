from pathlib import Path
import matplotlib.pyplot as plt
from TP2.lagrange import *
import numpy as np
import scipy.special as sci_sp

PLOTD = Path("plots")

N_START=1
N_STOP=60
N_STEP=2
def generate_plots(f, name, start=-1, end=1):
    print(name)
    N = list(range(N_START, N_STOP, N_STEP))
    err1 = [get_max_error(f, LagrangeInterpolate_lin(f, n, start, end), start, end)
        for n in N]
    err2 = [get_max_error(f, LagrangeInterpolate_cheb(f, n, start, end), start, end)
        for n in N]

    fig, ax = plt.subplots()

    print(err2)
    ax.set_yscale('log')
    ax.set_ylabel('maximaler Relativer Fehler')
    ax.set_xlabel('Interpolationsgrad')
    ax.plot(N, err1,
            label="Lineare Punkte",
            linestyle="solid"
            )
    ax.plot(N, err2,
            label="Chebychev Knoten",
            linestyle="dashed"
            )
    ax.legend()
    fig.savefig(PLOTD/(name+".1.pdf"))


def get_max_error(f, f1, start=-1, end=1):
    X = np.linspace(start, end, 10_000)
    Y = f(X)
    Y1 = f1(X)

    return abs((Y-Y1)/Y1).max()

generate_plots(lambda x: np.sin(np.pi/2 * x), "sinph")
generate_plots(np.atan, "atan")
generate_plots(lambda x: sci_sp.gamma(x+1), "gamma", start=0, end=1)


