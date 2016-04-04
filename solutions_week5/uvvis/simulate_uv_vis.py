import matplotlib.pyplot as plt
import numpy as np
import math


### Physical Constants
NA=6.02214199*10**23 # avogadros number
c=299792458 # speed of light
e=1.60217662*10**(-19) # electron charge
me=9.10938*10**(-31) # electron mass
pi=math.pi
epsvac=8.8541878176*10**(-12) # vacuum permittivity
h=4.13566733*10**(-15) # plancks constant in eV*s


def uvvis(wavelengths, transition_list, oscillator_list):
    """
    Calculate the spectra for transitions and oscillators for a specific range
    of wavelengths.

    Parameters:
    wavelengths -- array of wavelengths to be calculated
    transition_list -- list of transitions (in nm)
    oscillator_list -- list of oscillators

    Returns:
    epsilon_whole_range -- list of absorption for the investigated range of  wavelengths

    """

    k = (NA*e**2)/(np.log(10)*2*me*c**2*epsvac)*np.sqrt(np.log(2)/pi)*10**(-1)

    epsilon_whole_range = []

    # convert transitions from eV to nm via e=hc/lambda
    for l in range(len(transition_list)):
         transition_list[l] = 10**9*h*c/transition_list[l]

    for i in range(len(wavelengths)):

        # list for intensities at the investigated wavelength
        epsilon_single_lambda = []

        for j in range(len(transition_list)):
            # in the following the intensity pr. transistion at wavelengths[i]
            # is calculated and appended to lidt epsilon_single_lambda

            # the total intensity at the wavelength lambda from all transistions
            eps = k*(oscillator_list[j]/sigmacm)*np.exp(-4*np.log(2)*((1/wavelengths[i]-1/transition_list[j])/(sigmacm*10**(-7)))**2)

            # list of the intensity pr. transition
            epsilon_single_lambda.append(eps)

        # the sum of the calculated transistions aka total absorption intensity
        inten = sum(epsilon_single_lambda)

        # list of the total absorption intensities
        epsilon_whole_range.append(inten)

    return epsilon_whole_range


# Set up parameters for spectra
#full width half maximum in eV
sigmaeV=0.4
# and in reciprocal cm
sigmacm=sigmaeV*8065.544 

#number of points to be calculated
N=500 
#range of wavelengths to be investigated
wavelengths = np.linspace(200, 700, N, endpoint=True)

# Load Data
f=open("data1_uv_vis.dat","r")

transition_list1 = []
oscillator_list1 = []

for line in f:
    line = line.split() # split line (string) into a line (list) for every space
    t = float(line[0]) #load the transition energy
    o = float(line[1]) # load the oscillator strength
    transition_list1.append(t)
    oscillator_list1.append(o)

g = open("data2_uv_vis.dat","r")

transition_list2 = []
oscillator_list2 = []

for line in g:
    line = line.split() # split line (string) into a line (list) for every space
    t = float(line[0]) #load the transition energy
    o = float(line[1]) # load the oscillator strength
    transition_list2.append(t)
    oscillator_list2.append(o)


# Calculate uvvis  using the function
y1 = uvvis(wavelengths,transition_list1,oscillator_list1)
y2 = uvvis(wavelengths,transition_list2,oscillator_list2)

#plot the uvvis data of the two chromophores
plt.plot(wavelengths,y1,label='Chromophore1', color='b')
plt.plot(wavelengths,y2,label='Chromophore2', color='r')
plt.legend()
plt.grid(True)
plt.title('UV-vis spectra',fontsize=20)
plt.xlabel('Wavelength (nm)',fontsize=16)
plt.ylabel(r'$\varepsilon$ (L/(mol cm))',fontsize=16)
plt.savefig('uvvis.png')
