
import numpy as np
import matplotlib.pyplot as plt

def read_list(filename):
    """
    """
    f = open(filename, 'r')
    list = []

    for line in f:
        list.append(int(line))

    return list


n_particles = 40


# plot the partdist list
partdist = read_list('test_list')

plt.title('Particle Count for X > 0.0 and N < 10000')
plt.xlabel('Number of particles where X > 0.0')
plt.ylabel('Count')
plt.hist(partdist, bins=range(0, n_particles), align='left')
plt.xlim( (0, n_particles) )
plt.savefig('partdist.png')
plt.clf()


# plot the partdisteq list
partdisteq = read_list('test_list_eq')

plt.title('Particle Count for X > 0.0 and N > 10000')
plt.xlabel('Number of particles where X > 0.0')
plt.ylabel('Count')
plt.hist(partdisteq, bins=range(0, n_particles), rwidth=1, align='left')
plt.xlim( (0, n_particles) )
plt.savefig('partdisteq.png')
plt.clf()

