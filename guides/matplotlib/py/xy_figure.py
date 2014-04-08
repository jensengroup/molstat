import matplotlib.pyplot as plt

x = range(1, 20)
y = [i**2 for i in x]

plt.plot(x, y)
plt.savefig('figure_xy.eps')

