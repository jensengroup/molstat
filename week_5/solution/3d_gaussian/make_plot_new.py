import numpy as np
import matplotlib.pyplot as plt

f = open('2d_data')

x, y = [], []
for line in f:
    tokens = line.split()
    x.append(tokens[0])
#    y.append(tokens[1])

data = np.loadtxt('2d_data', dtype=np.float)

h,a,b = np.histogram2d(data[:,0], data[:,1], [10,10])

hmasked = np.ma.masked_where(h==0,h)

plt.imshow(a,b,hmasked)
plt.show()
# Create the axis
extent = [min(x), max(x), min(y), max(y)]

# Plot the Z matrix
im = plt.imshow(Z,
                interpolation='nearest', # Does not anti aliasing squares
                extent=extent,           # Use the defined axis
                aspect='auto',
                origin='lower',          # Corrects the origin
                cmap='gray')             # Colormap


# create colorbar
cbar = plt.colorbar(im)
cbar.set_label('Probability [$p(x,y)$]', rotation=270)


plt.xlabel('$x$')
plt.ylabel('$y$')

plt.savefig('figure_mesh.png')
plt.clf()


# Make a scan

for i in range(Nx):

    # computational numeric uncertainty
    if abs(X[i] + 1.0) < 0.00001:

        index = i


scan_list = []

for i in range(Ny):

    scan_list.append(Z[index][i])

plt.plot(Y, scan_list)
plt.savefig('scanned.png')


