#!/usr/bin/env python

import copy
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

"""
video.py

@author jimmy@charnley.dk

Usage:

    See bottom of module

"""


# Create a pair of empty frames
x_frames = []
y_frames = []


def save(filename, box_width=10.0, fps=25):
    """ Takes 2D coordinates x_frames and y_frames, saves it into filename.mp4 with
    len(x_frames) steps.
    """

    video_frames = len(x_frames)

    print "Saving", video_frames, "frames"

    # Setup figure
    fig = plt.figure()
    fig.subplots_adjust(left=0, right=1, bottom=0, top=1)
    ax = fig.add_subplot(111,
                        aspect='equal',
                        autoscale_on=False,
                        xlim=(-(box_width+0.2), (box_width+0.2)),
                        ylim=(-(box_width+0.2), box_width+0.2))

    # Particles holds the locations of the particles
    particles, = ax.plot([], [], 'ko', ms=6)

    # Set an Retangle around the box
    rect = plt.Rectangle((-box_width, -box_width),
                        2*box_width,
                        2*box_width,
                        fill=False,
                        linewidth=2.0,
                        edgecolor='k')
    ax.add_patch(rect)

    # Remove default axis for cinematic effect
    plt.axis('off')

    def init():
        """initialize animation"""
        particles.set_data([], [])
        return particles

    def animate(i):
        """perform animation step"""
        particles.set_data(x_frames[i], y_frames[i])
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
    ani.save(filename+'.mp4', fps=fps, writer='mencoder')

    # Clear figure
    plt.clf()

    print "Done saving "+filename+".mp4"


def add_frame(x_frame, y_frame):
    """ Add X and Y coordinates for a video-frame
    """
    x_frames.append(copy.copy(x_frame))
    y_frames.append(copy.copy(y_frame))



if __name__ == "__main__":

    # Testing and showing example of how to use module

    n_particles = 20

    for _ in xrange(600):
        add_frame(np.array([np.random.random() for i in range(n_particles)]) * 10.0,
                  np.array([2 * (np.random.random() - 0.5) for i in range(n_particles)]) * 10.0)

    save('random_particles', 10.0)

