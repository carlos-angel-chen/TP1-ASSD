#Script para calcular los parametros de la Sallen-Key

num = 3.68e10
a0 = 1

# Stage 1
# den = S**2 + 2.48e5*S + 1.93e10
a1_s1 = 2.48e5
a2_s1 = 1.93e10

# Stage 2
# den = S**2 + 1.75e5*S + 4.33e10
a1_s2 = 1.75e5
a2_s2 = 4.33e10

# Stage 1
# den = S**2 + 6.45e4*S + 6.43e10
a1_s3 = 6.45e4
a2_s3 = 6.43e10