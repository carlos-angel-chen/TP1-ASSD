from scipy import signal 
import matplotlib.pyplot as plt 
import numpy as np
import scipy.fft as fft

with open('AM_SyH_input_output_data.txt', 'r') as file_AM_SyH:
    data_SyH = file_AM_SyH.read()
    time_SyH = data_SyH[1][0]
print(time_SyH)

def FFT(signal, dt):
    signal_fft = fft.fft(signal)
    signal_frecs = fft.fftfreq(len(signal_fft), dt)[:len(signal_fft) // 2]
    signal_spectrum = 2.0 / len(signal_fft) * np.abs(signal_fft[0:len(signal_fft) // 2])

    return signal_frecs, signal_spectrum