import matplotlib.pyplot as plt
import numpy as np
import math

###CONSTANTS####
NA=6.02214199*10**23 #avogadros number
c=299792458 #speed of light
e=1.60217662*10**(-19) #electron charge
me=9.10938*10**(-31) #electron mass
pi=math.pi
epsvac=8.8541878176*10**(-12) #vacuum permittivity
###
sigmaeV=0.4 #full width half maximum
sigmacm=sigmaeV*8065.544
###

k=(NA*e**2)/(np.log(10)*2*me*c**2*epsvac)*np.sqrt(np.log(2)/pi)*10**(-1)
l="{:.3E}".format(k)
print k,l

N=500
t=np.linspace(200, 700, N, endpoint=True)

def uvvis(t,l,f):
        lambda1=np.zeros(len(l))
        lambda_tot=np.zeros(len(t))
        for x in range(1,len(t)):
                for i in range(0,len(l)):
                        lambda1[i]=(k/sigmacm)*f[i]*np.exp(-4*np.log(2)*((1/t[x]-1/l[i])/(10**(-7)*sigmacm))**2)
                lambda_tot[x]=sum(lambda1)
        return lambda_tot

f=open("data_uv_vis.dat","r")

lambda_list = []
oscillator_list = []
for line in f:
  line=line.split() # split line (string) into a line (list) for every space
  l=float(line[1])
  o=float(line[2])
  lambda_list.append(l)
  oscillator_list.append(o)

print lambda_list,oscillator_list

y=uvvis(t,lambda_list,oscillator_list)

plt.plot(t,y,label=r'$SubPc_1$', color='b')
plt.legend()
plt.grid(True)
plt.title('UV-vis spectra',fontsize=20)
plt.xlabel('Wavelength (nm)',fontsize=16)
plt.ylabel(r'$\varepsilon$ (L/(mol cm))',fontsize=16)
plt.savefig('uvvis.png')
plt.show()

'''
Extra - plot with both epsilon and oscillator strength
fig,ax1 = plt.subplots()
fig.set_size_inches(18.5, 10.5, forward=True)
ax2 = ax1.twinx()
ax1.ticklabel_format(style='sci', axis='y', scilimits=(0,0),fontsize=14) 
ax1.ticklabel_format(axis='x', fontsize=14)
ax1.ticklabel_format(axis='y',fontsize=14)


ax1.set_xlabel('Wavelength (nm)',fontsize=16)
ax1.set_ylabel(r'$\varepsilon$ (L/(mol cm))',color='b',fontsize=16)
ax2.set_ylabel('Oscillator Strength', color='r',fontsize=16)

ax1.plot(t,y,label=r'$\varepsilon$ (L/(mol cm))', color='b')
ax2.bar(lambda_list,oscillator_list, label='Oscillator Strength',width=3,color='r')


plt.title('UV-vis spectra',fontsize=20)
ax1.legend(loc = (.8,0.95), frameon = False)
ax2.legend( loc = (.8, .9), frameon = False)
ax1.grid(True)
plt.savefig('eps_and_osc.png',dpi=100)
plt.show()
'''
