import pandas as pd
from numpy import *

file = 'data.csv'
data = pd.read_csv(file)

xB1 = (data['xB1'].dropna() - 31.8) * 10**-2 #centering and change units
B1 = (data['B1'].dropna() - 4) * 10**-4    #deleting residuals and change units
dB1 = B1*0+3* 10**-4                         #error of hall's probe

xB2 = (data['xB2'].dropna() -31.8 )* 10**-2 
B2 = (data['B2'].dropna()- 4) * 10**-4
dB2 = B2*0+3* 10**-4

xHm = (data['xHm'].dropna() -34.5) * 10**-2
Hm = (data['Hm'].dropna() - 4)* 10**-4
dHm = Hm*0+3* 10**-4

xH = (data['xH'].dropna() -35) * 10**-2
H = (data['H'].dropna() - 4)* 10**-4
dH = H*0+3* 10**-4

xHM = (data['xHM'].dropna() -35.5)* 10**-2
HM = (data['HM'].dropna() - 4)* 10**-4
dHM = HM*0+3* 10**-4

b1 = pd.DataFrame(zip(xB1, B1, dB1), columns = ['xB1', 'B1', 'dB1'])
b1.to_csv('b1.csv', index = False)

b2 = pd.DataFrame(zip(xB2, B2, dB2), columns = ['xB2', 'B2', 'dB2'])
b2.to_csv('b2.csv', index = False)

hm = pd.DataFrame(zip(xHm, Hm, dHm), columns = ['xHm', 'Hm', 'dHm'])
hm.to_csv('hm.csv', index = False)

h = pd.DataFrame(zip(xH, H, dH), columns = ['xH', 'H', 'dH'])
h.to_csv('h.csv', index = False)

hM = pd.DataFrame(zip(xHM, HM, dHM), columns = ['xHM', 'HM', 'dHM'])
hM.to_csv('hM.csv', index = False)