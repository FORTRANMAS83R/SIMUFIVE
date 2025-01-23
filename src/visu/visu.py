import matplotlib.pyplot as plt
import numpy as np 

def freq_marge(c_f: float, r_max: float):
    marge = np.arange(0, 1, 0.05)
    plt.title("Fréquentation en fonction de la marge")
    plt.xlabel("Marge (%)")
    plt.ylabel("Fréquentation (%)")
    plt.plot( c_f / ((1 -marge) * r_max), marge * 100)
    plt.plot(- (c_f * marge) / (r_max )**2, marge * 100)
    plt.show()

freq_marge(10000, 19000)