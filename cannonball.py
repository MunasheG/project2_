import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy.stats import norm
from sklearn.model_selection import train_test_split

def linear(x, m, b):
    return m * x + b

def quadratic(x, a, b, c):
    return a*x**2 + b*x + c

data = np.loadtxt("cannon.csv", delimiter=",", dtype=str)

v = data[1:, 0].astype(np.float32) #velocity in m/s
h = data[1:, 1].astype(np.float32) #height in meters
d = data[1:, 2].astype(np.float32) #distance in meters

print("v = ", v)
print("h = ", h)
print("d = ", d)

params, params_cov = scipy.optimize.curve_fit(linear, v, d)
slope = params[0]
intercept = params[1]
print('pumpkin fit: d = {:.3f} v + {:.3f}'.format(slope,intercept))

plt.figure()
plt.scatter(v, d, label='Data')
plt.plot(v, linear(v, slope, intercept),label='Linear Fit') 
plt.legend(loc='best')
plt.xlabel("velocity of cannonball (m/s)")
plt.ylabel("horizontal distance (meters)")  
plt.show()

###   Exercise 1

params, params_cov = scipy.optimize.curve_fit(quadratic, v, d)
a = params[0]
b = params[1]
c = params[2]

print("pumpkin fit: d = {:.3f} t^2 + {:.3f} t + {:.3f}".format(a, b, c))

plt.figure()
plt.scatter(v, d, label='Data')
plt.plot(v, quadratic(v, a, b, c), label='Quadratic Fit')
plt.xlabel("time (s)")
plt.ylabel("distance (d)")
plt.legend(loc='best')
plt.show()

###   Exercise 2

data2 = np.loadtxt("piano.csv", delimiter=",", dtype=str)

ve = data2[1:, 0].astype(np.float32) #velocity in m/s
he = data2[1:, 1].astype(np.float32) #height in meters
di = data2[1:, 2].astype(np.float32) #distance in meters

params, params_cov = scipy.optimize.curve_fit(linear, ve, di)
slope2 = params[0]
intercept2 = params[1]
print('piano fit: di = {:.3f} v + {:.3f}'.format(slope,intercept))

plt.figure()
plt.scatter(ve, di, label='Data')
plt.plot(ve, linear(ve, slope2, intercept2),label='Linear Fit') 
plt.legend(loc='best')
plt.xlabel("velocity of cannonball (m/s)")
plt.ylabel("horizontal distance (meters)")  
plt.show()

###   Quadratic fit

params, params_cov = scipy.optimize.curve_fit(quadratic, ve, di)
a2 = params[0]
b2 = params[1]
c2 = params[2]

print("piano fit: di = {:.3f} t^2 + {:.3f} t + {:.3f}".format(a2, b2, c2))

plt.figure()
plt.scatter(ve, di, label='Data')
plt.plot(ve, quadratic(ve, a, b, c), label='Quadratic Fit')
plt.xlabel("time (s)")
plt.ylabel("distance (d)")
plt.legend(loc='best')
plt.show()


