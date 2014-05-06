#!/usr/bin/env python

"""
video3d.py

@author jimmy@charnley.dk

usage:
    See main in bottom of file

"""


import numpy as np
import copy

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import matplotlib.animation as animation


x_frames = []
y_frames = []
z_frames = []


def save(filename, box_width, fps=25):
    """ Save a video with added frames
    """

    video_frames = len(x_frames)

    # Generate video output
    x_output = x_frames - box_width * np.floor(x_frames/box_width)
    y_output = y_frames - box_width * np.floor(y_frames/box_width)
    z_output = z_frames - box_width * np.floor(z_frames/box_width)

    fig = plt.figure()
    fig.subplots_adjust(left=0, right=1, bottom=0, top=1)
    ax = fig.add_subplot(111, projection='3d', autoscale_on=False,
                        xlim=(-box_width, box_width),
                        ylim=(-box_width, box_width),
                        zlim=(-box_width, box_width))

    # ax = fig.add_subplot(111, projection='3d', autoscale_on=False,
    #                     xlim=(-box_width, box_width),
    #                     ylim=(-box_width, box_width),
    #                     zlim=(-box_width, box_width))


    particles = ax.scatter(x_frames[0], y_frames[0], z_frames[0])


    def init():
        """ initialize animation
        """
        fig.clear()
        ax = fig.add_subplot(111, projection='3d', autoscale_on=False,
                            xlim=(-box_width, box_width),
                            ylim=(-box_width, box_width),
                            zlim=(-box_width, box_width))
        particles = ax.scatter([], [], [])
        return particles


    def animate(i):
        """ perform animation step
        """
        fig.clear()

        x = x_output[i]
        y = y_output[i]
        z = z_output[i]
        r = ((x-9.0)**2 + (y+9.0)**2 + (z-9.0)**2)**0.5
        r = 500/r

        # ax = fig.add_subplot(111, projection='3d', autoscale_on=False,
        #                     azim=-45,elev=35,
        #                     xlim=(-box_width, box_width),
        #                     ylim=(-box_width, box_width),
        #                     zlim=(-box_width, box_width))

        ax = fig.add_subplot(111, projection='3d', autoscale_on=False,
                            azim=-45,elev=35,
                            xlim=(0.0, box_width),
                            ylim=(0.0, box_width),
                            zlim=(0.0, box_width))

        particles = ax.scatter(x_output[i], y_output[i], z_output[i], s=r, c='k', marker='o', edgecolors='none')

        return particles


    # Create the animation object
    ani = animation.FuncAnimation(fig, animate, frames=video_frames,
                                    interval=10, blit=True, init_func=init)

    # Save the animation to disk
    # Change fps for another framerate
    ani.save(filename+'.mp4', fps=fps)


def add_frame(R):
    """ Add a frame to the video
    """

    x_frames.append(copy.copy(R[0]))
    y_frames.append(copy.copy(R[1]))
    z_frames.append(copy.copy(R[2]))


def save_frame(box_width, R, filename):
    """ Used for debugging
    """

    # Viewpoint
    E = [[9.0], [-9.0], [9.0]]

    x = R[0]
    y = R[1]
    z = R[2]

    r = ((x-9.0)**2 + (y+9.0)**2 + (z-9.0)**2)**0.5
    r = 500/r

    fig = plt.figure()
    fig.subplots_adjust(left=0, right=1, bottom=0, top=1)
    ax = fig.add_subplot(111, projection='3d', autoscale_on=False,
                        azim=-45,elev=35,
                        xlim=(-box_width, box_width),
                        ylim=(-box_width, box_width),
                        zlim=(-box_width, box_width))

    particles = ax.scatter(E[0], E[1], E[2], c='r', marker="o", edgecolors='none')
    particles = ax.scatter(R[0], R[1], R[2], c='k', marker="o", s=r, edgecolors='none')

    # plt.show(block=True)
    plt.savefig(filename)


if __name__ == '__main__':

    D = 3
    n_particles = 5
    n_steps = 3000
    dt = 0.1
    box_width = 10.0

    R = np.random.uniform(0.0, 10.0, (D, n_particles))
    V = np.random.uniform(-1.0, 1.0, (D, n_particles))

    for s in xrange(n_steps):

        R += V*dt

        for i in xrange(n_particles):
            for x in xrange(3):
                if abs(R[x,i]) > box_width:
                    V[x,i] *= -1.0
                    R[x,i] += V[x,i]*dt

        if s % 5 == 0:
            add_frame(R)

    save(box_width, 'test_video', fps=25)
    save_frame(box_width, R, 'test_image')


