
import numpy as np
import matplotlib.pyplot as plt

def h(x):
    return 1.0/x + np.exp(5.0*x)


x_list = np.arange(0, 10, 0.1)
h_list = [h(x) for x in x_list]

plt.plot(x_list, h_list)
plt.show()
plt.clf()


def heart(t):

    p = 13*np.sin(t)**3
    q = 13*np.cos(t) - 5*np.cos(2*t) - 2*np.cos(3*t) - np.cos(4*t)

    return p, q

t_list = np.arange(-2*np.pi, 2*np.pi, 0.1)
x_list = []
y_list = []

for t in t_list:
    p, q = heart(t)
    x_list.append(p)
    y_list.append(q)

plt.plot(x_list, y_list)
plt.show()

