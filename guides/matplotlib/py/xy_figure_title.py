import matplotlib.pyplot as plt

# Data
x = range(1, 20)
y = [i**2 for i in x]


# First graph
plt.title('Nice Graph Title')
plt.xlabel('Energy [kcal/mol]')
plt.ylabel('Something else $\hat \lambda^2$')

plt.plot(x, y)
plt.savefig('figure_title.eps')


# Clear data
plt.clf()


# Second graph
plt.title('Another nice title')
plt.xlabel('X [$R^2$]')
plt.ylabel('Y [$\hat \epsilon$]')

# Place some text
plt.text(5, 200, r'$\mu=100,\ \sigma=15$')

plt.plot(x, y)
plt.savefig('figure_title_text.eps')


