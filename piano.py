import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy.stats import norm
from sklearn.model_selection import train_test_split

def linear(x, m, b):
    return m * x + b

def quadratic(x, a, b, c):
    return a*x**2 + b*x + c

data2 = np.loadtxt("piano.csv", delimiter=",", dtype=str)

v = data2[1:, 0].astype(np.float32) #velocity in m/s
h = data2[1:, 1].astype(np.float32) #height in meters
d = data2[1:, 2].astype(np.float32) #distance in meters

params, params_cov = scipy.optimize.curve_fit(linear, v, d)
slope = params[0]
intercept = params[1]
print('piano fit: di = {:.3f} v + {:.3f}'.format(slope,intercept))

plt.figure()
plt.scatter(v, d, label='Data')
plt.plot(v, linear(v, slope, intercept),label='Linear Fit') 
plt.legend(loc='best')
plt.xlabel("velocity of piano (m/s)")
plt.ylabel("distance (m)")  
plt.show()

###   Quadratic fit

params, params_cov = scipy.optimize.curve_fit(quadratic, v, d)
a = params[0]
b = params[1]
c = params[2]

print("piano fit: di = {:.3f} t^2 + {:.3f} t + {:.3f}".format(a, b, c))

plt.figure()
plt.scatter(v, d, label='Data')
plt.plot(ve, quadratic(ve, a, b, c), label='Quadratic Fit')
plt.xlabel("velocity of piano (m/s)")
plt.ylabel("distance (m)")
plt.legend(loc='best')
plt.show()

###    Analysis:
### Both linear and quadratic fits for the piano are extremely similar to that of the cannonball, whose fit is almost perfect to the line of best fit

