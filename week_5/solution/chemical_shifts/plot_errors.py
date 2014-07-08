import sys
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

# If the script is run as 'python plot_errors.py data_filename', sys.argv[1] will return data_filename
filename = sys.argv[1]

# Numpy alternative to open().
data = np.loadtxt(filename,dtype=np.float)

# Freedman-Diaconis rule for selecting binwidths
def bins(data) :
    data.sort()
    n = len(data)
    width = 2*(data[3*n/4] - data[n/4]) * n**(-1./3)
    return int((data[-1] - data[0]) / width)

#plot a histogram
plt.hist(data, normed=1, alpha = 0.2, bins=bins(data))
#make "x"-data-range for our probability function.
data_range =  np.linspace(min(data),max(data),1000)
#Fit parameters to the data
parameters = norm.fit(data)
#Create y-values for our data-range"
y = norm.pdf(data_range, *parameters)
#plot
plt.plot(data_range, y, label="Normal Distribution")
plt.xlabel("Error in the chemical shift")
plt.ylabel("Probability density")
plt.legend()
plt.savefig("norm.png")
plt.clf()

