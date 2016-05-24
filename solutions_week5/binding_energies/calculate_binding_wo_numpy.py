
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
import seaborn

def rmsd(x, y):
    n = len(x)
    d = []
    for i in range(n):
        d.append((x[i] - y[i])**2)

    return np.sqrt(np.sum(d)/n)



# get experimental data
dGexp = []

f = open('experimental.csv')
for line in f:

    line = line.split(',') # argument ',' is what the string will be split on

    dG = float(line[1])
    dGexp.append(dG)


# get calculated data

dGcal = []

delta = -5.83 # constant

f = open('calculated_new.csv')
for line in f:

    line = line.split()
    dU = float(line[1])
    dW = float(line[2])
    dS = float(line[3])

    dG = dU + dW - 298.0*dS + delta

    dGcal.append(dG)

# Make the plot
# plot experimental vs calculated
plt.plot(dGexp, dGcal, 'k.')

# set labels
plt.xlabel('Experimental [kcal/mol]')
plt.ylabel('Calculated [kcal/mol]')

# save image
plt.savefig('binding_energies.png')


# calculate correlation r and rmsd
print 'correlation r and p:', stats.pearsonr(dGexp, dGcal)
print 'rmsd:', rmsd(dGexp, dGcal)

print

# print a Latex ready table row, using the format function
for i in range(len(dGcal)):
    print "{0:5d} & {1:5.2f} & {2:5.2f} \\\\".format(i+1, dGexp[i], dGcal[i])

