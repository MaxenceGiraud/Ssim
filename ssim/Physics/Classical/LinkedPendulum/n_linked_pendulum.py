import sympy as smp
from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt
from copy import deepcopy
from matplotlib import animation
from matplotlib.animation import PillowWriter
from functools import partial
import os

def linked_pend_analytical(n_pendulum):
    m = [smp.symbols(r'm_{}'.format(i)) for i in range(n_pendulum)] # mass
    l = [smp.symbols(r'L_{}'.format(i)) for i in range(n_pendulum)] # lenght of roap
    t, g = smp.symbols('t g')

    # Angles between springs and associated first and second derivative
    thetas = [smp.symbols(r'\theta_{}'.format(i), cls=smp.Function)(t) for i in range(n_pendulum)]
    thetas_d = [smp.diff(thetas[i],t) for i in range(n_pendulum)]
    thetas_dd = [smp.diff(thetas_d[i],t) for i in range(n_pendulum)]

    # Position of balls
    x = [smp.symbols(r'x_{}'.format(i), cls=smp.Function) for i in range(n_pendulum)]
    y = [smp.symbols(r'y_{}'.format(i), cls=smp.Function) for i in range(n_pendulum)]


    T = 0 # Kinetic energy
    V = 0 # Potential energy

    for i in range(n_pendulum):
        # params = [thetas[j] for j in range(i+1)]
        # params.extend([r[j] for j in range(i+1)])
        # x[i] = x[i](*params)
        # y[i] = y[i](*params)

        if i ==0 :
            x[0] = l[i]*smp.cos(thetas[0])
            y[0] = -l[i]*smp.sin(thetas[0])

        else :
            x[i] = x[i-1] + l[i]*smp.cos(thetas[i])
            y[i] = y[i-1] - l[i]*smp.sin(thetas[i])
        
        T = T + m[i] * (smp.diff(x[i], t)**2 + smp.diff(y[i], t)**2) 
        V = V + m[i] * g * y[i] 

    T = 1/2*T
    L = T-V # Lagrangian

    print(" Calculating Lagrange Equations")
    ## Lagrange equations
    LE = [smp.diff(L,thetas[i]) - smp.diff(smp.diff(L,thetas_d[i]),t) for i in range(n_pendulum)]
    LE = [LE[i].simplify() for i in range(len(LE))] 


    print(" Solving systems of Lagrange equations")
    # Solve the System of equations
    params = deepcopy(thetas_dd)
    sols = smp.solve(LE, (*params),simplify=False, rational=False)

    all_params = deepcopy(m)
    all_params.extend(l)
    all_params.extend([g])
    all_params.extend(thetas)
    all_params.extend(thetas_d)

    # Create functions to use with our numerical methods
    dwdt_f = [smp.lambdify(all_params,sols[thetas_dd[i]]) for i in range(n_pendulum)]
    dthetasdt_f = [smp.lambdify(thetas_d[i], thetas_d[i]) for i in range(n_pendulum)]

    
    # Define our system of ODEs
    def dSdt(m,l,g,S, t):
        S_np = np.reshape(S,(int(len(S)/n_pendulum),n_pendulum))
        thetas, w  = S_np
        return [
            *[dthetasdt_f[i](w[i]) for i in range(n_pendulum)],
            *[dwdt_f[i](*m,*l,g,*thetas,*w)for i in range(n_pendulum)],
        ]

    return dSdt



def n_linked_pendulum(n_pendulum=2,filename="npend.gif",mass=1,lenght=2,theta_init =None):
    ''' Solve the N Linked pendulum problem

    Params
    ------
    n_pendulum : int,
        Number of Pendulums. Defaults to 2
    filename : string, 
        File to write the animation.
    mass : {int,list}
        Mass of the balls, if int all the balls have the specified mass
    length : {int,list}
        length of the roaps/links, if int all the balls have the specified mass
    {}_init : list,
        Initial condition of each param. Thetas are the angles between the spring.

    Yields
    ------
    Create an animation and play it.
    ''' 
    
    t = np.linspace(0, 20, 1000)
    g = 9.81

    if isinstance(mass,int) or isinstance(mass,float):
        m = [mass for _ in range(n_pendulum)]
    else :
        m = mass
    if isinstance(lenght,int) or isinstance(lenght,float):
        l = [lenght for _ in range(n_pendulum)]
    else :
        l = lenght

    ode_sys = partial(linked_pend_analytical(n_pendulum=n_pendulum),m,l,g)

    if theta_init is None : 
        theta_init = [-np.pi/(4*i) for i in range(1,n_pendulum)]
    w_init = [0 for i in range(n_pendulum)]

    print("Solve resulting differential equations")
    ans = odeint(ode_sys, y0=[*theta_init,*w_init], t=t)

    # Compute x,y coordonates
    def get_xy(thetas):

        x = [l[0]*np.cos(thetas[0])]
        y = [-l[0]*np.sin(thetas[0])]

        for i in range(1,n_pendulum):
            x.append(x[i-1] + l[i]*np.cos(thetas[i]))
            y.append(y[i-1] - l[i]*np.sin(thetas[i]))

        return x,y

    x,y = get_xy(ans.T[:n_pendulum])  

    print("Creating Animation")
    def animate(i):
        ln1.set_data([[0,*[x[j][i] for j in range(n_pendulum)]], [0,*[y[j][i] for j in range(n_pendulum)]]])

    plt.style.use('dark_background')
    fig, ax = plt.subplots(1,1, figsize=(8,8))
    ax.grid()
    ax.axis('off')
    ln1, = plt.plot([],[], 'ro--', lw=2.5, markersize=10)
    ax.set_ylim(-15, 10)
    ax.set_xlim(-10,10)
    ani = animation.FuncAnimation(fig, animate, frames=1000, interval=50)
    ani.save("n_pendulum.gif",writer='pillow',fps=50)

    print("\n Done !")  

if __name__ == "__main__":
    filename = "n_pendulum.gif"
    n_linked_pendulum(filename =filename)

    import sys,subprocess

    def open_file(filename):
        if sys.platform == "win32":
            os.startfile(filename)
        else:
            opener = "open" if sys.platform == "darwin" else "xdg-open"
            subprocess.call([opener, filename])
        
    open_file(filename)