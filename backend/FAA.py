import numpy as np
from scipy import signal 
import matplotlib.pyplot as plt

#El propósito del filtro antialiasing es eliminar toda presencia, antes de hacer el muestreo, de las frecuencias superiores a fs/2, siendo fs la frecuencia muestreo.
def FAA(data, fs):
    order=8
    fc = 40e3
    wc = 2*np.pi*fc
    ws = 2*np.pi*fs
    num, den = signal.butter(order, wc, fs=ws, btype='lowpass', analog=False)
    y = signal.lfilter(num, den, data)
    return y


# def filter_test():
#     num = [3.13e43]
#     den = [1, 1.4e6, 9.82e11, 4.47e17, 1.44e23, 3.34e28, 5.5e33, 5.86e38, 3.13e43]
#     sys = signal.TransferFunction(num, den)

"""
#---------------------------#
#       TEST BENCH          #
#---------------------------#

# https://stackoverflow.com/questions/25191620/creating-lowpass-filter-in-scipy-understanding-methods-and-units

# Filter requirements.
fs = 100e3       # sample rate, Hz
# Demonstrate the use of the filter.
# First make some data to be filtered.
T = 2e-3        # seconds
t = np.linspace(0, T, 1000)
f= 100e3
# "Noisy" data.  We want to recover the 1.2 Hz signal from this.
#data = np.sin(1.2*2*np.pi*t) + 1.5*np.cos(9*2*np.pi*t) + 0.5*np.sin(12.0*2*np.pi*t)
data2 = np.cos(2*np.pi*f*t)

# Filter the data, and plot both the original and filtered signals.
y = FAA(data2, fs)

plt.plot(t, data2, 'b-', label='data')
plt.plot(t, y, 'g-', linewidth=2, label='filtered data')
plt.xlabel('Time [sec]')
plt.grid()
plt.legend()

plt.subplots_adjust(hspace=0.35)
plt.show()
"""