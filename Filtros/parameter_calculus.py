import numpy as np

#Script para calcular los parametros de la Sallen-Key

num = 3.68e10
a0 = 1
pi = np.pi
f = 40e3
w = 2*pi*f

# Stage 1
# den = S**2 + 2.48e5*S + 1.93e10
# Q1 = 0.561247923
a1_s1 = 2.48e5
a2_s1 = 1.93e10

# Stage 2
# den = S**2 + 1.75e5*S + 4.33e10
# Q2 = 1.145772932
a1_s2 = 1.75e5
a2_s2 = 4.33e10

# Stage 1
# den = S**2 + 6.45e4*S + 6.43e10
# Q3 = 3.930692039
a1_s3 = 6.45e4
a2_s3 = 6.43e10

# Transferencia completa 
# num = 5e31
# den = S**6 + 4.87e5*S**5 + 1.94e11*S**4 + 4.72e16*S**3 + 8.25e21*S**2 + 9.08e26*S + 5e31

c1 = 1e-9
c2 = 1e-9

# Parametros para Stage 1
R1R2 = 1/(c1*c2*a2_s1*w*w)
b = R1R2*c2*a1_s1*w
c = R1R2
print(b)
print(c)
print(w*w*a2_s1*c1*c1)
print(c2*w*a1_s1/(w*w*a2_s1*c1*c1))
