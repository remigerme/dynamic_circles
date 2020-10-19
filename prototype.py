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

r = [5, 3, 3]
w = [2, 3, 4]
N = 1000

T = determine_T(w)
t = 0
dt = T / N

absc = []
ords = []

while t <= T:
    z = position(len(r), r, w, t)
    absc.append(z.real)
    ords.append(z.imag)
    t += dt

plt.scatter(absc, ords, s = 1)
plt.axis("equal")
plt.savefig("My great figure")
