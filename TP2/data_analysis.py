import pandas as pd
from numpy import *

file = 'data.csv'
data = pd.read_csv(file)

f = data['f']
sf = data['sf']

V_f = data['V_f']
V_R = data['V_R']
sV_f = data['sV_f']
sV_R = data['sV_R']

G = V_R/V_f
sG = sqrt((V_R * sV_f / V_f**2)**2 + (sV_R / V_f)**2)

t1 = data['t1']
t2 = data['t2']
st1 = data['st1']
st2 = data['st2']

Dt = t1 - t2
sDt = sqrt(st1**2 + st2**2)

phi = 2*180*f*Dt
sphi = 2*180*sqrt((Dt*sf)**2 + (sDt*f)**2)

transf_fun = pd.DataFrame(zip(f,G,sG),columns = ['f','G','sG'])
transf_fun.to_csv('transf_fun.csv', index = False)


phase = pd.DataFrame(zip(f,phi,sphi),columns = ['f' , 'phi', 'sphi'])
phase.to_csv('phase.csv', index = False)

print(phase)
print(transf_fun)