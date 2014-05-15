import sys
import numpy as np
from scipy.stats import *
import matplotlib.pyplot as plt

filename = sys.argv[1]
y = []
data = np.loadtxt(filename,dtype=np.float)


fit_list = ["norm", "cauchy", "genlogistic", "hypsecant", "johnsonsu", "laplace", "logistic", "nct", "t", "dgamma", "dweibull"]
for dist in fit_list:
    plt.hist(data, normed=1, alpha = 0.2, bins=100)
    data_range =  np.linspace(1.0*min(data),1.0*max(data),1000)
    parameters = eval(dist+".fit(data, loc=0, scale=1)")
    y = eval(dist+".pdf(data_range, *parameters)")
    plt.plot(data_range, y, label=dist)
    plt.xlabel("Error in the chemical shift")
    plt.ylabel("Probability density")
    plt.legend()
    plt.savefig(dist+".png")
    plt.clf()

