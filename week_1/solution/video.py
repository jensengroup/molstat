import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

"""
particle_video.py
@author jimmy@charnley.dk

Usage:
  1) Save particle_video.py in the same folder as your python program 
     and import the module

  from particle_video import save_video

  2) Initialize two lists to contain the frames

  xframes = []
  yframes = []

  3) For every frame append current coordinates for the 
     particles

  xframes.append(X)
  yframes.append(Y)

  4) Save the video with the imported function

  save_video(xframes, yframes, 'my_video')

  and a video will be saved as my_video.mp4

"""

def save_video(X, Y, box_width, filename):
  """
    Takes 2D coordinates X[i] and Y[i], saves it into
    filename.mp4 with len(X) steps.
  """

  # Variables
  #box_width = 10.0
  video_frames = len(X)

  # Setup figure
  fig = plt.figure()
  fig.subplots_adjust(left=0, right=1, bottom=0, top=1)
  ax = fig.add_subplot(111, aspect='equal', autoscale_on=False,
                      xlim=(-(box_width+1.2), (box_width+1.2)), ylim=(-(box_width+0.4), box_width+0.4))

  # Particles holds the locations of the particles
  particles, = ax.plot([], [], 'ko', ms=6)

  # Set an Retangle around the box
  rect = plt.Rectangle((-box_width, -box_width), 2*box_width, 2*box_width, fill=False, linewidth=2.0, edgecolor='k')
  ax.add_patch(rect)

  # Remove default axis for cinematic effect
  plt.axis('off')

  def init():
      """initialize animation"""
      particles.set_data([], [])
      return particles

  def animate(i):
      """perform animation step"""
      particles.set_data(X[i], Y[i])
      return particles

  # Create the animation object
  ani = animation.FuncAnimation(fig, animate, frames=video_frames,
                                interval=10, blit=True, init_func=init)

  # Save the animation to disk
  # Change fps for another framerate
  ani.save(filename+'.mp4', fps=25)

if(__name__ == "__main__"):
  """
    Animation selftest
  """
  n_particles = 20

  X = []
  Y = []

  for _ in xrange(400):
    X.append(np.array([np.random.random() for i in range(n_particles)]) * 10.0)
    Y.append(np.array([2 * (np.random.random() - 0.5) for i in range(n_particles)]) * 10.0)

  save_video(X, Y, 10.0, 'random_particles')

