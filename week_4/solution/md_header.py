import numpy
import time
import copy


from forces import lennardjones as fortran_lj


def initialize_positions(natms, rho):
    """ Initialize particle positions, based on number of atoms and density rho
    """
    n = natms
    p = int(numpy.floor(n**(1.0/3.0))) + 1
    box = (n/rho)**(1.0/3.0)
    du = box/p
    X = numpy.multiply.outer(numpy.ones(p), numpy.arange(p))
    X = numpy.multiply.outer(numpy.ones(p), X)
    Y = numpy.multiply.outer(numpy.arange(p), numpy.ones(p))
    Y = numpy.multiply.outer(numpy.ones(p), Y)
    Z = numpy.multiply.outer(numpy.arange(p), numpy.ones(p))
    Z = numpy.multiply.outer(Z, numpy.ones(p))
    U = numpy.reshape(numpy.ravel((X, Y, Z)), (3, p**3))
    U = U[:, :n] * du + du / 2
    return U


def initialize_box(n_atoms, rho):
    """ Initialize the box
    """
    n = n_atoms
    p = int(numpy.floor(n**(1.0/3.0))) + 1
    box = (n/rho)**(1.0/3.0)
    du = box/p
    box = numpy.array([box]*3)
    return box


def initialize_velocities(U, T):
    """ Initialize random velocities
    """
    # Calculate random velocities
    # Make the sum of velocities zero
    ndim, n = numpy.shape(U)
    V = numpy.random.rand(ndim, n) - 0.5
    Vm = numpy.sum(V,1)/n
    V -= numpy.reshape(Vm, (ndim,1))

    # scale according to temperature
    fs = numpy.dot( numpy.ravel(V), numpy.ravel(V) ) / n

    # the dot product of the velocities divided by the number of particles
    fs = numpy.sqrt(ndim * T/fs)
    V *= fs

    return V


def initialize_particles(n_atoms, temperature, rho):
    """ Initialize particles
    """

    U = initialize_positions(n_atoms, rho)
    box = initialize_box(n_atoms, rho)
    V = initialize_velocities(U, temperature)
    epot, F, Vir = fortran_lj(U,box)

    return U, V, F, box[0]


def lennard_jones(U, box):

    return fortran_lj(U, numpy.array([box,box,box]))


