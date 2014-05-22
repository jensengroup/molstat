import numpy
import time
import copy

from forces import lennardjones as fortran_lj



# Initialize particle positions
def initialize_positions(natms, rho):
    """This code block is unreadable
    """
    n = natms
    p = int(numpy.floor(n**(1.0/3.0))) + 1
    box = (n/rho)**(1.0/3.0)
    du = box/p
    X = numpy.multiply.outer(numpy.ones(p), numpy.arange(p))
    X = numpy.multiply.outer(numpy.ones(p), X)
    Y = numpy.multiply.outer(numpy.arange(p), numpy.ones(p))
    Y = numpy.multiply.outer(numpy.ones(p), Y)
    Z = numpy.multiply.outer(numpy.arange(p), numpy.ones(p))
    Z = numpy.multiply.outer(Z, numpy.ones(p))
    U = numpy.reshape(numpy.ravel((X, Y, Z)), (3, p**3))
    U = U[:, :n] * du + du / 2

    return U


# Initialize the box size
def initialize_box(n_atoms, rho):
    """This code block is unreadable
    """
    n = n_atoms
    p = int(numpy.floor(n**(1.0/3.0))) + 1
    box = (n/rho)**(1.0/3.0)
    du = box/p
    box = numpy.array([box]*3)

    return box


# Initialize random velocities
def initialize_velocities(U, T):
    """This code block is unreadable
    """

    #ACS numpy.random.seed(555)
    # Calculate random velocities
    # Make the sum of velocities zero
    (ndim, n) = numpy.shape(U)
    V = numpy.random.rand(ndim, n) - 0.5
    Vm = numpy.sum(V,1)/n

    V -= numpy.reshape(Vm, (ndim,1))

    # scale according to temperature
    fs = numpy.dot( numpy.ravel(V), numpy.ravel(V) ) / n 
    # the dot product of the velocities divided by the numbeer of particles
    fs = numpy.sqrt(ndim * T/fs)
    V *= fs

    return V


def initialize_particles(n_atoms, temperature, rho):

    U = initialize_positions(n_atoms, rho)
    box = initialize_box(n_atoms, rho)
    V = initialize_velocities(U, temperature)
    epot, F, Vir = fortran_lj(U,box)

    return U, V, F, box[0]


def lennard_jones(U, box):

    return fortran_lj(U, numpy.array([box,box,box]))



import numpy as np
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import matplotlib.animation as animation

"""
  Author:
    Jimmy Charnley Kromann <jimmy@charnley.dk>

  Usage:

  0) Import
    from particle_video3d import save_video

  1) Set the variables
    xframes, yframes, zframes
    box_width = 1.0
    filename = "week2solution"

  2) Call the function
    save_video(xframes, yframes, zframes, box_width, filename)

"""



def save_video3d_jimmy(X, Y, Z, box_width, filename):
  """
    Save a 3d video from x,y,z frames of a particle
    simulation.
  """

  # TODO Create array of marker size for every frame for every particle
  # size related to distance to the viewer

  video_frames = len(X)

  print "Creating plot ..."
  fig = plt.figure()
  fig.subplots_adjust(left=0, right=1, bottom=0, top=1)
  ax = fig.add_subplot(111, projection='3d', autoscale_on=False, 
                      xlim=(0.0, box_width),
                      ylim=(0.0, box_width),
                      zlim=(0.0, box_width))

  particles = ax.scatter(X[0], Y[0], Z[0])

  def init():
      """initialize animation"""
      fig.clear()
      ax = fig.add_subplot(111, projection='3d', autoscale_on=False, 
                          xlim=(0.0, box_width),
                          ylim=(0.0, box_width),
                          zlim=(0.0, box_width))
      particles = ax.scatter([], [], [])
      return particles

  def animate(i):
      """perform animation step"""
      fig.clear()
      ax = fig.add_subplot(111, projection='3d', autoscale_on=False, 
                          xlim=(0.0, box_width),
                          ylim=(0.0, box_width),
                          zlim=(0.0, box_width))
      particles = ax.scatter(X[i], Y[i], Z[i])
      return particles

  print "Creating animation ..."
  # Create the animation object
  ani = animation.FuncAnimation(fig, animate, frames=video_frames,
                                interval=10, blit=True, init_func=init)

  print "Generating video ..."
  # Save the animation to disk
  # Change fps for another framerate
  ani.save(filename+'.mp4', fps=35)

  print "Done!"

def save_3dvideo(U_frames, box_width, filename):

    output_x_frames = []
    output_y_frames = []
    output_z_frames = []

    print "Converting coordinates ..."

    for U in U_frames: 

        # print
        #print "U", U[0]
        #print "N", np.floor(U[0]/box_width)
        #print "T", U[0] - box_width * np.floor(U[0]/box_width)

        output_x_frames.append((U[0] - box_width * np.floor(U[0]/box_width)))  
        output_y_frames.append((U[1] - box_width * np.floor(U[1]/box_width)))
        output_z_frames.append((U[2] - box_width * np.floor(U[2]/box_width)))

    #exit()
    save_video3d_jimmy(output_x_frames,
                 output_y_frames,
                 output_z_frames,
                 box_width,
                 filename)


