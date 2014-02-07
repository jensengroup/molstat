#!/usr/bin/env python

import numpy as np
import copy

import pylab

import video3d
from md_header import initialize_particles, lennard_jones


def calc_kinetic(V):
    """ Calculate kinetic energy
    """
    return np.sum(V*V)*0.5


def calc_temperature(V):
    """ Calculate temperature
    """
    return np.mean(V*V)


save_video = False

# Simulation constants
n_steps     = 10000
temperature = 0.5
n_atoms     = 40
rho         = 0.1
dt          = 0.001

# Save frequency
save_freq = 10

# Initialize simulation
R, V, F, box_size = initialize_particles(n_atoms, temperature, rho)

# Calculate the tail correction
p_tail = 16.0/3.0 * np.pi * rho * (2.0/3.0 * (2.5**-9) - (2.5**-3))

# Storage arrays
ek_list = [] # Kinetic energy
ep_list = [] # Potential energy
et_list = [] # Total energy
pr_list = [] # Pressure
te_list = [] # Temperature


# Run simulation for n_steps
for n in range(n_steps+1):

    # Step 1: Calculate new positions
    R += V*dt + 0.5*F*dt*dt

    # Step 2: Calculate new forces
    F0 = copy.copy(F)
    potential_energy, F, vir = lennard_jones(R, box_size)

    # Step 3: Calculate new velocities
    V += 0.5*(F + F0)*dt

    if n % save_freq == 0:

        # Calculate properties
        kinetic_energy  = calc_kinetic(V)
        total_energy    = kinetic_energy + potential_energy
        temperature     = calc_temperature(V)
        pressure        = rho * temperature + 1.0/(3.0 * box_size**3) * vir * p_tail

        ek_list.append(kinetic_energy)
        ep_list.append(potential_energy)
        et_list.append(total_energy)
        pr_list.append(pressure)
        te_list.append(temperature)

        print "%1 %2".format(n, total_energy)

        # Add frame to video
        # NOTE remove this line for large n_steps
        # video3d.add_frame(R)


# Create plots
pylab.title("Energy versus time")
pylab.xlabel("Simulation step")
pylab.ylabel("Energy")
pylab.grid(True)
pylab.plot(ek_list, 'r-', label= "kinetic")
pylab.plot(ep_list, 'b-', label= "potential")
pylab.plot(et_list, 'g-', label = "total")
pylab.legend()
pylab.savefig("energy.png")

pylab.clf()

pylab.title("Pressure versus time")
pylab.xlabel("Simulation step")
pylab.ylabel("Pressure")
pylab.grid(True)
pylab.plot(pr_list, 'b-')
pylab.savefig("pressure.png")

pylab.clf()

pylab.title("Temperature versus time")
pylab.xlabel("Simulation step")
pylab.ylabel("Temperature")
pylab.grid(True)
pylab.plot(te_list, 'b-')
pylab.savefig("temperature.png")

pylab.clf()

print box_size

# Remember not to save a video
# for large n_steps
if save_video:
    video3d.save(box_size, 'solution_4')


