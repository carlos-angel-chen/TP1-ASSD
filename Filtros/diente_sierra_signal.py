from scipy import signal 
import matplotlib.pyplot as plt 
import numpy as np 
  
t = np.linspace(0, 1e-3, 10000, endpoint=True) 
f = 7.5e3
y = signal.sawtooth(2 * np.pi * f * t)

file = open("diente_sierra.txt", "w")
for i in range(len(t)):
    file.write(str(t[i]) + "\t" + str(y[i]) + "\n")
file.close()

# plt.plot(t, y)   
# plt.xlabel('Time') 
# plt.ylabel('Amplitude') 
# plt.title('Sawtooth Signal - Geeksforgeeks') 
# plt.grid(True)
# plt.axhline(y=0, color='k') 
  
# plt.show()