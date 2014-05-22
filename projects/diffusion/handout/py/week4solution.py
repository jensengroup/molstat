import numpy as np
import pylab
import copy
from md_header import initialize_particles, lennard_jones, save_3dvideo

#from particle_video3d import save_video


def calc_ekin(V):
    return np.sum(V*V) * 0.5

def calc_temperature(V):
    return np.mean(V*V)

n_steps = 10000
save_freq = 50
video = 0

temperature = 0.5
n_atoms = 100
rho = 0.7
dt = 0.001

np.random.random(555)

R, V, F, box_width = initialize_particles(n_atoms,       # n_atoms
                                          temperature,   # temperature
                                          rho)           # rho

#print R, box_width
#exit()

R_frames = []
R_frames.append(R)
k_list = []
p_list = []
t_list = []
te_list = []
pr_list = []


p_tail =  16.0/3.0 * np.pi * rho *( 2.0/3.0 * (2.5**-9) - (2.5**-3))

print "p_tail", p_tail

for n in range(n_steps+1):

    # Step 1: Calculate new positions
    R = R + V * dt + 0.5 * dt * dt * F

    # Step 2: Calculate new forces
    F_old = copy.deepcopy(F)
    e_pot, F, k_vir = lennard_jones(R, box_width)

    # Step 3: Calculate new velocities
    V = V + 0.5 * dt * (F + F_old)

    e_kin = calc_ekin(V)
    T = calc_temperature(V)
    e_kin = calc_ekin(V)
    e_tot = e_kin + e_pot

    p = rho * T + 1.0/(3.0 * box_width**3) * k_vir + p_tail

    # Print output
    if (n % save_freq == 0 ):
        print n, e_pot, e_kin, e_tot, T
        R_frames.append(R)
        k_list.append(e_kin)
        p_list.append(e_pot)
        t_list.append(e_tot)
        te_list.append(T)
        pr_list.append(p)

pylab.title("Energy versus time")
pylab.xlabel("Simulation step")
pylab.ylabel("Energy")
pylab.grid(True)
pylab.plot(k_list, 'r-', label= "kinetic")
pylab.plot(p_list, 'b-', label= "potential")
pylab.plot(t_list, 'g-', label = "total")
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

if video:
    save_3dvideo(R_frames, box_width, "lol")




