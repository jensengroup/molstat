
import solution_week4 as sim
import numpy as np
import matplotlib.pyplot as plt

## SIMULATION CONSTANTS

n_steps = 500000

# temperature = 0.05
# temperature = 0.1
temperature = 0.13
# temperature = 2.0

n_atoms = 42
rho = 0.2
dt = 0.0005

# Save frequency
save_freq = 1000


epss = np.ones((n_atoms, n_atoms))
for i in range(n_atoms):
    for j in range(n_atoms):
        if i > j:

            epss[i,j] = 0.1

            if j <= 1:
                epss[i,j] = 0.1

            if i <= 1 and j <= 1:
                epss[i,j] = 0.8



ek_list, ep_list, et_list, te_list, r_list = sim.simulation(n_atoms, n_steps, rho, temperature, dt,
               eps = epss,
               save_freq=save_freq,
               video_filename='week4simulation',
               constant_temperature=True)



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


plt.title("Temperature versus time")
plt.xlabel("Simulation step")
plt.ylabel("Temperature")
plt.grid(True)
plt.plot(te_list, 'b-')
plt.savefig("temperature.png")

plt.clf()


plt.title("Binding versus time")
plt.xlabel("Simulation step")
plt.ylabel("Distance")
plt.grid(True)
plt.plot(r_list, 'b-')
plt.savefig("distance.png")

plt.clf()


# calculate free energy

nn = 0
nb = 0
r_bound = 1.52

for x in r_list:

    if x > r_bound:
        nn += 1

    else:
        nb += 1


k = float(nb) / float(nn)

print k







