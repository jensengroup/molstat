#!/usr/bin/env python

# Calculate standard gravity g from pendulum data

import numpy as np


no_datapoints = 5000
period = 7.0

# noise = np.random.normal(0.0, 1.0, no_datapoints)

time = 65.0

print 1, time

for i in xrange(1, no_datapoints):

        time += np.random.normal(0.0, 0.5)  + period/2.0
        print i, time

