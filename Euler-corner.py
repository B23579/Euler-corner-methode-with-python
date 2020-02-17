

from numpy import zeros, linspace, pi, cos, array
import matplotlib.pyplot as plt
"""" This method is for Euler-corner methode"""

omega = 2
P = 2*pi/omega
h = P/100 # this guy is for the step
T = 2*P
N_t = int(round(T/h))# here we compute the number of the point we are going to consider
t = linspace(0, N_t*h, N_t+1) # to cree a liste of value between 0 and 2*pi 

u = zeros(N_t+1)
v = zeros(N_t+1)

# Initial condition
X_0 = 1
u[0] = X_0
v[0] = 0

# Step equations forward in time
for n in range(N_t):
    v[n+1] = v[n] - h*u[n]
    u[n+1] = u[n] +h*v[n+1]

fig = plt.figure()
l1, l2 = plt.plot(t, u, 'o-', t, X_0*cos(t), 'r')
fig.legend((l1, l2), ('numerical', 'exact'), 'upper left')
plt.xlabel('t')
plt.grid(True)
plt.savefig('tmp.pdf'); plt.savefig('tmp.png')
plt.show()


# In[45]:

import numpy as np
Tspan = [0.,2*np.pi]
I = np.stack((1.,0.))
I


# In[55]:

xx = np.linspace(0, 2*np.pi, 101)
t


# In[56]:

xx


# In[ ]:



