
# Example: Operator

# example floats

c = 5.0
# c = c + 5
c += 5.0
print c

c /= 2.0
print c

c *= 2.0
print c


# example lists

x_list = [1.0, 4.0, 8.0]
n_particles = 3

for i in range(n_particles):

    x_list[i] = x_list[i] + 1.0

    x_list[i] += 1.0

print x_list


