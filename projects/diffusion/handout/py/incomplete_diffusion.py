import numpy as np
import pylab
import copy
from md_header import initialize_particles, lennard_jones
from scipy import stats


def calculate_msd(R1, R2):
    """ Calculate MSD between two position matrices R1 and R2
    """
    # TODO Finish function
    msd = 0.0
    return msd


def calculate_vacf(V1, V2):
    """ Calculate VACF between two velocity matrices V1 and V2
    """
    # TODO Finish function
    vacf = 0.0
    return vacf


def calculate_temperature(V):
    """ Calculate temperature from a velocity matrix
    """
    return np.mean(V*V)


def limit_msd(time_list, msd_list):
    """ Calculate diffusion coeffcient from a time and msd list.
    """
    slope, intercept, r_value, p_value, std_err = stats.linregress(time_list, msd_list)
    return slope


def integrate_vacf(time_list, vacf_list):
    """ Calculate the integration of vacf
        by numerical integration
    """
    # TODO Finish function
    I = 0.0
    return I


def velo_verlet(R, V, F, box_width, dt):
    """ Take a velo verlet step
    """
    # Step 1: Calculate new positions
    R = R + V * dt + 0.5 * dt * dt * F

    # Step 2: Calculate new forces
    F_old = copy.deepcopy(F)
    e_pot, F, k_vir = lennard_jones(R, box_width)

    # Step 3: Calculate new velocities
    V = V + 0.5 * dt * (F + F_old)

    return R, V, F


def simulation(n_particles, temperature, rho, equilib_steps, n_steps, sampling_freq, dt):
    """ Run a simulation of lennard jones fluid
    """
    # TODO Finish function
    R, V, F, box_width = initialize_particles(n_particles, temperature, rho)

    return


# Simulation Constants
n_particles = 108
temperature = 0.5
rho = 0.7
equilib_steps = 10000
n_steps = 10000
sampling_freq = 24
dt = 0.001

# TODO Run simulation

simulation(n_particles, temperature, rho, equilib_steps, n_steps, sampling_freq, dt)

