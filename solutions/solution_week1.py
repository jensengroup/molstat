# Import pyplot and a function to create random numbers
import numpy as np
import matplotlib.pyplot as plt
import md_video as video

# initialize some variables
n_particles = 100
box_width = 10.0
n_steps = 5000
dt = 0.001

# create the x- and y-coordinates
positions_x = [np.random.random()*box_width for i in range(n_particles)]
positions_y = [(np.random.random()-0.5)*2*box_width for i in range(n_particles)]

# create the velocities
velocities_x = [(np.random.random()-0.5)*2*box_width for i in range(n_particles)]
velocities_y = [(np.random.random()-0.5)*2*box_width for i in range(n_particles)]

# Plot the x- and y- coordinates
plt.plot(positions_x, positions_y, 'ro')
plt.axis((-box_width, box_width, -box_width, box_width))
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
        if abs(positions_x[i]) > box_width:
            velocities_x[i] = -velocities_x[i]
            positions_x[i] = positions_x[i] + velocities_x[i]*dt


        if abs(positions_y[i]) > box_width:
            velocities_y[i] = -velocities_y[i]
            positions_y[i] = positions_y[i] + velocities_y[i]*dt




    # save a 'frame' for the video every 10 step
    if n % 10 == 0:
        video.add_frame(positions_x, positions_y)

    if n % 100 == 0:
        print 'step', n


# Plot the x- and y- coordinates
plt.clf() # clear figure
plt.plot(positions_x, positions_y, 'ro')
plt.axis((-box_width, box_width, -box_width, box_width))
plt.savefig("coordinates_end.png")
plt.clf()

# Save video
video.save('solution_week1_video')

