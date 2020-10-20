import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np

# no acceleration : angular speed remains constant
# no initial angle : 0

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def determine_T(w):
    gcd_w = 0
    for elt in w:
        gcd_w = gcd(gcd_w, elt)
    nb_of_c0_revolutions = w[0] // gcd_w
    return nb_of_c0_revolutions * 2 * np.pi / w[0]

def position(k, r, w, t):
    z = 0
    for i in range(k):
        z += r[i] * (np.cos(w[i] * t) + 1j * np.sin(w[i] * t))
    return z

def full_path_graph(k, r, w, N):
    """Paramaters : k (studied point index), r (radius list),
    w (angular velocity list), N (nb of calculated points), filename
    """

    T = determine_T(w)
    t = 0
    dt = T / N
    xdata, ydata = [], []

    while t <= T:
        z = position(k, r, w, t)
        xdata.append(z.real)
        ydata.append(z.imag)
        t += dt
    plt.plot(xdata, ydata)
    plt.axis("equal")
    plt.savefig("graphs/dynamic_circles__" + "_".join(list(map(str, r))) + "__" + "_".join(list(map(str, w))))

def animated_graph_over_time(k, r, w, N):
    """Paramaters : k (studied point index), r (radius list),
    w (angular velocity list), N (nb of calculated points)
    """
    fig, ax = plt.subplots()
    xdata, ydata = [], []
    ln, = plt.plot([], [])

    def init():
        ax.set_xlim(- sum(r), sum(r))
        ax.set_ylim(- sum(r), sum(r))
        return ln, 

    def update(frame):
        z = position(k, r, w, frame)
        xdata.append(z.real)
        ydata.append(z.imag)
        ln.set_data(xdata, ydata)
        return ln,

    T = determine_T(w)
    ani = animation.FuncAnimation(fig, update, frames=np.linspace(0, T, N), init_func=init)
    plt.show()

r = [1, 5]
w = [7, 9]
N = 1000
full_path_graph(len(r), r, w, N)
