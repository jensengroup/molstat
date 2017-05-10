# Example 2
import matplotlib.pyplot as plt

# Indentation and looping
# Point out that [] are for list and () for "functions"

a = 5
# a = 5 # error

#

my_list = [2.0, 4.0, 8.0]

for x in my_list:
    print 'x', x**2

print my_list # Nothing is change

# Range function

print range(5)
print range(2, 5)
# help(range)

x_list = range(1, 11)

y_list = [] # empty list
for x in x_list:
    y = x**2
    y_list.append(y)

y_list = [x**2 for x in x_list]

plt.plot(x_list, y_list)
plt.savefig('first_plot.png')


# SUM EXAMPLE
my_list = range(1, 51)
K = 0

for j in my_list:
    K = K + j**2

print K

# Easier way?

