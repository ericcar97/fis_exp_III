import lin_fit_mod
import pandas as pd
from numpy import *
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import plotly.express as px
from matplotlib import rc
from scipy.stats import t

file = 'short_conection.csv'
data = pd.read_csv(file)
data.index += 1
column = data.columns
x_data = data[column[0]].values
y_data = data[column[1]].values
y_error = data[column[2]].values
N = len(data)

a, b, sa, sb, r_squared, sigma = lin_fit_mod.w_lin_reg(x_data, y_data, N)
residuals = y_data - (a*x_data + b)

alpha = 0.05
t = t.ppf(1-alpha/2, df = N - 2)

#Results
print('number of points: ', N)
print('slope: ', a)
print('intercept: ', b)
print('standar desviation of the slope: ', sa * t)
print('standar desviation of the intercept: ', sb)

#plotting
x_min = x_data[0] - (x_data[1] - x_data[0])/2
x_max = x_data[N-1] + (x_data[N-1]- x_data[N-2])/2
x_fit = linspace(x_min,x_max,1000)
y_fit = a*x_fit + b

fig = plt.figure(1, figsize = (8,5))
gs = gridspec.GridSpec(2, 1, height_ratios = [6,2],
                       hspace = 0.15)
plt.rc('text', usetex = True)
plt.rc('font', family = 'serif')
def plotStyle():
    plt.grid(b = True, ls = '--',
             lw = 0.5, c = 'grey')
    plt.xlim(x_min,x_max)

ax1 = fig.add_subplot(gs[0])
ax1.set_ylabel('Corriente [A]')
ax1.scatter(x_data, y_data, c = 'r', s = 0.5)
ax1.errorbar(x_data, y_data , yerr = y_error,
            ls =  'none', elinewidth = 0.5,
            capsize = 1, capthick = 0.5, c = 'k')
ax1.plot(x_fit, y_fit, lw = 0.5, c = 'k')
#ax1.set_xticklabels([])
plotStyle()

ax2 = fig.add_subplot(gs[1])
ax2.set_xlabel('Voltaje [V]')
ax2.set_ylabel('Residuos')
ax2.scatter(x_data, residuals, c = 'r')
plotStyle()
plt.savefig('short_conection_VI.eps')
