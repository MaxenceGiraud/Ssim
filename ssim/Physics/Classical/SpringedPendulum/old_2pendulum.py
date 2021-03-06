import sympy as smp
from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from matplotlib.animation import PillowWriter

def two_pendulum(masses=[1,1]):
    print("Solving Analytical Problem")
    t, m1,m2, g, k = smp.symbols(r't m_1 m_2 g k')

    the1, the2, r1, r2 = smp.symbols(r'\theta_1, \theta_2, r_1, r_2', cls=smp.Function)

    # theta1
    the1 = the1(t)
    the1_d = smp.diff(the1, t)
    the1_dd = smp.diff(the1_d, t)

    the2 = the2(t)
    the2_d = smp.diff(the2, t)
    the2_dd = smp.diff(smp.diff(the2, t), t)

    r1 = r1(t)
    r1_d = smp.diff(r1, t)
    r1_dd = smp.diff(smp.diff(r1, t), t)

    r2 = r2(t)
    r2_d = smp.diff(r2, t)
    r2_dd = smp.diff(smp.diff(r2, t), t)

    x1, y1, x2, y2 = smp.symbols('x_1, y_1, x_2, y_2', cls=smp.Function)
    x1= x1(the1, r1)
    y1= y1(the1, r1)
    x2= x2(the1, r1, the2, r2)
    y2= y2(the1, r1, the2, r2)


    x1 = (1+r1)*smp.cos(the1)
    y1 = -(1+r1)*smp.sin(the1)
    x2 = (1+r1)*smp.cos(the1) + (1+r2)*smp.cos(the2)
    y2 = -(1+r1)*smp.sin(the1)-(1+r2)*smp.sin(the2) 

    print("Computing Lagrangian")
    ## Lagrangian
    T = 1/2 * m1 * (smp.diff(x1, t)**2 + smp.diff(y1, t)**2)+ 1/2 * m2 * (smp.diff(x2, t)**2 + + smp.diff(y2, t)**2)
    V = m1*g*y1 + m2*g*y2 + 1/2 * k * r1**2 + 1/2 * k * r2**2
    L = T-V

    print("Computing Lagrange Equations")
    ## Lagrange equations 
    LE1 = smp.diff(L, the1) - smp.diff(smp.diff(L, the1_d), t)
    LE1 = LE1.simplify()

    LE2 = smp.diff(L, the2) - smp.diff(smp.diff(L, the2_d), t)
    LE2 = LE2.simplify()

    LE3 = smp.diff(L, r1) - smp.diff(smp.diff(L, r1_d), t)
    LE3 = LE3.simplify()

    LE4 = smp.diff(L, r2) - smp.diff(smp.diff(L, r2_d), t)
    LE4 = LE4.simplify()


    sols = smp.solve([LE1, LE2, LE3, LE4], (the1_dd, the2_dd, r1_dd, r2_dd),
            simplify=False, rational=False)

    
    print("Solving the systems of DE")


    dw1dt_f = smp.lambdify((m1,m2, k ,g, the1, the2, r1, r2, the1_d, the2_d, r1_d, r2_d), sols[the1_dd])
    dthe1dt_f = smp.lambdify(the1_d, the1_d)

    dw2dt_f = smp.lambdify((m1,m2, k ,g, the1, the2, r1, r2, the1_d, the2_d, r1_d, r2_d), sols[the2_dd])
    dthe2dt_f = smp.lambdify(the2_d, the2_d)

    dv1dt_f = smp.lambdify((m1,m2, k ,g, the1, the2, r1, r2, the1_d, the2_d, r1_d, r2_d), sols[r1_dd])
    dr1dt_f = smp.lambdify(r1_d, r1_d)

    dv2dt_f = smp.lambdify((m1,m2, k ,g, the1, the2, r1, r2, the1_d, the2_d, r1_d, r2_d), sols[r2_dd])
    dr2dt_f = smp.lambdify(r2_d, r2_d)


    def dSdt(S, t):
        the1, w1, the2, w2, r1, v1, r2, v2 = S
        return [
            dthe1dt_f(w1),
            dw1dt_f(m1,m2,k,g,the1,the2,r1,r2,w1,w2,v1,v2),
            dthe2dt_f(w2),
            dw2dt_f(m1,m2,k,g,the1,the2,r1,r2,w1,w2,v1,v2),
            dr1dt_f(v1),
            dv1dt_f(m1,m2,k,g,the1,the2,r1,r2,w1,w2,v1,v2),
            dr2dt_f(v2),
            dv2dt_f(m1,m2,k,g,the1,the2,r1,r2,w1,w2,v1,v2),
        ]

    t = np.linspace(0, 20, 1000)
    g = 9.81
    m1 = masses[0]
    m2 = masses[1]
    k=10
    ans = odeint(dSdt, y0=[np.pi/2,0,(3/2)*np.pi/2,0,0,5,0,5], t=t)

    def get_x1y1x2y2(the1, the2, r1, r2):
        return ((1+r1)*np.cos(the1),
            -(1+r1)*np.sin(the1),
            (1+r1)*np.cos(the1) + (1+r2)*np.cos(the2),
            -(1+r1)*np.sin(the1)-(1+r2)*np.sin(the2)
    )


    x1, y1, x2, y2 = get_x1y1x2y2(ans.T[0], ans.T[2], ans.T[4], ans.T[6])


    ## Create animation
    print("\nCreating animation")
    def animate(i):
        ln1.set_data([0, x1[i], x2[i]], [0, y1[i], y2[i]])
    
    fig, ax = plt.subplots(1,1, figsize=(3,3))
    ax.grid()
    ln1, = plt.plot([], [], 'ro--', lw=3, markersize=8)
    ax.set_ylim(-15, 10)
    ax.set_xlim(-10,10)
    ani = animation.FuncAnimation(fig, animate, frames=1000, interval=50)
    ani.save('2pendulum.gif',writer='pillow',fps=50)

    print("Done !")

def main():
    two_pendulum()
    filename = './2pendulum.gif'
    import os, sys, subprocess

    def open_file(filename):
        if sys.platform == "win32":
            os.startfile(filename)
        else:
            opener = "open" if sys.platform == "darwin" else "xdg-open"
            subprocess.call([opener, filename])
        
    open_file(filename)

if __name__ == "__main__":
    main()