import numpy as np
from scipy.special import eval_genlaguerre,lpmv
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

##### CONSTANTS 
h_bar = 6.62607015e-34 / (2*np.pi) # reduced plank constant (J.s)
me = 9.1093837015e-31 # electron's mass (kg)
eps0 = 8.85418782e-12 # Vacuum permittivity (F.m-1)
e = 1.602176634e-19 # Electron charge (C)

a= 0.529e-10 # Bohr radius

def energy_hydrogen(n):
    ''' Compute energy of the hydrogen atom ( in J) '''
    return - (me/(2*h_bar**2) *  (e**2/(4*np.pi*eps0))**2) * 1/n**2

def compute_radial_hydrogen(n,l,r,a= 0.529e-10):
    ''' Compute the radial part of the hydrogen atom wave function 
    Parameters
    -----------
    n : int,
        Principal quantum number, strictly greater than 0
    l : int,
        Azimuthal quantum number, range between 0 and n-1
    m : int,
        Magnetic quantum number, range between -l and l
    r : Distance from center
    Yields
    ------
    '''
    laguerre = eval_genlaguerre(n-l-1,2*l+1,(2*r/(n*a)))
    sqrt_term = (2/(n*a)) **3 * np.math.factorial(n-l-1)/(2*n*np.math.factorial(n+l))
    exp_term = -r/(n*a)
    third_term = (2*r/(n*a))**l
    
    return np.sqrt(sqrt_term) * np.exp(exp_term) * third_term * laguerre

def compute_spherical_harmonics_hydrogen(l,m,theta,phi):
    '''
    Parameters
    -----------
    l : int,
        Azimuthal quantum number,
    m : int,
        Magnetic quantum number, range between -l and l
    theta :
    phi : 
    '''
    first_term = np.sqrt( ((2*l+1) * np.math.factorial(l-m)) / (4*np.pi *np.math.factorial(l+m) ) ) * np.exp(1j * m * phi) 
    legendre = lpmv(m,l,np.cos(theta))

    return first_term * legendre

def hydrogen_wave_function(x,n,l,m,a= 0.529e-10):
    '''
    Parameters
    -----------
    x : 
    n : int,
        Principal quantum number, strictly greater than 0
    l : int,
        Azimuthal quantum number, range between 0 and n-1
    m : int,
        Magnetic quantum number, range between -l and l
    a : float,
        Radius of the atom
    Yields
    ------
    out : 
    '''

    assert (len(x.shape) <3), "X dimension must be at most 2" 

    ## Compute spherical / polar coordonates
    theta = 0
    phi = 0
    if len(x.shape) == 1 or x.shape[1] == 1:
        r = x
    else : 
        assert x.shape[1] <4, "2nd dim of x must be at most 3"
        r = np.sum(x**2,axis=1)
        theta  = np.arctan2(x[:,1],x[:,0])
        if x.shape[1] == 3 : 
            phi = np.arctan(np.sum(x[:,:2]**2,axis=1)/x[:,2]) 

    hwf =  compute_radial_hydrogen(n,l,r,a) * compute_spherical_harmonics_hydrogen(l,m,theta,phi)

    return hwf


def main():

    # 2D 
    # Creating grid points 
    x= np.linspace(-10,10,100)
    y = np.linspace(-10,10,100)
    xx,yy = np.meshgrid(x,y)
    grid = np.vstack((xx.flatten(),yy.flatten())).T
    hwf = hydrogen_wave_function(grid,4,2,-1,a=1).reshape(xx.shape)
    probs = np.abs(hwf)**2
    plt.imshow(probs)
    plt.show()

    #3D
    z = np.linspace(-10,10,100)
    xx,yy,zz = np.meshgrid(x,y,z)
    grid = np.vstack((xx.flatten(),yy.flatten(),zz.flatten())).T
    hwf = hydrogen_wave_function(grid,4,2,-1,a=1).reshape(xx.shape)

if __name__ == '__main__':
    main()