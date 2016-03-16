
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

