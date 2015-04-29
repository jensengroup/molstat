
import numpy as np
import matplotlib.pyplot as plt


# simple example
f = open('file', 'w')

f.write('line')
f.write('new line?')
f.write('line\n')
f.write('line')



# Bifurcation diagram

# http://en.wikipedia.org/wiki/Bifurcation_diagram
# http://en.wikipedia.org/wiki/Complex_quadratic_polynomial

# rs = np.linspace(0.0, 0.5, 30) # local plot
# iterations = 100
# rs = np.linspace(0.0, 1.0, 100) # local plot
# iterations = 100

# List of elements from 0.0 to 2.0 in 300 steps
rs = np.linspace(0.0, 2.0, 300) # for file

# how many n's
iterations = 1000

# file to save to
f = open('chaos.csv', 'w')

# First guess
for r in rs:

    print r

    # initial guess
    x = 0.1

    # burn-in steps
    for i in range(iterations):
        x = x**2 - r

    # iterate some more
    for i in range(iterations):
        x = x**2 - r

        line = str(r) + ',' + str(x)
        f.write(line)
        f.write('\n')

        # plt.plot(r, y, 'k.')

# plt.savefig('chaos1.png')

