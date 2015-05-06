import math
import numpy as np
import matplotlib.pyplot as plt

def make_step(x1, y1, x2, x3):
    i, j = np.random.uniform(-1,1,2)

    distance2 = i**2 + j**2

    if distance2 < 1:
        x1.append(i)
        y1.append(j)
        return 1
    else:
        x2.append(i)
        y2.append(j)
        return 0


n_steps = 100000
x1, y1, x2, y2 = [],[],[],[]

count = 0
for n in range(n_steps):
    count += make_step(x1,y1,x2,y2)


# Area of circle A_c = pi * r^2
# Area of square A_s = 4
# r = 1
# pi = 4 * A_c/A_s
pi = 4* float(count)/n_steps

print pi, pi - np.pi

plt.plot(x1,y1,"rx", alpha=0.1)
plt.plot(x2,y2,"bx",alpha=0.1)
#circle = plt.Circle((0,0),0.1,color='r') # need subplots for drawing circle
#plt.axis([-1,1,-1,1])
plt.axis('image') # or set axis explicitly and use 'scaled'
plt.savefig('circle')


