# Modules

import random
import numpy as np
import matplotlib.pyplot as plt
import video_test as video

np.random.seed(109)

# Functions

def distance(x_i, y_i, x_j, y_j):
    """ Calculate the distance between particle i and particle j
    """
    dx = x_j - x_i
    dy = y_j - y_i
    d = np.sqrt(dx**2 + dy**2)
    return d


def initialize_particles(n_particles):
    """ initialize particles, positions and velocities for n_particles
    """
    box_width = 10.0

    positions_x = np.random.uniform(0.0, 9.0, n_particles)
    positions_y = np.random.uniform(-9.0, 9.0, n_particles)
    velocities_x = np.random.uniform(-9.0, 9.0, n_particles)
    velocities_y = np.random.uniform(-9.0, 9.0, n_particles)

    return positions_x, positions_y, velocities_x, velocities_y


def simulate_step(positions_x, positions_y, velocities_x, velocities_y, dt):
    """ Simulate particles movement for their positions and velocities in a
    a single time-step with time dt
    """

    N = len(positions_x)

    # Minimum distance before particles collide
    r_min = 1.1225
    box_width = 10.0

    # Loop over all particles and update positions
    for i in range(N):

        # make reflections if the particles are hitting the walls
        if abs(positions_x[i] + velocities_x[i]*dt) > box_width:
            velocities_x[i] = -velocities_x[i]

        if abs(positions_y[i] + velocities_y[i]*dt) > box_width:
            velocities_y[i] = -velocities_y[i]

        # make the move
        positions_x[i] += velocities_x[i]*dt
        positions_y[i] += velocities_y[i]*dt

        # make reflections if particle distances are small
        for j in range(N):
            if j > i:

                d = distance(positions_x[i],
                             positions_y[i],
                             positions_x[j],
                             positions_y[j])

                if d < r_min:

                    # print i, j, "hit", d
                    # plot_particles(positions_x, positions_y, 'hit')
                    # video.screenshot('hit_screenshot', positions_x, positions_y)

                    x_temp = velocities_x[i]
                    y_temp = velocities_y[i]

                    velocities_x[i] = velocities_x[j]
                    velocities_y[i] = velocities_y[j]

                    velocities_x[j] = x_temp
                    velocities_y[j] = y_temp


    return positions_x, positions_y, velocities_x, velocities_y


def plot_particles(X, Y, filename):
    """ Save an image of the positions at certain time """
    plt.plot(X, Y, 'bo')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.axis((-15, 15, -15, 15))
    plt.savefig(filename)
    # plt.show()
    plt.clf()


# Constants

n_particles = 20
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
# plot_particles(X, Y, 'coordinates_start.png')

# Loop over all time-steps
for n in range(n_step):

    # Simulate a single step
    X, Y, Vx, Vy = simulate_step(X, Y, Vx, Vy, dt)

    # Print status every 100th step
    if n % 100 == 0:
        print "Step {0:6d}".format(n)

    # Save frame for video every 10th step
    if n % 10 == 0:
        color = (1.0/(np.abs(Vx) + np.abs(Vy)))
        # color = [str(item/255.) for item in color]
        video.add_frame(X, Y, color)

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
# plot_particles(X, Y, 'coordinates_end.png')

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
plt.clf()

video.save('hard_sphere')


