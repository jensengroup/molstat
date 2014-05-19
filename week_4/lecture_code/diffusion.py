import numpy as np
import matplotlib.pyplot as plt

dl = 0.15 # change in position
n_steps = 10000
n_particles = 80000
n_particles = 40000

box_width = 10.0

pos_x = np.zeros(n_particles)
pos_y = np.zeros(n_particles)

d_list = []
t_list = []

for n in range(n_steps):

    pos_x += np.random.uniform(-dl, dl, n_particles)
    pos_y += np.random.uniform(-dl, dl, n_particles)

    if n % 1 == 0:

        # deviation from starting point (0.0, 0.0)
        # sqrt((x1-0.0)**2 + (y1-0.0)**2)
        r = np.sqrt(pos_x**2 + pos_y**2)

        # std for the particles from origin
        sigma = r.std()

        D = sigma**2/(2*n)

        print n, D

        d_list.append(D)
        t_list.append(n)


plt.plot(t_list, d_list)
plt.ylim((0.0010, 0.0020))
plt.savefig("diffusion.png")


# Questions:
# How do i find the minimum D?
# and the corresponding n-step?


