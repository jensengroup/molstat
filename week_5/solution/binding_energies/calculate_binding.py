
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats


def rmsd(x, y):

    n, = x.shape

    return np.sqrt(np.sum((x-y)**2)/n)



# experimental

dGexp = []

f = open('experimental.csv')
for line in f:

    line = line.split(',')
    dG = float(line[1])
    dGexp.append(dG)



dGcal = []

delta = -5.83

f = open('calculated_new.csv')
for line in f:

    line = line.split()
    dU = float(line[1])
    dW = float(line[2])
    dS = float(line[3])

    dG = dU + dW - 298.0*dS + delta

    dGcal.append(dG)


mx = max(dGcal+dGexp)+3
mn = min(dGcal+dGexp)-3

# plot

middle = np.arange(-30, 5)

plt.plot(middle, middle, 'r-')
plt.plot(middle-2.0, middle, 'r--')
plt.plot(middle, middle-2.0, 'r--')

plt.plot(dGexp, dGcal, 'k.')

# Plot Outliers

for i in range(len(dGexp)):

    x = dGexp[i]
    y = dGcal[i]

    ddG = abs(x - y)

    if ddG > 4.5:
        plt.text(x+0.2, y+0.2, i+1)


plt.xlim((mn, mx))
plt.ylim((mn, mx))

plt.xlabel('Experimental [kcal/mol]')
plt.ylabel('Calculated [kcal/mol]')

plt.savefig('binding_energies.png')

print 'correlation', stats.pearsonr(dGexp, dGcal)
print 'rmsd', rmsd(np.array(dGexp), np.array(dGcal))

print


for i in range(len(dGcal)):

    print "{0:5d} & {1:5.2f} & {2:5.2f} \\\\".format(i+1, dGexp[i], dGcal[i])



