###Integration methods for COMP6216 Coursework 2###
#Brijee Rana
#br1e21
#33385874

from math import sin
from numpy import arange
import matplotlib.pyplot as plt
from pylab import plot, xlabel, ylabel, show

#DE parameters
a=0.5
L=0
H=1

def f(x,t):
    return a*(L-H)*x*(1-x)

#intial t
t0 = 0.0
#final t
tf = 20.0 
N = 20
#step size
h = (tf-t0)/N
tpoints = arange(t0,tf,h)
xpoints = []
xp2 = []
xp3 = []
xp4 = []

#intial condition
x = 0.5

for t in tpoints:
    xpoints.append(x)
    k1 = h*f(x,t)
    k2 = h*f(x+0.5*k1,t+0.5*h)
    k3 = h*f(x+0.5*k2,t+0.5*h)
    k4 = h*f(x+k3,t+h)
    x+= (k1+2*k2+2*k3+k4)/6

#plotting graph
plot(tpoints, xpoints)
xlabel("t")
ylabel("x(t)")
plt.title("Numerical integration using Runge-Kutta")
plt.savefig("Rungekutta4order.png")
show()

