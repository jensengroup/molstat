#!/usr/bin/env python

# Calculate standard gravity g from pendulum data

import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt


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

xfit = np.linspace(0.0, 500)
yfit = np.array([linear(x,  values[0], values[1]) for x in xfit])

plt.plot(xfit, yfit, label='fit')
plt.legend(loc='upper left')
plt.savefig("test.png")

a = values[0]
b = values[1]
T = values[0]*2
L = 14.35

# g = \left( \frac{2\pi}{T} \right)^2 \cdot L \label{eq:Pendul_g}
g = (2*np.pi/T)**2*L

print "T = {0:5.2f}".format(T)
print "g = {0:5.2f}".format(g)


# Error distribution

time_error = []

# TODO JCK
# hmm, wrong
# we need to check if [i+1] - [i] == a ?

for i, t in enumerate(times):
    time_error.append(t - (i+1)*a - b)


plt.clf()
num_bins = 15
# the histogram of the data
n, bins, patches = plt.hist(time_error, num_bins)
# add a 'best fit' line
# y = mlab.normpdf(bins, mu, sigma)
# plt.plot(bins, y, 'r--')

print len(times)

plt.savefig('hist')

plt.clf()
plt.plot(xdata, time_error)
plt.savefig('error.png')


