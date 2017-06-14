#!/usr/bin/env python

import numpy as np
import copy

from numba import double, jit, autojit

# from forces import lennardjones as fortran_lj


def initialize_positions(n, rho, d):
    """
    Initialize particle positions, based on number of atoms and density rho

    n number of particles
    rho particle density (n/box_width**d)
    d number of dimensions

    TODO redo in dimensions!

    """

    # TODO Clean and make it numpy

    npl = int(np.ceil( n**(1.0/float(d)) ))

    # rho = n / volume = n / box_width**dimension
    box_width = (n/rho)**(1.0/float(d))

    dr = box_width / npl

    X = []
    Y = []

    for j in range(npl):
        X += [i for i in range(npl)]
        Y += [j for i in range(npl)]

    # Remove excess particles.
    X = X[:n]
    Y = Y[:n]

    X = np.array(X)*dr + dr/2.0
    Y = np.array(Y)*dr + dr/2.0

    # shift 0 and 1 to center of box instead
    X = np.roll(X, int(np.floor(n/2)+npl/2))
    Y = np.roll(Y, int(np.floor(n/2)+npl/2))


    # for -box_width, box_width
    # but this is wrong volume
    # X = (X - 0.5*(npl-1))*1.0/npl*box_width*1.8
    # Y = (Y) * 1.0/npl*box_width*0.8

    R = np.array([X, Y])

    return R, box_width


def swap_particles(frm, to, R):
    """
    Swap positions between particle i and j
    """
    R[:,[frm, to]] = R[:,[to, frm]]


def initialize_velocities(R, T):
    """
    Initialize random velocities
    """

    # Calculate random velocities
    # Make the sum of velocities zero
    d, n = np.shape(R)
    V = np.random.rand(d, n) - 0.5
    Vm = np.sum(V,1)/n
    V -= np.reshape(Vm, (d,1))

    V = scaletemp(V, T)

    # # the dot product of the velocities divided by the number of particles
    # fs = np.dot( np.ravel(V), np.ravel(V) ) / n
    #
    # # scale according to temperature
    # fs = np.sqrt(n * T/fs)
    # V *= fs


    return V


def lennard_jones(R, box_width, eps):
    """
    """

    energy_potential, forces = force(R, box_width, eps)


    return energy_potential, forces


# Constants
rc = 2.5 # cut-off distance
rc2 = rc**2
rc2i = 1.0/rc2
rc6i = rc2i*rc2i*rc2i
ecut = rc6i*(rc6i-1.0)


#@jit(argtypes=[double[:,:], double, double[:,:]])
@jit()
def force(R, box_width, eps):
    """
    Calculate the force of U given a box, for periodic boundary conditions
    """

    n_dim, n_part = np.shape(R)
    F = np.zeros((n_dim, n_part))

    epot = 0.0
    vir = 0.0

    for i in range(n_part):
        for j in range(n_part):
            if i > j:

                X  = R[0, j] - R[0, i]
                Y  = R[1, j] - R[1, i]

                # Periodic boundary condition
                X  -= box_width * np.rint(X/box_width)
                Y  -= box_width * np.rint(Y/box_width)

                # Distance squared
                r2 = X*X + Y*Y

                if r2 < rc2:
                    r2i = 1.0 / r2
                    r6i = r2i*r2i*r2i
                    epot += eps[i,j]*r6i*(r6i-1.0) - ecut
                    ftmp = eps[i,j]*48.0 * r6i*(r6i-0.5) * r2i

                    F[0, i] -= ftmp * X
                    F[1, i] -= ftmp * Y
                    F[0, j] += ftmp * X
                    F[1, j] += ftmp * Y

                    vir += ftmp

    epot = epot * 4.0

    return epot, F



def scaletemp(V, temp):
    """
    Scale velocities V to a certain temperature temp
    """

    # current temperature(t)
    temp_t = np.mean(V*V)

    # calculate scaling factor
    scale = np.sqrt(temp/temp_t)
    V *= scale

    return V


def initialize_particles(n_atoms, temperature, rho, eps=[]):
    """
    Initialize particles
    """
    dimension = 2

    R, box_width = initialize_positions(n_atoms, rho, dimension)
    V = initialize_velocities(R, temperature)

    # swap particles
    # swap_particles(0, np.random.randint(n_atoms), R)
    # swap_particles(1, np.random.randint(n_atoms), R)

    Epot, F = lennard_jones(R, box_width, eps)

    return R, V, F, box_width


if __name__ == '__main__':

    print "Header self-test"


