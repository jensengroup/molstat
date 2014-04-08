import matplotlib.pyplot as plt
import numpy as np

# Data
x = np.arange(0, 14, 0.1)
y_cos = [np.cos(i) for i in x]
y_sin = [np.sin(i) for i in x]

# First plot
plt.plot(x, y_cos, 'r-')
plt.plot(x, y_sin, 'b-')

plt.savefig('figure_sincos1.eps')

# Clear MPL data
plt.clf()

# Second figure
plt.plot(x, y_cos, '-', label="Cos function")
plt.plot(x, y_sin, '.-', label="Sin function")

# Location of legend
plt.legend(loc='upper left')

plt.savefig('figure_sincos2.eps')


