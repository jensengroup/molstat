# Modules

import random
import numpy as np
import matplotlib.pyplot as plt
import video

# Functions

def distance(xi, yi, xj, yj):
    """ Calculate the distance between particle i and particle j
    """
    dx = xj-xi
    dy = yj-yi
    d = np.sqrt(dx**2 + dy**2)
    return d


def initialize_particles(n_particles):
    """ initialize particles, positions and velocities for n_particles
    """
    pos_x = [random.random() for i in range(n_particles)]
    pos_y = [2 * (random.random() - 0.5) for i in range(n_particles)]
    vel_x = [2 * (random.random() - 0.5) for i in range(n_particles)]
    vel_y = [2 * (random.random() - 0.5) for i in range(n_particles)]
    return pos_x, pos_y, vel_x, vel_y


def simulate_step(pos_x, pos_y, vel_x, vel_y, dt):
    """ Simulate particles movement for their positions and velocities in a
    a single time-step with time dt
    """

    N = len(pos_x)

    # Minimum distance before particles collide
    r_min = 0.03

    # Loop over all particles and update positions
    for i in range(N):

        # make reflections if the particles are hitting the walls
        if abs(pos_x[i] + vel_x[i]*dt) > 1.0:
            vel_x[i] = -vel_x[i]

        if abs(pos_y[i] + vel_y[i]*dt) > 1.0:
            vel_y[i] = -vel_y[i]

        # make the move
        pos_x[i] += vel_x[i]*dt
        pos_y[i] += vel_y[i]*dt

        # make reflections if particle distances are small
        for j in range(N):
            if j > i:

                d = distance(pos_x[i], pos_y[i], pos_x[j], pos_y[j])

                if d < r_min:

                    x_temp = vel_x[i]
                    y_temp = vel_y[i]

                    vel_x[i] = vel_x[j]
                    vel_y[i] = vel_y[j]

                    vel_x[j] = x_temp
                    vel_y[j] = y_temp


    return pos_x, pos_y, vel_x, vel_y


def plot_particles(X, Y, filename):
    """ Save an image of the positions at certain time """
    plt.plot(X, Y, 'bo')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.axis((-1, 1, -1, 1))
    plt.savefig(filename)
    plt.clf()


# Constants

n_particles = 40
dt = 0.001

# For movie
n_step = 5000

# for histogram
#n_step = 20000


# Histogram
partdist = []
partdisteq = []

# initialize particles
X, Y, Vx, Vy = initialize_particles(n_particles)

# plot start coordinates
plot_particles(X, Y, 'coordinates_start.png')

# Loop over all time-steps
for n in range(n_step):

    # Simulate a single step
    X, Y, Vx, Vy = simulate_step(X, Y, Vx, Vy, dt)

    # Print status every 100th step
    if n % 100 == 0:
        print "Step {0:6d}".format(n)

    # Save frame for video every 10th step
    if n % 10 == 0:
        video.add_frame(X, Y)

    # Count the particles in the right part of the box
    if n % 5 == 0:
        no_part = 0

        for i in range(n_particles):
            # No need to check for x_positions > 1 or y_positions since we are ALWAYS
            # within the box.
            if X[i] > 0.0:
                no_part += 1

        partdist.append(no_part)

        if n > n_step / 2.0:
            partdisteq.append(no_part)


# plot particles in the end of the simulation
plot_particles(X, Y, 'coordinates_end.png')

# plot the partdist list
plt.title('Particle Count for X > 0.0 and N < 10000')
plt.xlabel('Number of particles where X > 0.0')
plt.ylabel('Count')
plt.hist(partdist, bins=range(0, n_particles), align='left')
plt.xlim( (0, n_particles) )
plt.savefig('partdist.png')
plt.clf()

# plot the partdisteq list
plt.title('Particle Count for X > 0.0 and N > 10000')
plt.xlabel('Number of particles where X > 0.0')
plt.ylabel('Count')
plt.hist(partdisteq, bins=range(0, n_particles), rwidth=1, align='left')
plt.xlim( (0, n_particles) )
plt.savefig('partdisteq.png')

video.save('hard_sphere')

