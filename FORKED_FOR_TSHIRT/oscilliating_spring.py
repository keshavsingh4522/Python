import numpy as np
import matplotlib.pyplot as plt
from math import e, cos, sqrt

#Create two 'empty' lists with 101 zeros each
n = 101
t_array = np.zeros(n)
y_array = np.zeros(n)

#Defining the y(t) function with the correct constants
def y(t):
    k = 4
    fric = 0.15
    m = 9
    A = -0.3
    
    return (A*e**(fric*t)*cos(sqrt(k*t/m)))

#Use linspace to create a list with 101 uniformly spaced values in the range [0, 25]    
t_array = np.linspace(0, 25, 101)

#Have to vectorize the y(t) function so that it can calculate the y values
y_vec = np.vectorize(y)
#Use the vectorized function to calculate y values for each t value
y_array = y_vec(t_array)

#Plots the position of the rock against time in the given time interval
plt.plot(t_array, y_array)
plt.xlabel("Time (s)")
plt.ylabel("Vertical position (m)")
plt.show()
