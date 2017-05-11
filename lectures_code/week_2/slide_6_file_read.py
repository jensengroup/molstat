
import matplotlib.pyplot as plt

# Simple example
f = open('file', 'r')

for line in f:
    print line


# Bifurcation diagram

f = open('chaos.csv', 'r')

x = []
y = []

for line in f:

    line = line.split(',') #remember that this is updating the variable line
    x.append(float(line[0]))
    y.append(float(line[1]))


plt.plot(x, y, '.', color='k', markersize=0.1)
plt.xlabel('$r$')
# plt.ylabel("$\lim_{n \\rightarrow \infty} \, x$")
plt.ylabel("$x$")

plt.savefig('chaos3.png')

