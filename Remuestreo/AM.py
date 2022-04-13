from scipy import signal 
import matplotlib.pyplot as plt 
import numpy as np
import scipy.fft as fft
  
t = np.linspace(0, 1e-3, 10000, endpoint=True) 
f = 15e3
y = 0.5*np.cos(2*np.pi*1.8*f*t) + np.cos(2*np.pi*2*f*t) + 0.5*np.cos(2*np.pi*2.2*f*t)

file = open("AM.txt", "w")
for i in range(len(t)):
    file.write(str(t[i]) + "\t" + str(y[i]) + "\n")
file.close()



# plt.plot(t, y)   
# plt.xlabel('Time') 
# plt.ylabel('Amplitude') 
# plt.title('Sawtooth Signal - Geeksforgeeks') 
# plt.grid(True)
  
# plt.show()