import numpy as np
from scipy.special import eval_genlaguerre,lpmv,binom,factorial
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

def laguerre_assoc():
    pass

def legendre_assoc(x,l,m):
    k = np.arange(m,l)
    return (-1)**m * 2**l  *(1-x**2)**(m/2) * np.sum(factorial(k)/factorial(k-m) * x**(k-m) * binom(l,k)* binom((l+k-1)/2,l))

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
    sqrt_term = (2/(n*a)) **3 * factorial(n-l-1)/(2*n*factorial(n+l))
    exp_term = -r/(n*a)
    third_term = (2*r/(n*a))**l
    
    return np.sqrt(sqrt_term) * np.exp(exp_term) * third_term * laguerre


# equivalent to scipy.special.sph_harm
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
    first_term = np.sqrt( ((2*l+1) * factorial(l-m)) / (4*np.pi *factorial(l+m) ) ) * np.exp(1j * m * phi) 
    legendre = lpmv(m,l,np.cos(theta))
    # legendre = legendre_assoc(np.cos(theta),l,m)

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
    assert n > 0, "n must be greater than 0"
    assert l < n and l>=0, "l must be between 0 and n-1"
    assert m <= l and m>=-l, "m must be between -l and l"

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

def plot_hydrogen_orbitals(n=2,l=0,m=0,precision=800,posx=(-10,10),posy=(-10,10),posz=None):
    ''' Plot hydrogen orbitals in 1/2/3D'''

    ## 1D
    if posy == None :
        grid = np.linspace(posx[0],posx[1],precision)
        hwf = hydrogen_wave_function(grid,n,l,m,a=1)
        probs = np.abs(hwf)

        # Plotting
        plt.plot(grid,probs)
        plt.title(f"Radial Wave function with n={n}, l={l}, m={m}")
        plt.show()
    
    ## 2D
    elif posz == None :
        precisiony = int((max(posy)-min(posy))/(max(posx)-min(posx)) * precision) # adapt y precision if grid not a square

        # Creating grid points 
        x= np.linspace(posx[0],posx[1],precision)
        y = np.linspace(posy[0],posy[1],precisiony)
        xx,yy = np.meshgrid(x,y)
        grid = np.vstack((xx.flatten(),yy.flatten())).T
        hwf = hydrogen_wave_function(grid,n,l,m,a=1).reshape(xx.shape)
        probs = np.abs(hwf)**0.7 # the power here is simply for plotting purposes

        # Plotting
        plt.imshow(probs,cmap='magma')
        plt.axis('off')
        title = "Hydrogen orbitals with n="+str(n)+", l="+str(l)+", m="+str(m)
        plt.title(title)
        plt.show()

    ## 3D
    else :
        raise NotImplementedError("3D plots is not yet implemented")

        precisiony = int((max(posy)-min(posy))/(max(posx)-min(posx)) * precision) 
        precisionz = int((max(posz)-min(posz))/(max(posx)-min(posx)) * precision) 

        # Creating grid points 
        x= np.linspace(posx[0],posx[1],precision)
        y = np.linspace(posy[0],posy[1],precisiony)
        z = np.linspace(posz[0],posz[1],precisionz)
        xx,yy,zz = np.meshgrid(x,y,z)
        grid = np.vstack((xx.flatten(),yy.flatten(),zz.flatten())).T

        hwf = hydrogen_wave_function(grid,n,l,m,a=1).reshape(xx.shape)
        probs = np.abs(hwf)**0.7 # the power here is simply for plotting purposes

        to_include = probs.flatten() >= 1e-4 # Datapoints to include, in order not to have a filled cube ()

        # Plotting
        title = "Hydrogen orbitals with n="+str(n)+", l="+str(l)+", m="+str(m)
        # TODO
    

def main():

    # 1D
    plot_hydrogen_orbitals(posx=(0,10),posy=None)
    # 2D
    plot_hydrogen_orbitals(4,1,-1)
    
    #3D
    # plot_hydrogen_orbitals(posz=(-12,12))

if __name__ == '__main__':
    main()