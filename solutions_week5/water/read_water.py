import matplotlib.pyplot as plt
import numpy as np
import seaborn

# If working with multiple files
# you can read loop over the files by creating a array of
# filenames
dat_files = ['CCSD(t).dat', 'F12.dat', 'B3LYP.dat', 'mp2.dat']

# initialize empty lists
energies = []
r_lists = []

# for data-file in file-list
for datf in dat_files:

    # initialize empty list for current
    # data file
    dat_energy = []
    r_list = []

    # open datafile and loop over lines
    f = open(datf, 'r')
    for line in f:

        # split line (string) into a line (list) for every space
        line = line.split()

        # Check if line is empty by checking the length of the line list
        if len(line) < 1:
            continue

        # Get the energy and distance
        # and convert it to float from string
        energy = float(line[-1])
        r = float(line[0])

        # append it to energies
        dat_energy.append(energy)
        r_list.append(r)


    dat_energy = np.array(dat_energy)
    m = dat_energy.min()

    dat_energy -= m
    dat_energy *= 627.509 # a.u. to kcal/mol

    # append energy list to overall energy array
    energies.append(dat_energy)
    r_lists.append(r_list)


# energies is now a "list of lists"
# which we can access as

plt.plot(r_lists[0], energies[0], '.-', label='CCSD(T)')
plt.plot(r_lists[1], energies[1], '.-', label='F12')
plt.plot(r_lists[2], energies[2], '.-', label='B3LYP')
plt.plot(r_lists[3], energies[3], '.-', label='MP2')

plt.legend(loc='upper right')

plt.xlabel('Displacement [$\AA$]')
plt.ylabel('Relative energy [kcal/mol]')

plt.savefig('energy_water.png')

