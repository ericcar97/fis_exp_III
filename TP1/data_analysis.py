import pandas as pd 

file = 'data.csv'
data = pd.read_csv(file)
print(data)

I = data['I']*10**-3
dI = data['dI']*10**-3
Vcc = data['Vcc']
dVcc = data['dVcc']
Vcl = data['Vcl']
dVcl = data['dVcl']

#short_conection = pd.DataFrame(zip(I,V,dV),columns = ['I','Vcc','dVcc'])
short_conection = pd.DataFrame(zip(Vcc,I,dI),columns = ['Vcc','I','dI'])
short_conection.to_csv('short_conection.csv', index = False)
#long_conection = pd.DataFrame(zip(I,V,dV),columns = ['I','Vcl','dVcl'])
long_conection = pd.DataFrame(zip(Vcl,I,dI),columns = ['Vcl','I','dI'])
long_conection.to_csv('long_conection.csv', index = False)