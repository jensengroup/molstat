import pylab
import math
import numpy

x = range(1, 20)
y = [i**2 for i in x]

pylab.plot(x, y)
pylab.savefig('xy_figure.eps')


# Figure 2

pylab.clf()

x = range(1, 20)
y = [i**2 for i in x]

pylab.title('Wow, Nice Graph')
pylab.xlabel('kcal/mol')
pylab.ylabel('$\hat \lambda R^2$')


pylab.plot(x, y)
pylab.savefig('figure_title.eps')


pylab.clf()

x = range(1, 20)
y = [i**2 for i in x]

pylab.title('Wow, Nice Graph')
pylab.xlabel('kcal/mol')
pylab.ylabel('$\hat \lambda R^2$')

pylab.text(5, 200, r'$\mu=100,\ \sigma=15$')

pylab.plot(x, y)
pylab.savefig('figure_title_text.eps')



# Figure 3

pylab.clf()

x = numpy.arange(0, 14, 0.1)
y_cos = [math.cos(i) for i in x]
y_sin = [math.sin(i) for i in x]

pylab.plot(x, y_cos, 'r-')
pylab.plot(x, y_sin, 'b-')

pylab.savefig('figure_sincos1.eps')

# Next

pylab.clf()


x = numpy.arange(0, 14, 0.1)
y_cos = [math.cos(i) for i in x]
y_sin = [math.sin(i) for i in x]

pylab.plot(x, y_cos, 'r-', label="Cos function")
pylab.plot(x, y_sin, 'b-', label="Sin function")

pylab.legend(loc='upper left')

pylab.savefig('figure_sincos2.eps')



