import numpy as np
import matplotlib.pyplot as plt

def Euler(fcn, Tspan, I, Nt):
   
    dt = (Tspan[1] - Tspan[0])/float(Nt) 
    t = np.linspace(Tspan[0], Tspan[1], Nt+1)

    f_ = lambda u, t: np.asarray(fcn(u, t))
    if isinstance(I, (float, int)):
        u = np.zeros(Nt+1)  # u[n] is the numerical solution
    else:
        I = np.asarray(I)
        neq = I.size
        u = np.zeros((Nt+1, neq))

    u[0] = I
    for n in xrange(Nt):
        u[n+1] = u[n] + dt*f_( u[n], t[n] )
    return u, t

if __name__ == "__main__":
    def fcn(u, t):
        return np.array([u[1], -u[0]])
        #return np.stack((u[1], -u[0]))
        return [u[1], -u[0]]

    def exact(t):
        return np.cos(t)
   
    Tspan = [0.,2*np.pi]
    omega = 2
    P = 2*np.pi/omega
    h = P/100 # this guy is for the step
    T = 2*P
    Nt = int(round(T/h))# here we compute the number of the point we are going to consider
    I = np.stack((1.,0.))

    plt.figure(figsize=(6,3))
    u, x = Euler(fcn, Tspan, I, Nt+1)
    plt.plot(x, u[:,0],'o-', label = 'numerical solution')

    xx = np.linspace(0, 2*np.pi, Nt+1)
    ex = exact(xx)

    plt.plot(xx, ex,'r-', label='exact')
    plt.legend(loc='best')
    plt.title('Euler method, simple system of ODEs')
    plt.grid(True)
    plt.show()

