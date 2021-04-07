import pandas as pd
from numpy import *

file = 'hM.csv'
data = pd.read_csv(file)

print(data)
columns = data.columns
xB = data[columns[0]]
B = data[columns[1]]
dB = data[columns[2]]

for i in range(0,len(data)):
    print('$',xB[i],'$ & $',B[i],'\pm',dB[i],'$ \ ' )

    
