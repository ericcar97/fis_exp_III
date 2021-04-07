from numpy import *

R = 26.6
L = 0.68e-3
C = 1.01e-6
s_L = 0.01e-3
s_C = 0.01e-6
s_R = 0.8

v_0 = 1/(2*pi*sqrt(L*C))
sv_0 = sqrt(s_L**2/(16*pi**2*C*L**3) + s_C**2/(16*pi**2*C**3*L))

print('Frecuencia de resonancia en Hz: ',v_0)
print('Incertidumbre: ',sv_0)

Q = sqrt(L/C)/R
s_Q = sqrt((4*L*s_R**2/R**2 + s_L**2/L + L*s_C**2/C**2)/(C*R**2))/2

print('Factor de calidad: ', Q)
print('Incertidumbre: ',s_Q)



