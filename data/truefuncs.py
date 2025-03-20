import numpy as np

def sin1_2_simple(x0, theta0=0.4, theta1=-3.14):
    return theta0*np.sin(theta1/5*x0)

def sin1_2(x0, theta0=0.4, theta1=-3.14):
    return np.sin(theta0*x0 + theta1)