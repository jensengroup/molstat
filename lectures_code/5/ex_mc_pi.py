
import numpy as np
import matplotlib.pyplot as plt


def calculate_pi(n_steps, save_lists):


    if save_lists:
        x_red = []
        y_red = []
        x_green = []
        y_green = []

    count = 0

    for n in range(n_steps):

        # give as hint
        # call it x y
        i, j = np.random.uniform(-1, 1, 2)

        squared = i**2 + j**2

        if squared < 1.0:
            count += 1

            if save_lists:
                x_red.append(i)
                y_red.append(j)

        else:

            if save_lists:
                x_green.append(i)
                y_green.append(j)

    if save_lists:
        return count, x_red, y_red, x_green, y_green

    else:
        return count


count, x_red, y_red, x_green, y_green = calculate_pi(1000, True)

plt.plot(x_red, y_red, 'rx', alpha=0.1)
plt.plot(x_green, y_green, 'gx', alpha=0.1)
plt.axis('image')
plt.savefig('circle')
plt.clf()



step_list = []
pi_list = []

for n_steps in range(1000, 1000000, 10000):

    print n_steps
    count = calculate_pi(n_steps, False)
    pi = 4 * float(count)/n_steps

    step_list.append(n_steps)
    pi_list.append(pi)


pi_line = [x - np.pi for x in pi_list]

# plt.plot(step_list, pi_list)
plt.plot(step_list, pi_line)
plt.savefig('pi_list')

print pi_line

