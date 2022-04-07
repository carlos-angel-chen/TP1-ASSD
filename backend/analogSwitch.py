import numpy as np

def analogSwitch(signal, sq):
    output=[]
    for i in range(len(sq)):
       if sq[i]>0:
           # output = np.append(output, signal[i])
            output.append(signal[i])
       elif sq[i]<0:
           # output = np.append(output, 0)
           output.append(0)
    return output