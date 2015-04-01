# Modules

import numpy as np
import matplotlib.pyplot as plt
import md_video as video

np.random.seed(109)

# Functions

def distance(x_i, y_i, x_j, y_j):
    """
    Calculate the distance between particle i and particle j
    """
    dx = x_j - x_i
    dy = y_j - y_i
    d = np.sqrt(dx**2 + dy**2)
    return d


def initialize_particles(n_particles, box_width):
    """
    initialize particles, positions and velocities for n_particles
    """

    positions_x = np.random.uniform(0.0, box_width, n_particles)
    positions_y = np.random.uniform(-box_width, box_width, n_particles)
    velocities_x = np.random.uniform(-box_width, box_width, n_particles)
    velocities_y = np.random.uniform(-box_width, box_width, n_particles)

    return positions_x, positions_y, velocities_x, velocities_y


def simulate_step(positions_x, positions_y, velocities_x, velocities_y, dt, N, box_width):
    """
    Simulate particles movement for their positions and velocities in a single
    time-step with time dt
    """

    # Minimum distance before particles collide
    r_min = 1.1225

    # Loop over all particles and update positions
    for i in xrange(N):

        # make reflections if the particles are hitting the walls
        if abs(positions_x[i] + velocities_x[i]*dt) > box_width:
            velocities_x[i] = -velocities_x[i]

        if abs(positions_y[i] + velocities_y[i]*dt) > box_width:
            velocities_y[i] = -velocities_y[i]

        # make the move
        positions_x[i] += velocities_x[i]*dt
        positions_y[i] += velocities_y[i]*dt

        # make reflections if particle distances are small
        for j in xrange(i, N):
            # if j > i:

            d = distance(positions_x[i],
                        positions_y[i],
                        positions_x[j],
                        positions_y[j])

            if d < r_min:

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


def write_list(filename, list):
    """
    """

    f = open(filename, 'w')

    for element in list:

        f.write(str(element))
        f.write('\n')



# Constants

n_particles = 40
box_width = 10.0
dt = 0.001

# For movie
# n_step = 5000

# for histogram
n_step = 20000


# Histogram
partdist = []
partdisteq = []

# initialize particles
X, Y, Vx, Vy = initialize_particles(n_particles, box_width)

# plot start coordinates
# plot_particles(X, Y, 'coordinates_start.png')

# Loop over all time-steps
for n in range(n_step):

    # Simulate a single step
    X, Y, Vx, Vy = simulate_step(X, Y, Vx, Vy, dt, n_particles, box_width)

    # Print status every 100th step
    if n % 200 == 0:
        print "Step {0:6d}".format(n)

    # Save frame for video every 10th step
    # if n % 10 == 0:
        # color = (1.0/(np.abs(Vx) + np.abs(Vy)))
        # color = [str(item/255.) for item in color]
        # video.add_frame(X, Y)


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



write_list('test_list', partdist)
write_list('test_list_eq', partdisteq)


# plot particles in the end of the simulation
# plot_particles(X, Y, 'coordinates_end.png')


# video.save('hard_sphere')


