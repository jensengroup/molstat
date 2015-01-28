# Import pyplot and a function to create random numbers
import random
import matplotlib.pyplot as plt
import video

# initialize some variables
n_particles = 100
n_steps = 1000
dt = 0.01

# create the x- and y-coordinates
positions_x = [random.random() for i in range(n_particles)]
positions_y = [(random.random()-0.5)*2 for i in range(n_particles)]

# create the velocities
velocities_x = [(random.random()-0.5)*2 for i in range(n_particles)]
velocities_y = [(random.random()-0.5)*2 for i in range(n_particles)]

# Plot the x- and y- coordinates
plt.plot(positions_x, positions_y, 'ro')
plt.axis((-1, 1, -1, 1))
plt.savefig("coordinates_start.png")

# Make n_steps steps
for n in range(n_steps):

    # loop over each particle
    # for every step
    for i in range(n_particles):

        # make a step in time dt
        positions_x[i] = positions_x[i] + velocities_x[i]*dt
        positions_y[i] = positions_y[i] + velocities_y[i]*dt

        # if the particle is exiting the box in the x-direction, change the
        # velocity
        if abs(positions_x[i] + velocities_x[i]*dt) > 1.0:
            velocities_x[i] = -velocities_x[i]
            positions_x[i] = positions_x[i] + velocities_x[i]*dt


        if abs(positions_y[i] + velocities_y[i]*dt) > 1.0:
            velocities_y[i] = -velocities_y[i]
            positions_y[i] = positions_y[i] + velocities_y[i]*dt


    # save a 'frame' for the video every 10 step
    if n % 10 == 0:
        video.add_frame(positions_x, positions_y)


# Plot the x- and y- coordinates
plt.clf() # clear figure
plt.plot(positions_x, positions_y, 'ro')
plt.axis((-1, 1, -1, 1))
plt.savefig("coordinates_end.png")
plt.clf()

# Save video
video.save('non_interacting_particles')

