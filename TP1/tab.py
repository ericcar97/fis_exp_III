import pandas as pd
from numpy import *

file = 'data.csv'
data = pd.read_csv(file)

print(data)
I = data['I']
dI = data['dI']
Vcc = data['Vcc']
dVcc = data['dVcc']
Vcl = data['Vcl']
dVcl = data['dVcl']
for i in range(0,len(data)):
    print('$',I[i],'\pm',dI[i],'$ & $', Vcc [i],'\pm',dVcc[i],'$ & $',Vcl [i],'\pm',dVcl[i], '$ \ ' )

    
