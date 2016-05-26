
from numpy import *
from numba import jit

def mandel(n, m, itermax, xmin, xmax, ymin, ymax):
    """
        Create a mandelbrot plot

        @value n,
        @value m,
        @value itermax,
        @value xmin,
        @value xmax,
        @value ymin,
        @value ymax,

        @return img
    """
    ix, iy = mgrid[0:n, 0:m]
    x = linspace(xmin, xmax, n)[ix]
    print x.shape
    y = linspace(ymin, ymax, m)[iy]
    c = x+complex(0,1)*y
    del x, y
    img = zeros(c.shape, dtype=int)
    ix.shape = n*m
    iy.shape = n*m
    c.shape = n*m
    z = copy(c)
    for i in xrange(itermax):
        if not len(z): break
        multiply(z, z, z)
        add(z, c, z)
        rem = abs(z)>2.0
        img[ix[rem], iy[rem]] = i+1
        rem = -rem
        z = z[rem]
        ix, iy = ix[rem], iy[rem]
        c = c[rem]
    return img


from pylab import *
import time
start = time.time()
I = mandel(1000, 1000, 100, -2, .5, -1.25, 1.25)
print 'Time taken:', time.time()-start
I[I==0] = 101
img = imshow(I.T, origin='lower left', cmap='cubehelix')
img.write_png('mandel.png', noscale=True)

