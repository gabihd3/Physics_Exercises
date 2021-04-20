# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 18:11:00 2021

@author: sandr
"""



import numpy as np
import matplotlib.pyplot as plt

#Create a function that gives you J(m, x)

def J(m, x):
    def f(m, x, theta): #Function inside integral
        return np.cos(m * theta - x * np.sin(theta))

    N = 100
    a = 0
    b = np.pi
    h = (b - a) / N
    s = (f(m, x, a) + f(m, x, b))
    
    for k in range(1,N,2): #Odd numbers
        s = s + 4* f(m, x, a+k*h)
    for k in range(2,N,2): #Even numbers
        s = s + 2* f(m, x, a+k*h)

    return 1 / np.pi * h/3 * s 

#Plot J0, J1, J2
xpoints = np.linspace(0, 20, 100) #From x=0 to x=20 
J0 = [] 
J1 = []
J2 = []
for x in xpoints:
    J0.append(J(0, x))
    J1.append(J(1, x))
    J2.append(J(2, x))

plt.plot(xpoints, J0, "g")
plt.plot(xpoints, J1, "b")
plt.plot(xpoints, J2, "r")
plt.legend(("$J_0$", "$J_1$", "$J_2$"))
plt.show()



#Part b
def r(x, y): #Get radius from coordinates
    return np.sqrt(x**2 + y**2)


def I(r): #Intensity function
    if r == 0:
        return 0.25

    Lambda = 0.5 #micrometers
    kr = 2 * np.pi / Lambda * r
    return (J(1, kr)/ kr)**2

#Create grid
side = 2  #micrometers 

space = side / 200 #200 grid points each direction

# Calculate the position of the center
xcentre = side / 2
ycentre = side / 2

# Make an empty array to store values
Intensities = np.empty([200, 200], float) #200 grid points each direction

# Calculate the values in the array
for i in range(0,200):
    y = i * space
    for j in range(0,200):
        x = j * space
        distance = r(x - xcentre, y - ycentre)
        Intensities[i, j] = I(distance)

plt.imshow(Intensities, origin="lower", extent=[0, side, 0, side], vmax=0.01)
plt.hot()
plt.show()
