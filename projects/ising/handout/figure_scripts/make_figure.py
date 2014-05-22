from __future__ import division
import numpy as np
import pylab
from data import sim_data

sim_data = np.array(sim_data).T

Tc = 2/(np.log(1 + np.sqrt(2)))

def m(T):

    value = (1.0 - np.sinh(2.0 / T)**(-4.0))**(0.125)

    if np.isnan(value):
        return 0.0

    return value

def cv(T):

    if T < Tc:
        return 2/np.pi * (2/Tc)**2 * ( - np.log(1 - T/Tc) + np.log(Tc/2) - (1+ np.pi/4))

    return 2/np.pi * (2/Tc)**2 * ( - np.log(- (1 - T/Tc)) + np.log(Tc/2) - (1+ np.pi/4))

def xi(T):

    if T <= Tc:
        P1 = 0.0000063457
        P3 = 1.74276
        return P1 * ((Tc - T)/Tc)**(-P3)

    else:
        P1 = 0.00077
        P3 = 1.0304
        return P1 * ((T-Tc)/Tc)**(-P3)



T = np.arange(1.0, 4.0, 0.005)

T_sim = np.arange(1.0, 4.05, 0.05)

M = []
Cv = []
Xi = []

for t in T:

    M.append(m(t))
    Cv.append(cv(t))
    Xi.append(xi(t))

pylab.figure(figsize=(5.6,5.6))
pylab.grid(True)
pylab.plot(T_sim, (sim_data[2]) * -1.0, label ="Simulation")
pylab.plot(T, M, 'r-', label="Analytical")
pylab.legend()
#pylab.title("Magnetization, N = 256, steps = 10,000,000")
pylab.xlabel("Temperature [kB]")
pylab.ylabel("Magnetization [S]")
pylab.savefig("mag_anal.png")
pylab.clf()

pylab.grid(True)
pylab.ylim([0.0, 3.5])
pylab.plot(T_sim, sim_data[0], label ="Simulation")
pylab.plot(T, Cv, 'r-', label="Analytical")
pylab.legend()
pylab.title("Heat Capacity, N = 256, steps = 10,000,000")
pylab.xlabel("Temperature [kB]")
pylab.ylabel("Heat Capacity [j/kB]")
pylab.savefig("cv_anal.png")
pylab.clf()

pylab.grid(True)
pylab.ylim([0,0.0012])
pylab.plot(T_sim, sim_data[1], label ="Simulation")
pylab.plot(T, np.array(Xi) * 0.01, 'r-', label="Analytical")
pylab.legend()
pylab.title("Magnetic Susceptibility, N = 256, steps = 10,000,000")
pylab.xlabel("Temperature [kB]")
pylab.ylabel("Susceptibility [S/kB]")
pylab.savefig("xi_anal.png")
pylab.clf()
