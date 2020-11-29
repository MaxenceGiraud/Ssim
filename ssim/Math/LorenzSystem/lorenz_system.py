import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint,solve_ivp
from mpl_toolkits.mplot3d import Axes3D


def lorenz_system_deriv(coord,rho = 28,sigma = 10,beta = 8/3):
    x,y,z = coord
    return sigma * (y - x), x * (rho - z) - y, x * y - beta * z 

def lorenz_system_integ(t,coord,rho = 28,sigma = 10,beta = 8/3):
    return lorenz_system_deriv(coord,rho,sigma,beta )

def plot_lorenz_system(rho= 28,sigma= 10,beta= 8/3):
    init =  [1,1,1]
    sol = solve_ivp(lorenz_system_integ,[0,40],init,max_step=0.01,args=(rho,sigma,beta))

    fig = plt.figure()
    ax = fig.gca(projection="3d")
    ax.plot(sol.y[0], sol.y[1], sol.y[2])
    plt.draw()
    plt.show()

def main():

   plot_lorenz_system()

if __name__ == '__main__':
    main()