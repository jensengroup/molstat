import matplotlib.pyplot as plt
import sys

# See chemical shift exercise for explanation of sys.argv
native_filename = sys.argv[1]
non_native_filename = sys.argv[2]

native_lines = open(native_filename,"r").readlines()
non_native_lines = open(non_native_filename,"r").readlines()

native_rmsd = [line.split()[0] for line in native_lines]
native_data = [line.split()[1] for line in native_lines]

non_native_rmsd = [line.split()[0] for line in non_native_lines]
non_native_data = [line.split()[1] for line in non_native_lines]

plt.plot(non_native_rmsd,non_native_data,".k",markeredgecolor='k')
plt.plot(native_rmsd,native_data,".r",markeredgecolor='r')
plt.savefig("rmsd_E.png")
