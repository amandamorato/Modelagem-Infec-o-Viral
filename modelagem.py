# -*- coding: utf-8 -*-
from scipy.integrate import solve_ivp
import numpy as np
import pandas as pd

# Função que define o sistema de EDOs 
def odeSystem(t, u, b, k, a, p, k2, s, m):
    E, I, V, T = u[0], u[1], u[2], u[3]
    dE_dt = -b*E*V
    dI_dt = b*E*V - k*I*T - a*I
    dV_dt = p*a*I - k2*V
    dT_dt = s*I - m*T
    return [dE_dt, dI_dt, dV_dt, dT_dt]  

def solveOde(t, y):
    global model_args
    return odeSystem(t, y, *model_args)

def setInitialCondition():
    E = 5000
    I = 0
    V = 100
    T = 5
    u = [E, I, V, T]
    return u

def setParameters():
    b = 0.0002
    k = 0.2
    a = 0.5
    p = 50
    k2 = 0.4
    s = 0.2
    m = 0.005
    model_args = (b, k, a, p, k2, s, m)
    return model_args

def setTime():
    dt = 0.010000    
    tfinal = 100
    nsteps = int(tfinal/dt)
    print('nsteps ' + str(nsteps))
    t=np.linspace(0,tfinal,nsteps)    
    return (tfinal,t)

if __name__ == "__main__":
    global model_args
    (tfinal,t) = setTime()
    P = setInitialCondition()
    model_args = setParameters()     
    results = solve_ivp(solveOde,(0, tfinal), P, t_eval=t, method='Radau')
    dir_ = ''
    df = pd.DataFrame(results.y.transpose(), columns = ['E', 'I', 'V', 'T'])
    df.insert(0, 'Time', results.t)
    df.to_csv(dir_+'oderesults.csv', float_format='%.5f', sep=',')