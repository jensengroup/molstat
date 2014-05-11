
# Example: More functions

# slide example

def f(x):
    b = 2.0
    return x*b

a = 2.0
print f(a)
print b # NameError: name 'b' is not defined
print a


# example x_pos

import random

def random_move(x_pos, n_particles):

    # x_pos is a local variable/argument

    for i in range(n_particles):

        # i, is even more local

        x_pos[i] += random.random()

    return x_pos

# ...

n_particles = 3
X = [1.0, 2.0, 4.0]

X = random_move(X, n_particles)

