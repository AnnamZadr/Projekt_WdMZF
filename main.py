import math
import numpy
from matplotlib import pyplot as plt

Hlist = []
Tlist = []
V = float(input())
g = 9.80
Hmax = pow(V, 2)/(2*g)

Tmax = math.sqrt((pow(V, 2)/pow(g, 2))+ (2*Hmax/g)) + (V/g)

print(Hmax, Tmax)

for t in numpy.arange(0, Tmax, 0.01):
    h = V*t-((g*pow(t, 2))/2)
    if h < 0:
        break
    Hlist.append(h)
    Tlist.append(t)

plt.plot(Tlist, Hlist)
plt.show()
