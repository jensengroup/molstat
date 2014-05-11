#!/usr/bin/env python

import numpy as np
import copy
import matplotlib.pyplot as plt
import md_header as md
import video3d

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
n_steps     = 20000
temperature = 2.0
n_atoms     = 40
rho         = 0.1
dt          = 0.001

# Save frequency
save_freq = 10


# Initialize simulation
R, V, F, box_size = md.initialize_particles(n_atoms, temperature, rho)

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
    potential_energy, F, vir = md.lennard_jones(R, box_size)

    # Step 3: Calculate new velocities
    V += 0.5*(F + F0)*dt

    if n % save_freq == 0:

        # Calculate properties
        kinetic_energy = calc_kinetic(V)
        total_energy = kinetic_energy + potential_energy
        temperature = calc_temperature(V)
        pressure = rho*temperature + 1.0/(3.0*box_size**3)*vir + p_tail

        ek_list.append(kinetic_energy)
        ep_list.append(potential_energy)
        et_list.append(total_energy)
        pr_list.append(pressure)
        te_list.append(temperature)

        print "{0:6d} {1:8.2f} {2:8.2f}".format(n, total_energy, potential_energy)

        # Add frame to video
        if save_video:
            video3d.add_frame(R)


# Create plots
plt.title("Energy versus time")
plt.xlabel("Simulation step")
plt.ylabel("Energy")
plt.grid(True)
plt.plot(ek_list, 'r-', label="kinetic")
plt.plot(ep_list, 'b-', label="potential")
plt.plot(et_list, 'g-', label="total")
plt.legend()
plt.savefig("energy.png")

plt.clf()

plt.title("Pressure versus time")
plt.xlabel("Simulation step")
plt.ylabel("Pressure")
plt.grid(True)
plt.plot(pr_list, 'b-')
plt.savefig("pressure.png")

plt.clf()

plt.title("Temperature versus time")
plt.xlabel("Simulation step")
plt.ylabel("Temperature")
plt.grid(True)
plt.plot(te_list, 'b-')
plt.savefig("temperature.png")

plt.clf()

print box_size

# Remember not to save a video
# for large n_steps
if save_video:
    video3d.save(box_size, 'solution_4')


