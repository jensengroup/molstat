import random
import pylab

n_particles = 100
n_steps = 1
dt = 0.001

x_positions = [random.random() for i in range(n_particles)]
y_positions = [random.random() for i in range(n_particles)]

pylab.plot(x_positions,y_positions, "ro")
pylab.axis((-1, 1, -1, 1))
pylab.savefig("coordinates_start.png")


