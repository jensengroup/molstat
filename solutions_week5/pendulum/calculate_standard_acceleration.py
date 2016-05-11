#!/usr/bin/env python

# Calculate standard gravity g from pendulum data

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import scipy.optimize as opt
from scipy.stats import norm


datafile = open('timer_gen.dat', 'r')

times = []

for line in datafile:

        line = line.strip()
        line = line.split()

        no = int(line[0])
        time = float(line[1])

        times.append(time)

        # print "Count number: {0:3.0f}    time measurement (s): {1:6.2f}".format(no, time)


xdata = range(1, len(times)+1)

plt.plot(xdata, times, '.')

# Calculate the period T from time data

def linear(x, a, b):
    return a*x + b

values, copt = opt.curve_fit(linear, xdata, times)

xfit = np.linspace(0.0, len(times))
yfit = np.array([linear(x,  values[0], values[1]) for x in xfit])

plt.plot(xfit, yfit, label='fit')
plt.legend(loc='upper left')
plt.savefig("test.png")

a = values[0]
b = values[1]
T = values[0]*2
L = 12.19

# g = \left( \frac{2\pi}{T} \right)^2 \cdot L \label{eq:Pendul_g}
g = (2*np.pi/T)**2*L

print "T = {0:5.2f}".format(T)
print "g = {0:5.2f}".format(g)


# Error distribution

time_error = [0.0]

# TODO JCK
# hmm, wrong
# we need to check if [i+1] - [i] == a ?

for i in xrange(1, len(times)):

    error = times[i] - times[i-1] - a
    time_error.append(error)

# for i, t in enumerate(times):
#     time_error.append(t - (i+1)*a - b)


# def f(x, a, b, c):
#     return a * np.exp(-(x - b)**2.0 / (2 * c**2))
#
# x = 
# y = time_error


plt.clf()
plt.plot(xdata, time_error, '.')
plt.savefig('error.png')


plt.clf()

num_bins = 15
n, bins, patches = plt.hist(time_error, num_bins, normed=1)

# Add a guassian fit
(mu, sigma) = norm.fit(time_error)
y = mlab.normpdf(bins, mu, sigma)
l = plt.plot(bins, y, 'g-', linewidth=2)

plt.title("Histogram of time measurment: $\mu =$ {0:4.2f}, $\sigma =$ {1:4.2f}".format(mu, sigma))


plt.grid(True)
plt.savefig('hist')


