import numpy as np
import matplotlib.pyplot as plt
import math
from numpy import array

#parameters
a=0.5
L=0
H=1

def function(t):
    #add exponential
    p = -a*(L-H)*t
    x = 1 / (1 + math.exp(p))
    return x 

#x values
x = []
l = []
#adjust time t
time = [i for i in range(20)]

for t in time:
    x.append(function(t))
    l.append(1-function(t))

#print(time)
#print(x)   
print(function(8)) 

plt.figure()
plt.grid()
plt.plot(time, x, label='Hard Students')
plt.plot(time, l, label='Lazy Students')
plt.title("Composition of the group over time")
plt.xlabel('t')
plt.ylabel('x(t)')
plt.legend()
plt.show()