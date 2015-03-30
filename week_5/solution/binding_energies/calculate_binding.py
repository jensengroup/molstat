
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats


def rmsd(x, y):
    """ simple function to calculate RMSD between two datasets x and y
    """

    # get the length of the dataset
    n, = x.shape

    return np.sqrt(np.sum((x-y)**2)/n)



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

# find the max and min of both arrays
# list1 + list2 = [list1, list2]
mx = max(dGcal+dGexp)+3
mn = min(dGcal+dGexp)-3


# Make the plot

# middle line and +/- 2 dotted line
middle = np.arange(-30, 5)
plt.plot(middle, middle, 'r-')
plt.plot(middle-2.0, middle, 'r--')
plt.plot(middle, middle-2.0, 'r--')


# plot experimental vs calculated
plt.plot(dGexp, dGcal, 'k.')


# Find and highlight outliers
# by iterating over all data
for i in range(len(dGexp)):

    x = dGexp[i]
    y = dGcal[i]

    # find the error in G
    ddG = abs(x - y)

    # plot text if G is larger than 4.5
    if ddG > 4.5:

        # plot the id of the ligand
        plt.text(x+0.2, y+0.2, i+1)


# set the limits of the axis
plt.xlim((mn, mx))
plt.ylim((mn, mx))

# set labels
plt.xlabel('Experimental [kcal/mol]')
plt.ylabel('Calculated [kcal/mol]')

# save image
plt.savefig('binding_energies.png')


# calculate correlation r and rmsd
print 'correlation r and p:', stats.pearsonr(dGexp, dGcal)
print 'rmsd:', rmsd(np.array(dGexp), np.array(dGcal))

print

# print a Latex ready table row, using the format function
for i in range(len(dGcal)):

    print "{0:5d} & {1:5.2f} & {2:5.2f} \\\\".format(i+1, dGexp[i], dGcal[i])


