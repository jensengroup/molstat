# Import pyplot and a function to create random numbers
import random
import matplotlib.pyplot as plt
import video

# initialize some variables
n_particles = 100
n_steps = 1000
dt = 0.01

# create the x- and y-coordinates
pos_x = [random.random() for i in range(n_particles)]
pos_y = [(random.random()-0.5)*2 for i in range(n_particles)]

# create the velocities
vel_x = [(random.random()-0.5)*2 for i in range(n_particles)]
vel_y = [(random.random()-0.5)*2 for i in range(n_particles)]

# Plot the x- and y- coordinates
plt.plot(pos_x, pos_y, 'ro')
plt.axis((-1, 1, -1, 1))
plt.savefig("coordinates_start.png")

# Make n_steps steps
for n in range(n_steps):

    # loop over each particle
    # for every step
    for i in range(n_particles):

        # make a step in time dt
        pos_x[i] = pos_x[i] + vel_x[i]*dt
        pos_y[i] = pos_y[i] + vel_y[i]*dt

        # if the particle is exiting the box in the x-direction, change the
        # velocity
        if abs(pos_x[i] + vel_x[i]*dt) > 1.0:
            vel_x[i] = -vel_x[i]
            pos_x[i] = pos_x[i] + vel_x[i]*dt

        if abs(pos_y[i] + vel_y[i]*dt) > 1.0:
            vel_y[i] = -vel_y[i]
            pos_y[i] = pos_y[i] + vel_y[i]*dt


    # save a 'frame' for the video every 10 step
    if n % 10 == 0:
        video.add_frame(pos_x, pos_y)


# Plot the x- and y- coordinates
plt.clf() # clear figure
plt.plot(pos_x, pos_y, 'ro')
plt.axis((-1, 1, -1, 1))
plt.savefig("coordinates_end.png")
plt.clf()

# Save video
video.save('non_interacting_particles')

