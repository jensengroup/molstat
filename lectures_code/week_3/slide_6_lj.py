
# Example: LJ Energy

# Douple loop

import numpy as np

def distance(xi, yi, xj, yj):
    return np.sqrt((xj-xi)**2 + (yj-yi)**2)


def lennard_jones(pos_x, pos_y, n_particles):

    energy = 0.0

    for i in range(n_particles):
        for j in range(n_particles):
            if i > j:

                rij = distance(pos_x[i], pos_y[i], pos_x[j], pos_y[i])
                energy += 4*(1.0/rij**12 - 1.0/rij**6)

    return energy


n_particles = 3

X = [1.0, 3.0, 6.0]
Y = [0.0, 0.0, 0.0]

print lennard_jones(X, Y, n_particles)

