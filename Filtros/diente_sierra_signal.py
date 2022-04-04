from scipy import signal 
import matplotlib.pyplot as plot 
import numpy as np 
  
t = np.linspace(0, 1, 1000, endpoint=True) 
  
plot.plot(t, signal.sawtooth(2 * np.pi * 5 * t)) 
  
plot.xlabel('Time') 
plot.ylabel('Amplitude') 
plot.title('Sawtooth Signal - Geeksforgeeks') 
  
plot.axhline(y=0, color='k') 
  
plot.show() 