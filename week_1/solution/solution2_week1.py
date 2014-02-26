import random
import pylab
import video

n_particles = 100
n_steps = 2000
dt = 0.001

pos_x = [random.random() for i in range(n_particles)]
pos_y = [2*random.random()-1 for i in range(n_particles)]
vel_x = [2*random.random()-1 for i in range(n_particles)]
vel_y = [2*random.random()-1 for i in range(n_particles)]

#pylab.plot(pos_x,pos_y, "ro")
#pylab.axis((-1, 1, -1, 1))
#pylab.quiver(pos_x,pos_y,vel_x,vel_y)


for n in xrange(n_steps):
    for i in range(n_particles):
        if abs(pos_x[i]+vel_x[i]*dt) >= 1:
            vel_x[i] *= -1
        if abs(pos_y[i]+vel_y[i]*dt) >= 1:
            vel_y[i] *= -1
        pos_x[i] += vel_x[i]*dt 
        pos_y[i] += vel_y[i]*dt
    if n % 10 == 0:
        video.add_frame(pos_x, pos_y)

video.save("week1_video")
#pylab.plot(pos_x,pos_y, "bo")
#pylab.savefig("coordinates_start.png")
