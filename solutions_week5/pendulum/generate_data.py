#!/usr/bin/env python

import numpy as np

no_datapoints = 100

# length of pendulum
L = 12.188431786255023

# period
period = 7.0

# start time
time = np.random.uniform(0.0, 100.0)

sigma = 1.9

print 1, time

for i in xrange(1, no_datapoints):
        time += np.random.normal(0.0, sigma)  + period/2.0
        print i, time

