import numpy as np
from scipy import signal 
import matplotlib.pyplot as plt

#El propósito del filtro antialiasing es eliminar toda presencia, antes de hacer el muestreo, de las frecuencias superiores a fs/2, siendo fs la frecuencia muestreo.
def FAA(data, fs):
    order=5
    fc = 40e3
    num, den = signal.butter(order, fc, fs=fs, btype='lowpass', analog=False)
    y = signal.lfilter(num, den, data)
    return y



"""
#---------------------------#
#       TEST BENCH          #
#---------------------------#

# https://stackoverflow.com/questions/25191620/creating-lowpass-filter-in-scipy-understanding-methods-and-units

# Filter requirements.
order = 6
fs = 30.0       # sample rate, Hz
cutoff = 3.667  # desired cutoff frequency of the filter, Hz

# Demonstrate the use of the filter.
# First make some data to be filtered.
T = 5.0         # seconds
n = int(T * fs) # total number of samples
t = np.linspace(0, T, n, endpoint=False)
# "Noisy" data.  We want to recover the 1.2 Hz signal from this.
data = np.sin(1.2*2*np.pi*t) + 1.5*np.cos(9*2*np.pi*t) + 0.5*np.sin(12.0*2*np.pi*t)

# Filter the data, and plot both the original and filtered signals.
y = FAA(data, cutoff, fs, order)

plt.plot(t, data, 'b-', label='data')
plt.plot(t, y, 'g-', linewidth=2, label='filtered data')
plt.xlabel('Time [sec]')
plt.grid()
plt.legend()

plt.subplots_adjust(hspace=0.35)
plt.show()
"""