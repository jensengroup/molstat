import math
import random
import pylab
import copy

import video


def distance(xi, yi, xj, yj):
    """ Calculate the distance between particle i and particle j """
    dx = xj-xi
    dy = yj-yi
    return math.sqrt(dx**2 + dy**2)


def lennard_jones(x_positions, y_positions):
    """ Calculate the force and energy based on the positions of the particles,
    in a Lennard-Jones potential
    """
    N = len(x_positions)
    energy = 0.0

    x_forces = [0.0 for _ in range(N) ]
    y_forces = [0.0 for _ in range(N) ]

    for i in range(N):
        for j in range(N):
            if i>j:

                # Distance
                rij = distance(x_positions[i],
                               y_positions[i],
                               x_positions[j],
                               y_positions[j])

                # Energy
                energy += 4*(1.0/rij**12 - 1.0/rij**6)

                # Force
                fx = -48* (x_positions[j]-x_positions[i])/rij**2 * (1/rij**12 - 0.5 *1/rij**6)
                fy = -48* (y_positions[j]-y_positions[i])/rij**2 * (1/rij**12 - 0.5 *1/rij**6)

                x_forces[i] = x_forces[i] + fx
                y_forces[i] = y_forces[i] + fy

                x_forces[j] = x_forces[j] - fx
                y_forces[j] = y_forces[j] - fy


    return x_forces, y_forces, energy


def initialize_particles(n_particles, box_width):
    """ Initialize particles in a grid position """

    sqrt_npart = int(math.ceil(math.sqrt(n_particles)))

    X = []
    Y = []

    for j in range(sqrt_npart):
        X += [i for i in range(sqrt_npart)]
        Y += [j for i in range(sqrt_npart)]

    # Might initialized too many particles, pop some
    while len(X) > n_particles:
        X.pop()
        Y.pop()

    for i in range(n_particles):
        X[i] = (X[i] - 0.5*sqrt_npart)*1.0/sqrt_npart*box_width*1.8
        Y[i] = (Y[i])*1.0/sqrt_npart*box_width*0.8

    # Initialize particle velocities
    Vx = [2*(random.random() - 0.5) for i in range(n_particles)]
    Vy = [2*(random.random() - 0.5) for i in range(n_particles)]

    # Initialize particle forces
    Fx, Fy, energy = lennard_jones(X, Y)

    return X, Y, Vx, Vy, Fx, Fy, energy


def velo_verlet(x_positions, y_positions,
                x_velocities, y_velocities,
                x_forces, y_forces, box_width, dt):
    """ Simulate particles movement for their positions and velocities in a
    single time - step with time dt
    """

    N = len(x_positions)

    x_forces_old = copy.copy(x_forces)
    y_forces_old = copy.copy(y_forces)

    # Step 1:
    # Update positions
    for i in range(N):
        x_positions[i] = x_positions[i] + dt*x_velocities[i] + 0.5*dt*dt*x_forces[i]
        y_positions[i] = y_positions[i] + dt*y_velocities[i] + 0.5*dt*dt*y_forces[i]

        if abs(x_positions[i]) > box_width:
            x_positions[i] -= dt*x_velocities[i]
            x_velocities[i] = -1*x_velocities[i]

        if abs(y_positions[i]) > box_width:
            y_positions[i] -= dt*y_velocities[i]
            y_velocities[i] = -1*y_velocities[i]

    # Step 2:
    # Update forces
    x_forces, y_forces, energy = lennard_jones(x_positions, y_positions)

    # Step 3:
    # Update velocities
    for i in range(N):
        x_velocities[i] = x_velocities[i] + 0.5*dt*(x_forces_old[i] + x_forces[i])
        y_velocities[i] = y_velocities[i] + 0.5*dt*(y_forces_old[i] + y_forces[i])

    return x_positions, y_positions, x_velocities, y_velocities, x_forces, y_forces, energy


def plot_box(X, Y, Vx, Vy, box_width, filename):
    pylab.plot(X, Y, 'ro')
    pylab.quiver(X, Y, Vx, Vy)
    pylab.axis((-box_width, box_width, -box_width, box_width))
    pylab.savefig(filename)
    pylab.clf()


## Simulation Initialization
box_width = 10.0
n_particles = 7*7
n_particles = 42
n_steps = 5000
dt = 0.001

# Empty energy lists
energy_list = []

# x_test = [0.0, 0.0]
# y_test = [0.0, 1.4]
# print lennard_jones(x_test, y_test)

## Initialize particles
X, Y, Vx, Vy, Fx, Fy, energy = initialize_particles(n_particles, box_width)

## Take simulation steps
for n in range(n_steps):

    X, Y, Vx, Vy, Fx, Fy, energy = velo_verlet(X, Y, Vx, Vy, Fx, Fy, box_width, dt)

    if n == 0:
        plot_box(X, Y, Vx, Vy, box_width, 'first_step.png')
        plot_box(X, Y, Fx, Fy, box_width, 'first_step_f.png')

    if n % 1 == 0:
        energy_list.append(energy)

    if n % 10 == 0:
        video.add_frame(X, Y)


## Plot Results

# Energy plot
pylab.plot(energy_list)
pylab.savefig('energy_time.png')

# Save video
video.save(box_width, "week3video")


