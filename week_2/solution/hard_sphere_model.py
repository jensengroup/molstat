#!/usr/bin/python

import random
import math
import pylab

import video

def distance(xi, yi, xj, yj):
    """ Calculate the distance between particle i and particle j """
    dx = xj-xi
    dy = yj-yi
    d = math.sqrt(dx**2 + dy**2)
    return d


def initialize_particles(n_particles):
    """ initialize particles, positions and velocities for n_particles """
    x_positions  = [random.random() for i in range(n_particles)]
    y_positions  = [2 * (random.random() - 0.5) for i in range(n_particles)]
    x_velocities = [2 * (random.random() - 0.5) for i in range(n_particles)]
    y_velocities = [2 * (random.random() - 0.5) for i in range(n_particles)]
    return x_positions, y_positions, x_velocities, y_velocities


def simulate_step(x_positions, y_positions, x_velocities, y_velocities, dt):
    """ Simulate particles movement for their positions and velocities in a
    single time-step with time dt """

    N = len(x_positions)

    # Minimum distance before particles collide
    r_min = 0.03

    # Loop over all particles and update positions
    for i in range(N):

        # make reflections if the particles are hitting the walls
        if abs(X[i] + Vx[i] * dt) > 1.0:
            Vx[i] = -Vx[i]

        if abs(Y[i] + Vy[i] * dt) > 1.0:
            Vy[i] = -Vy[i]


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
        X[i] += Vx[i] * dt
        Y[i] += Vy[i] * dt

    return x_positions, y_positions, x_velocities, y_velocities


def plot_particles(X, Y, filename):
    """ Save an image of the positions at certain time """
    pylab.plot(X, Y, 'bo')
    pylab.xlabel('x')
    pylab.ylabel('y')
    pylab.axis((-1,1,-1,1))
    pylab.savefig(filename)


# Constants
n_particles = 40
n_step = 2000 # for movie
# n_step = 20000 # for historgram
dt = 0.001

# Histogram
particle_dist = []
particle_dist_eq = []

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

    # Count the particles
    if n % 5 == 0:
        no_part = 0

        for i in range(n_particles):
            # No need to check for x_positions < 1 or y_positions since we are ALWAYS
            # within the box.
            if( X[i] > 0.0 ):
                no_part += 1


        if( n < n_step / 2 ):
            particle_dist.append( no_part )
        if( n > n_step / 2 ):
            particle_dist_eq.append( no_part )



plot_particles(X, Y, 'coordinates_end.png')


# plot the partdist list
# pylab.clf()
# pylab.title('Particle Count for X > 0.0 and N < 10000')
# pylab.xlabel('Number of particles where X > 0.0')
# pylab.ylabel('Count')
# pylab.hist(particle_dist, bins=range(0, n_particles), align='left')
# pylab.xlim( (0, n_particles) )
# pylab.savefig('partdist.png')
# pylab.savefig('partdist.eps')


# plot the partdisteq list
# pylab.clf()
# pylab.title('Particle Count for X > 0.0 and N > 10000')
# pylab.xlabel('Number of particles where X > 0.0')
# pylab.ylabel('Count')
# pylab.hist(particle_dist_eq, bins=range(0, n_particles), rwidth=1, align='left')
# pylab.xlim( (0, n_particles) )
# pylab.savefig('partdisteq.png')
# pylab.savefig('partdisteq.eps')


video.save(1.0, 'hard_sphere')

