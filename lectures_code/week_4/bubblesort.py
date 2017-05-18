import numpy as np
from numba import jit
import time

start = time.time()

#@jit() #uncomment to use the jit compiler for speed-up
def bubblesort(X):
    N = len(X)
    for end in range(N, 1, -1):
        for i in range(end - 1):
            
            cur = X[i]
            if cur > X[i + 1]:
                tmp = X[i]
                X[i] = X[i + 1]
                X[i + 1] = tmp
               

original = np.arange(0.0, 50.0, 0.01)
shuffled = original.copy()
np.random.shuffle(shuffled)

print original[0:10]
print shuffled[0:10]

sorted = shuffled.copy()
bubblesort(sorted)
print(np.array_equal(sorted, original))

print 'It took', time.time() - start, 'seconds'
