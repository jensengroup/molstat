import numpy as np
import matplotlib.pyplot as plt

def gaussian(x, y):
    """ Gaussian function in 2 dimensions """

    A = 1.0

    sigma_x = 1.0
    sigma_y = 2.0
    x_o = 0.0
    y_o = 0.0

    z =  A*np.exp( - (x - x_o)**2/(2*sigma_x**2) - (y - y_o)**2/(2*sigma_y**2) )

    return z


X = np.arange(-5, 5, 0.1)
Y = np.arange(-5, 5, 0.1)

Nx = len(X)
Ny = len(Y)

Z = np.zeros((Nx, Ny))

# iterate over X and Y and fill out Z
for i in range(Nx):

    for j in range(Ny):

        Z[i][j] = gaussian(X[i], Y[j])


# set a mark to 1.0 to see if the image is orientated properly
Z[-1][-1] = 1.0


# Create the axis
extent = [X[0], X[-1], Y[0], Y[-1]]

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


