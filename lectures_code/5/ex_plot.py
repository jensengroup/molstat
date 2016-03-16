
import matplotlib.pyplot as plt
import numpy as np

# load experimental data
# load calculated data

# calculate r

dg_exp = []
dg_cal = []

fe = open("experimental.csv")
fc = open("calculated_new.csv")

for line in fe:
    line = line.split(',')

    dg = float(line[1])
    dg_exp.append(dg)

for line in fc:
    line = line.split(' ')

    dU = float(line[1])
    dW = float(line[2])
    dS = float(line[3])

    dG = dU + dW - 298*dS - 5.83
    dg_cal.append(dG)


# plot
plt.plot(dg_exp, dg_cal, 'k.')
plt.xlabel('Experimental [kcal/mol]')
plt.ylabel('Calculated [kcal/mol]')
plt.savefig('binding_energy')

# calculate correlation r and rmsd
from scipy import stats

def rmsd(V, W):
    """
    Calculate Root-mean-square deviation from two sets of vectors V and W.
    """
    N = len(V)
    rmsd = 0.0
    for i in range(N):
        rmsd += (V[i]-W[i])**2.0
    return np.sqrt(rmsd/N)

print 'correlation r and p:', stats.pearsonr(dg_exp, dg_cal)
print 'rmsd', rmsd(dg_exp, dg_cal)


# print a latex table
for i in range(len(dg_cal)):

    print "{0:5d} & {1:5.2f} & {2:5.2f} \\\\".format(i+1, dg_exp[i], dg_cal[i])


