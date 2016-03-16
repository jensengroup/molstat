# Modules

import numpy as np
import matplotlib.pyplot as plt
import md_video as video


# Functions

def distance(x_i, y_i, x_j, y_j):
    """
    Calculate the distance between particle i and particle j
    """
    dx = x_j - x_i
    dy = y_j - y_i
    d = np.sqrt(dx**2 + dy**2)
    return d


def initialize_particles(n_particles, box_width, r_min):
    """
    initialize particles, positions and velocities for n_particles
    """

    positions_x = np.random.uniform(0.0, box_width, n_particles)
    positions_y = np.random.uniform(-box_width, box_width, n_particles)
    velocities_x = np.random.uniform(-box_width, box_width, n_particles)
    velocities_y = np.random.uniform(-box_width, box_width, n_particles)

    # EXTRA
    # Enable this to fix particles overlapping when initialized
    #positions_x, positions_y = correct_initial_positions(positions_x, positions_y, box_width, n_particles, r_min)
    return positions_x, positions_y, velocities_x, velocities_y


def correct_initial_positions(positions_x, positions_y, box_width, n_particles, r_min):
   """
   If two particles collide in the initialization, give one of them a new random position
   Repeat this 5 times
   """
   for repetition in range(5):
       for i in range(n_particles):
           for j in range(i+1,n_particles):

               # calculate distance
               d = distance(positions_x[i],
                            positions_y[i],
                            positions_x[j],
                            positions_y[j])

               if d < r_min:
                   positions_x[j] = np.random.uniform(0.0, box_width)
                   positions_y[j] = np.random.uniform(-box_width, box_width)

   return positions_x, positions_y


def simulate_step(positions_x, positions_y, velocities_x, velocities_y, dt, N, box_width, r_min):
    """
    Simulate particles movement for their positions and velocities in a single
    time-step with time dt
    """


    # Loop over all particles and make corrections for collisions
    for i in range(N):
        # make a step in time dt for all particles
        positions_x[i] = positions_x[i] + velocities_x[i]*dt
        positions_y[i] = positions_y[i] + velocities_y[i]*dt

        # make reflections if the particles are hitting the walls
        # and move them back inside
        if abs(positions_x[i]) > box_width:
            velocities_x[i] = -velocities_x[i]
            positions_x[i] = positions_x[i] + velocities_x[i]*dt

        if abs(positions_y[i]) > box_width:
            velocities_y[i] = -velocities_y[i]
            positions_y[i] = positions_y[i] + velocities_y[i]*dt

        # make reflections if particle distances are small
        for j in range(i+1, N): # This is the same as a double loop with 'if j > i':

            d = distance(positions_x[i],
                        positions_y[i],
                        positions_x[j],
                        positions_y[j])

            if d < r_min:

                vx_temp = velocities_x[i]
                vy_temp = velocities_y[i]

                velocities_x[i] = velocities_x[j]
                velocities_y[i] = velocities_y[j]

                velocities_x[j] = vx_temp
                velocities_y[j] = vy_temp

                # # EXTRA
                # # Enable this check to only correct colliding particles velocities
                # # if they are moving closer to each other at next step
                # d_next = distance(positions_x[i] + velocities_x[i]*dt,
                #                  positions_y[i] + velocities_y[i]*dt,
                #                  positions_x[j] + velocities_x[j]*dt,
                #                  positions_y[j] + velocities_y[j]*dt)
                # if d < d_next:
                #    continue
                #
                # # EXTRA
                # # do this instead for proper angle handling
                # c = (velocities_x[i] - velocities_x[j]) * (positions_x[i] - positions_x[j]) \
                #  + (velocities_y[i] - velocities_y[j]) * (positions_y[i] - positions_y[j])
                # c /= (positions_x[i] - positions_x[j])**2 + (positions_y[i] - positions_y[j])**2
                #
                # velocities_x[i] = velocities_x[i] - c * (positions_x[i] - positions_x[j])
                # velocities_y[i] = velocities_y[i] - c * (positions_y[i] - positions_y[j])
                #
                # velocities_x[j] = velocities_x[j] - c * (positions_x[j] - positions_x[i])
                # velocities_y[j] = velocities_y[j] - c * (positions_y[j] - positions_y[i])

                # or
                # velocities_x[i], velocities_x[j] = velocities_x[j], velocities_x[i]
                # velocities_y[i], velocities_y[j] = velocities_y[j], velocities_y[i]


    return positions_x, positions_y, velocities_x, velocities_y


def plot_particles(X, Y, box_width, filename):
    """
    Save an image of the positions at certain time
    """
    plt.plot(X, Y, 'bo')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.axis((-box_width, box_width, -box_width, box_width))
    plt.savefig(filename)
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
# Minimum distance before particles collide
r_min = 1.0

# For movie
n_step = 5000

# for histogram
# n_step = 20000

# Histogram
partdist = []
partdisteq = []

# initialize particles
X, Y, Vx, Vy = initialize_particles(n_particles, box_width, r_min)

# plot start coordinates
# plot_particles(X, Y, box_width, 'coordinates_start.png')

# Loop over all time-steps
for n in range(n_step):

    # Simulate a single step
    X, Y, Vx, Vy = simulate_step(X, Y, Vx, Vy, dt, n_particles, box_width, r_min)

    # Print status every 200th step
    if n % 200 == 0:
        print "Step {0:6d}".format(n)

    # Save frame for video every 10th step
    if n % 10 == 0:
        video.add_frame(X, Y)


    # Count the particles in the right part of the box
    if n % 5 == 0:
        no_part = 0

        for i in range(n_particles):
            # No need to check for x_positions > 10 or y_positions since we are ALWAYS
            # within the box.
            if X[i] > 0.0:
                no_part += 1

        partdist.append(no_part) # Save number of particles in right half of box

        if n > n_step / 2.0: # Only save number of particles for the last half of the simulation
            partdisteq.append(no_part)



write_list('test_list', partdist)
write_list('test_list_eq', partdisteq)


# plot particles in the end of the simulation
# plot_particles(X, Y, 'coordinates_end.png')


video.save('solution_video3')


