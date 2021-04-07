from numpy import *

R_m = 110.6
R_V = 10e6
sR_m = 0.0003
sR_V = 0.1
sR_A = 0.1
R_A = 0.4
R = R_m/(1 - R_m/R_V)
sR = sqrt(sR_m**2 + (R_m/R_V)**4*sR_V**2)/(1-R_m/R_V)**2
#R = R_m - R_A
#sR = sqrt(sR_m**2 + sR_A**2)
print(R)
print(sR)