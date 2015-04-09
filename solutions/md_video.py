#!/usr/bin/env python

import copy
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

"""

based on
http://stackoverflow.com/questions/9401658/matplotlib-animating-a-scatter-plot
http://stackoverflow.com/questions/12892863/animated-scatterplot-of-data-with-matplotlib
http://matplotlib.org/examples/shapes_and_collections/scatter_demo.html

"""


x_frames = []
y_frames = []
c_frames = []

green = "#4daf4a"


def create_plot(box_width, grid):
    """
    """

    fig = plt.figure()
    ax = fig.add_subplot(111,
                        aspect='equal',
                        autoscale_on=False,
                        xlim=(-(box_width+0.0), (box_width+0.0)),
                        ylim=(-(box_width+0.0), box_width+0.0))

    # Add an retangle around the box
    rect = plt.Rectangle((-box_width, -box_width),
                        2*box_width,
                        2*box_width,
                        fill=False,
                        linewidth=3.0,
                        edgecolor='k')
    ax.add_patch(rect)

    if grid:
        ax.grid(True)
    else:
        plt.axis('off')

    return fig, ax


def set_box_width():
    """
    TODO
    """


def set_particle_radius():
    """
    TODO
    """


def save(filename, box_width=10.0, fps=25, grid=False, area=300):
    """
    Takes 2D coordinates x_frames and y_frames, saves it into filename.mp4 with
    len(x_frames) steps.
    """

    global x_frames
    global y_frames
    global c_frames

    color_update = True

    x_frames = np.array(x_frames)
    y_frames = np.array(y_frames)

    video_frames = len(x_frames)

    if len(c_frames) == 0:
        c_frames = [green for n in xrange(video_frames)]
        color_update = False

    fig, ax = create_plot(box_width, grid)

    # marker="*"
    # marker='$\heartsuit$'
    # particles_dot, = ax.plot(x_frames[0], y_frames[0], 'ko', ms=6)
    particles = ax.scatter(x_frames[0], y_frames[0], s=area, c=c_frames[0], linewidth=0.6)


    def init():
        """
        initialize animation
        """
        # particles.set_data([], [])
        return particles


    def animate(i):
        """
        perform animation step
        """
        j = i-1

        # Offsets are given as a N tuples of 2 items each while the data array
        # is given as 2 tuples with N items each, transposing the data array
        # will fix your problem.
        offset = np.array([x_frames[i], y_frames[i]]).transpose()
        particles.set_offsets(offset)

        if color_update:
            particles.set_array(c_frames[i])

        # particles_dot.set_data(x_frames[i], y_frames[i])
        # print j, (x_frames[i]-x_frames[j])[0]

        return particles

    # Create the animation object
    ani = animation.FuncAnimation(fig, animate,
                                  frames=video_frames,
                                  interval=10,
                                  blit=True,
                                  init_func=init)

    # Save the animation to disk
    # Change fps for another framerate
    # NOTE: Use mencoder, instead of ffmpeg
    # ani.save(filename+'.mp4', fps=fps, writer='mencoder')
    ani.save(filename+'.mp4', fps=fps)

    # Save as gif
    # ani.save(filename+'.gif', writer='imagemagick')


    # Clear figure
    plt.clf()




def screenshot(filename, x, y, color=green, box_width=10.0, grid=True, area=300):
    """
    """

    # TODO
    # radius = 10.0
    # area = np.pi * radius**2
    # print area

    fig, ax = create_plot(box_width, grid)
    ax.scatter(x, y, s=area, c=color, linewidth=0.6)
    ax.plot(x, y, 'ko', ms=6)

    box = 1.0
    rect = plt.Rectangle((-box/2.0, -box/2.0),
                        box,
                        box,
                        fill=False,
                        linewidth=0.5,
                        edgecolor='k')
    ax.add_patch(rect)
    fig.savefig(filename)
    fig.clf()
    plt.clf()


def add_frame(x_frame, y_frame):
    """
    Add X and Y coordinates for a video frame
    """
    x_frames.append(copy.copy(x_frame))
    y_frames.append(copy.copy(y_frame))


def add_color_frame(color):
    """
    Add particle color for a video frame
    """
    c_frames.append(copy.copy(color))


if __name__ == "__main__":

    # Testing and showing example of how to use module

    x = [0.0, 1.0]
    y = [0.0, 1.0]

    screenshot('random_screenshot', x, y)

    quit()

    n_particles = 20

    for _ in xrange(600):
        add_frame(np.array([np.random.random() for i in range(n_particles)]) * 10.0,
                  np.array([2 * (np.random.random() - 0.5) for i in range(n_particles)]) * 10.0)

    save('random_particles', 10.0)


