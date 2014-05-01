#!/usr/bin/python

import random
import numpy as np
import matplotlib.pyplot as plt

import video

def distance(xi, yi, xj, yj):
    """ Calculate the distance between particle i and particle j """
    dx = xj-xi
    dy = yj-yi
    d = np.sqrt(dx**2 + dy**2)
    return d


def initialize_particles(n_particles):
    """ initialize particles, positions and velocities for n_particles """
    pos_x  = [random.random() for i in range(n_particles)]
    pos_y  = [2 * (random.random() - 0.5) for i in range(n_particles)]
    vel_x  = [2 * (random.random() - 0.5) for i in range(n_particles)]
    vel_y  = [2 * (random.random() - 0.5) for i in range(n_particles)]
    return pos_x, pos_y, vel_x, vel_y


def simulate_step(x_positions, y_positions, x_velocities, y_velocities, dt):
    """ Simulate particles movement for their positions and velocities in a
    single time-step with time dt """

    N = len(x_positions)

    # Minimum distance before particles collide
    r_min = 0.03

    # Loop over all particles and update positions
    for i in range(N):

        # make reflections if the particles are hitting the walls
        if abs(x_positions[i] + x_velocities[i] * dt) > 1.0:
            x_velocities[i] = -x_velocities[i]

        if abs(y_positions[i] + y_velocities[i] * dt) > 1.0:
            y_velocities[i] = -y_velocities[i]


        # make reflections if particle distances are small
        for j in range(N):
            if j > i:
                if distance(x_positions[i] + x_velocities[i]*dt,
                            y_positions[i] + y_velocities[i]*dt,
                            x_positions[j], y_positions[j]) < r_min:

                    x_temp = x_velocities[i]
                    y_temp = y_velocities[i]

                    x_velocities[i] = x_velocities[j]
                    y_velocities[i] = y_velocities[j]

                    x_velocities[j] = x_temp
                    y_velocities[j] = y_temp


        # make the move
        x_positions[i] += x_velocities[i] * dt
        y_positions[i] += y_velocities[i] * dt

    return x_positions, y_positions, x_velocities, y_velocities


def plot_particles(X, Y, filename):
    """ Save an image of the positions at certain time """
    plt.plot(X, Y, 'bo')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.axis((-1,1,-1,1))
    plt.savefig(filename)
    plt.clf()


# Constants
n_particles = 40
n_step = 5000 # for movie
#n_step = 20000 # for histogram
dt = 0.001

# Histogram
partdist = []
partdisteq = []

X, Y, Vx, Vy = initialize_particles(n_particles)

plot_particles(X, Y, 'coordinates_start.png')

# The main loop
for n in range(n_step):

    X, Y, Vx, Vy = simulate_step(X, Y, Vx, Vy, dt)

    # Print status every 100th step
    if n % 100 == 0:
        print "Step %5i" % (n)

    # Save frame for video every 10th step
    if n % 10 == 0:
        video.add_frame(X, Y)

    # Count the particles in the right part of the box
    if n % 5 == 0:
        no_part = 0

        for i in range(n_particles):
            # No need to check for x_positions > 1 or y_positions since we are ALWAYS
            # within the box.
            if( X[i] > 0.0 ):
                no_part += 1


        if( n < n_step / 2.0 ):
            partdist.append( no_part )
        if( n > n_step / 2.0 ):
            partdisteq.append( no_part )
            partdist.append( no_part )



plot_particles(X, Y, 'coordinates_end.png')


#plot the partdist list
plt.title('Particle Count for X > 0.0 and N < 10000')
plt.xlabel('Number of particles where X > 0.0')
plt.ylabel('Count')
plt.hist(partdist, bins=range(0, n_particles), align='left')
plt.xlim( (0, n_particles) )
plt.savefig('partdist.png')
#plt.savefig('partdist.eps')


#plot the partdisteq list
plt.clf()
plt.title('Particle Count for X > 0.0 and N > 10000')
plt.xlabel('Number of particles where X > 0.0')
plt.ylabel('Count')
plt.hist(partdisteq, bins=range(0, n_particles), rwidth=1, align='left')
plt.xlim( (0, n_particles) )
plt.savefig('partdisteq.png')
#plt.savefig('partdisteq.eps')


video.save('hard_sphere')

