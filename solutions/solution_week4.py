#!/usr/bin/env python

# python modules
import numpy as np
import copy

# local modules
import md_header as md
import md_video as video


def calc_kinetic(V):
    """ Calculate kinetic energy
    """
    return np.sum(V*V)*0.5


def calc_temperature(V):
    """ Calculate temperature
    """
    return np.mean(V*V)


def simulation(n_atoms, n_steps, rho, temperature, dt,
               eps = [],
               save_freq=60,
               video_filename='',
               constant_temperature=False):

    n_eq = 200*save_freq

    if video_filename != '':
        save_video = True


    if len(eps) == 0:
        eps = np.ones((n_atoms, n_atoms))
    else:
        # set particle 1 and 2 to other color
        colors = ['#4daf4a' for _ in range(n_atoms)]
        colors[0] = "#377eb8"
        colors[1] = "#377eb8"
        video.add_color(colors)



    # Initialize simulation
    R, V, F, box_width = md.initialize_particles(n_atoms, temperature, rho, eps)

    print 'Initialized'

    # # Calculate the tail correction
    # p_tail = 16.0/3.0 * np.pi * rho * (2.0/3.0 * (2.5**-9) - (2.5**-3))

    # Storage arrays
    ek_list = [] # Kinetic energy
    ep_list = [] # Potential energy
    et_list = [] # Total energy
    # pr_list = [] # Pressure
    te_list = [] # Temperature
    r_list = [] # distance list


    # Run simulation for n_steps
    for n in range(n_steps + 1):

        # Step 1: Calculate new positions
        R += V*dt + 0.5*F*dt*dt

        # Step 2: Calculate new forces
        F0 = copy.copy(F)
        potential_energy, F = md.lennard_jones(R, box_width, eps)

        # Step 3: Calculate new velocities
        V += 0.5*(F + F0)*dt

        # if temperture is set to constant, then scale the velocities
        if constant_temperature:
            V = md.scaletemp(V, temperature)


        # for every save_freq steps
        if n % save_freq == 0 and n > n_eq:

            print "step:", n

            # Calculate properties
            kinetic_energy = calc_kinetic(V)
            total_energy = kinetic_energy + potential_energy
            temperature = calc_temperature(V)
            # pressure = rho*temperature + 1.0/(3.0*box_width**3)*vir + p_tail


            ek_list.append(kinetic_energy)
            ep_list.append(potential_energy)
            et_list.append(total_energy)
            # pr_list.append(pressure)
            te_list.append(temperature)


            # calculate the distance between 0 and 1
            X  = R[0, 0] - R[0, 1]
            Y  = R[1, 0] - R[1, 1]

            # Periodic boundary condition
            X  -= box_width * np.rint(X/box_width)
            Y  -= box_width * np.rint(Y/box_width)
            d = np.sqrt(X**2 + Y**2)
            r_list.append(d)


            # Add frame to video
            if save_video:
                video.add_frame(R[0], R[1])


    # Remember not to save a video for large n_steps
    if save_video:
        video.save(video_filename, box_width, periodic_boundary=True)


    return ek_list, ep_list, et_list, te_list, r_list


