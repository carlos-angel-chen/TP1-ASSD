from operator import le
from tkinter import W
from turtle import color
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

t = np.linspace(0, 1e-3, 10000, endpoint=True) 
f = 40e3
pi = np.pi 

num1 = [59417706476.53]
den1 = [1, 436363.63636364, 59417706476.53]

num2 = [64474532559.639]
den2 = [1, 279432.62411348, 64474532559.639]

num3 = [64750064750.065]
den3 = [1, 108974.35897436, 64750064750.065]

num = [num1[0]*num2[0]*num3[0]]
den = [1, 824770.619451, 388579978404.7644, 2147483647, 2147483647, 2147483647, 2147483647]


sys1 = signal.TransferFunction(num1, den1)
sys2 = signal.TransferFunction(num2, den2)
sys3 = signal.TransferFunction(num3, den3)

sys = signal.TransferFunction(num, den)

w, mag1, phase1 = signal.bode(sys1)
w, mag2, phase2 = signal.bode(sys2)
w, mag3, phase3 = signal.bode(sys3)

w, mag, phase = signal.bode(sys)
plt.semilogx(w,mag)
# plt.semilogx(w,mag1)
# plt.semilogx(w,mag2)
# plt.semilogx(w,mag3)
plt.show()
