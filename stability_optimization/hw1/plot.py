import numpy as np
import matplotlib.pyplot as plt

def mih_even(w):
    return -w**2 - 1.j * w - 1/4
def mih_odd(w):
    return -w**2 + 1.j * w + 1/4


w_range = np.linspace(0, 1, int(10**3))
even_data = np.vectorize(mih_even)(w_range)
odd_data = np.vectorize(mih_odd)(w_range)
plt.plot(np.real(even_data), np.imag(even_data), label=r"$k = 2n$")
plt.plot(np.real(odd_data), np.imag(odd_data), label=r"$k = 2n+1$")
plt.scatter([0], [0], label='Начало координат')
plt.xlabel(r"Re $\arg D(i\omega)$")
plt.ylabel(r"Im $\arg D(i\omega)$")
plt.grid()
plt.legend()
plt.show()
