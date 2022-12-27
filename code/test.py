import matplotlib.pyplot as plt
from helper import *

CT_ratio = [100/5]*12
Isc = [ 0.12, 0.2, 0.3, 0.4, 0.5, 0.5,0.5,0.5,0.5,0.5,0.5,0.5]
Ip = [1, 1.2, 1.4, 2.6,10.8,11,11,11,11,11,11,11]

to_plot = []

for x in range(len(CT_ratio)):
    trip = tripping_time(Isc[x], CT_ratio[x], Ip[x])
    print(trip)
    to_plot.append(trip)

print(to_plot)


plt.plot(Ip, to_plot)
plt.show()