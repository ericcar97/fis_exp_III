import pandas as pd 
import plotly.express as px
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from scipy.optimize import curve_fit
from matplotlib import rc
from numpy import *
from scipy.stats import t

#constant
mu_0 =  1.25663706212e-6
corriente = 1.
radio2 = 0.0589
radio1 = 0.0598
vueltas1 = 468
vueltas2 = 458

###Importing the data
file = 'h.csv'
data = pd.read_csv(file)
column = data.columns
x_data = data[column[0]].values
y_data = data[column[1]].values
y_error = data[column[2]].values
N = len(data)
print(data)

###Defying the model
def B_model(x, x0, dist):
    resultado = vueltas1*radio1**2/(radio1**2 + (x - x0 + dist/2)**2)**(3/2) 
    resultado+= vueltas2*radio2**2/(radio2**2 + (x - x0 - dist/2)**2)**(3/2)
    resultado*= mu_0*corriente/2
    return resultado

###Model fitting
x0, dist = 0.01, 5.9
init_values = [ x0, dist ]
fit, covariance = curve_fit(B_model,x_data,y_data,
                            p0 = init_values,
                            absolute_sigma = True,
                            sigma = y_error)
nu = N - 2 #### degrees of freedom = number of data points - number of parameters fitted
std_dev = sqrt(diag(covariance))
residuals = y_data - B_model(x_data,fit[0], fit[1])
std_error = sqrt(diag(covariance)*sum(residuals**2)/nu)

#Confidence interval IC
alpha = 0.05 #95%
t = t.ppf(1-alpha/2, df = nu)

#Results

print('results: ', fit)
print('standar deviations: ', std_dev)
print('standar error: ', std_error)
print('adjusted standard error with t distribution: ', std_error*t)
print('Confidence interval: ', fit - std_error*t, 'to', fit + std_error*t)


#Plotting
xmin = x_data[0] - (x_data[1] - x_data[0])/2
xmax = x_data[N-1]+(x_data[N-1] - x_data[N-2])*2
xfit = linspace(xmin,xmax,1000)
yfit = B_model(xfit,fit[0],fit[1])
fig = plt.figure(1, figsize = (8,5))
gs = gridspec.GridSpec(2, 1, height_ratios = [6,2],
                       hspace= 0.15)
plt.rc('text', usetex=True)
plt.rc('font', family='serif', size = 12)
def plotStyle():
    plt.grid(b = True, which = 'major', ls = '--',
            lw = 0.5, c = 'k')
    plt.grid(b = True, which = 'minor', ls = '--',
            lw = 0.25, c = 'grey')
    plt.xlim(xmin,xmax)
 
#Subplot: fitted function
ax1 = fig.add_subplot(gs[0])
ax1.set_ylabel('Campo Magnetico [T]')
ax1.scatter(x_data,y_data,c = 'r',s = 10)
ax1.errorbar(x_data,y_data, ls = 'none',
             c = 'k',
             yerr = y_error,
             elinewidth= 0.5,
             capsize = 1,
             capthick = 0.5)
ax1.plot(xfit,yfit,lw = 0.5,
             c = 'k')
#ax1.set_xticklabels([])
plotStyle()

#Subplot: Residuals
ax2 = fig.add_subplot(gs[1])
ax2.scatter(x_data,residuals,c = 'r')
ax2.set_xlabel('Distancia [m]')
ax2.set_ylabel('Residuos')
plotStyle()
plt.savefig('h.eps')