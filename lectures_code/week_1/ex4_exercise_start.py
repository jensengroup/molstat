# Example 4

# Exercise

import random
import matplotlib.pyplot as plt

# initialize some variables
n_particles = 100
n_steps = 1
dt = 0.01

# create the x - and y - coordinates
x_positions = [ random.random() for i in range( n_particles ) ]
y_positions = [ random.random() for i in range( n_particles ) ]

# plot the x - and y - coordinates in a figure .
plt.plot(x_positions , y_positions , 'ro') #explain what 'ro' does
plt.axis((-10, 10, -10, 10))
plt.savefig('coordinates_start.png')

