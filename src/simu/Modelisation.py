import numpy as np



def modele_approx(x):
    facteur = 1 / 309.83
    return (-102.24 * np.sin((2 * np.pi * x) / 7) + 21.99 * np.cos((2 * np.pi * x) / 7) + 185.60) * facteur


#plot
import matplotlib.pyplot as plt
x = np.linspace(0, 7, 100)
y = modele_approx(x)
plt.plot(x, y)
plt.show()