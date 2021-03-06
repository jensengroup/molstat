# Example: Debug

# 01
# - multiple returns

def f(x, y):
    k = x**2
    l = x + y**2
    return k
    return l

#a, b = f(2.0, 2.0)
#print a, b


# 02
# - Local/Global variables
# - Wrong return
# - indent

import random

def random_move(x_pos, y_pos, n_particles):
    for i in range(n_particles):
        x_pos[i] += random.random()
        y_pos[i] += random.random()
    return y_pos, x_pos #wrong return

n_particles = 4
X = [random.random() for x in range(n_particles)]
Y = [random.random() for y in range(n_particles)]

for n in range(25):
    x_pos, y_pos = random_move(x_pos, y_pos, n_particles) #local variables
    # x_pos, y_pos = random_move(X, Y, n_particles) #still overwrites X and Y
    # since these are list and then identical to x_pos and y_pos


"""
# 03
# - wrong lists (not copy)
import random

def move(pos_x, n_particles):

    pos_x_old = pos_x
    dx = [0.0 for i in range(n_particles)]

    for i in range(n_particles):
        pos_x[i] += random.random()
        dx[i] = pos_x[i] - pos_x_old[i]

    return pos_x, dx

pos_x = [1.0, 5.0, 9.0]
print pos_x
pos_x, dx = move(pos_x, 3)
print pos_x
print dx
"""
