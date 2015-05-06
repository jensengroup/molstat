
import numpy as np
import matplotlib.pyplot as plt


def read_file(filename):
    """
    """

    f = open(filename, 'r')

    data = []

    for line in f:

        line = line.split(',')


        line[0] = int(line[0])
        line[1] = float(line[1])
        line[2] = float(line[2])

        data.append(line)

    return data



sim_data = read_file('simulation_energy')

step = []
e_pot = []
e_kin = []
e_tot = []

for data in sim_data:

    step.append(data[0])
    e_pot.append(data[1])
    e_kin.append(data[2])
    e_tot.append(data[1] + data[2])


plt.plot(step, e_pot, label='Potential')
plt.plot(step, e_kin, label='Kinetic')
plt.plot(step, e_tot, label='Total')

plt.xlabel('Step')
plt.ylabel('Energy')

plt.savefig('week3_energy')

