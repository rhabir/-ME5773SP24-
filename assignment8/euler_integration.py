import numpy as np
import math
import time

def int_funct(y, t):
    """
    Function to be integrated. 
    This represents the differential equation dy/dt = f(y, t).
    """
    # For this specific problem, f(y, t) = sin(t)
    f = np.sin(t)
    return f

def euler_integration(y0, t0, dt, tmax):
    """
    Implements the Euler method for solving ODEs.
    """
    nevals = int((tmax-t0)/dt)
    y = np.zeros(nevals+1)
    t = np.zeros(nevals+1)
    y[0] = y0
    t[0] = t0
    
    for i in range(nevals):
        t[i+1] = t[i] + dt
        y[i+1] = y[i] + dt * int_funct(y[i], t[i])
    
    return y, t

if __name__ == '__main__':
    y0 = -1
    t0 = 0.0
    dt = 0.000001
    tmax = 10
    
    t_start = time.time()
    y, t = euler_integration(y0, t0, dt, tmax)
    t_end = time.time()
    
    y_an = -np.cos(t[-1])
    
    print(f"Solution for time t={t[-1]:.4f}: y(t)={y[-1]:.8f} ")
    print(f"Analytical solution : y(t)={y_an:.8f} error: {abs(y_an-y[-1]):.4e} ")
    print(f'CPU time {t_end-t_start}')
