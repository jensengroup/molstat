import matplotlib.pyplot as plt
import numpy as np
import csv

dat_files = ['CCSD(t).dat', 'F12.dat', 'B3LYP.dat', 'mp2.dat']

energies = []
r_lists = []

for datf in dat_files:

    dat_energy = []
    r_list = []

    f = open(datf, 'r')

    for line in f:

        line = line.split()

        if len(line) < 1:
            continue

        energy = float(line[-1])
        r = float(line[0])

        dat_energy.append(energy)
        r_list.append(r)


    dat_energy = np.array(dat_energy)
    m = dat_energy.min()

    dat_energy -= m
    dat_energy *= 627.509 # a.u. to kcal/mol

    energies.append(dat_energy)
    r_lists.append(r_list)

plt.plot(r_lists[0], energies[0], '.-', label='CCSD(T)')
plt.plot(r_lists[1], energies[1], '.-', label='F12')
plt.plot(r_lists[2], energies[2], '.-', label='B3LYP')
plt.plot(r_lists[3], energies[3], '.-', label='MP2')

plt.legend(loc='upper right')

plt.xlabel('Displacement [$\AA$]')
plt.ylabel('Relative energy [kcal/mol]')

# plt.ylim((0.0, 0.2))
plt.savefig('energy_water.png')

