# Example 2

# SQUARE FUNCTION
# - functions used in functions
# - multiple parameters
# - multiple return values

def square(x):
    y = x**2
    return y

import numpy as np
# Note, also use np as math

x_list = np.arange(0, 10, 0.1)
y_list = [square(x) for x in x_list]

import matplotlib.pyplot as plt

plt.plot(x_list, y_list)
plt.savefig('the_square_function.png')
plt.clf()



# THE LENNARD-JONES POTENTIAL

def lj(r):

    epsilon = 1.0
    sigma = 1.0

    v = 4*epsilon*((sigma/r)**12 - (sigma/r)**6)

    return v

x_list = np.arange(1, 3, 0.001)
l_list = [lj(x) for x in x_list]

plt.plot(x_list, l_list)
plt.savefig('lj.png')
plt.clf()



# THE GAUSSIAN FUNCTION

def gaussian(x):

    a = 1.0
    b = 0.0
    c = 1.0
    d = 0.0

    g = a*np.exp( -(x-b)**2 / (2*c**2) ) + d

    return g


x_list = np.arange(-5, 5, 0.01)
g_list = [gaussian(x) for x in x_list]

plt.plot(x_list, g_list)
plt.savefig('gaussian.png')


