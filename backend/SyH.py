

def SyH(signal, sq):
    output=[]
    aux=signal[0]
    for i in range(len(sq)):
       if sq[i]<0:
           # output = np.append(output, signal[i])
            output.append(signal[i])
            aux=signal[i]
       elif sq[i]>0:
           # output = np.append(output, 0)
           output.append(aux)
    return output