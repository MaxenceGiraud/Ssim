import numpy as np
from scipy.linalg import eigh_tridiagonal
import matplotlib.pyplot as plt
import scipy.sparse
import scipy.sparse.linalg as sparsealg

from potentials import infinite_well_2D,Gaussian_2D

def compute_1D_eigenstates(potential,x=np.linspace(0,1,100)):
    N = len(x)
    dx = 1/N

    d = 1/dx**2 + potential(x) # Diagonal element of the matrix
    e = -1/(2*dx**2) * np.ones(len(d)-1) # Off-diagonal element of the matrix

    # Compute eigenvectors
    _, eigen_v = eigh_tridiagonal(d, e)

    return eigen_v.T


def plot_1D_eigenstates(potential,x_range=np.linspace(0,1,100),n_states=5):
    eigen_v = compute_1D_eigenstates(potential,x_range)

    for i in range(n_states):
        plt.plot(x_range,eigen_v[i],label=f"N={i}")
    
    plt.legend()
    plt.show()


def compute_2D_eigenstates(potential,grid_range=(0,1),precision=100,n_states= 5):
    # Grid space
    x,y = np.meshgrid(np.linspace(grid_range[0],grid_range[1],precision),np.linspace(grid_range[0],grid_range[1],precision))

    # Compute potential on grid
    V = potential(x,y)

    # 3  Diagonal elements 
    diag = np.ones(precision)
    diags = np.array([diag, -2*diag, diag])
    D = scipy.sparse.spdiags(diags, np.array([-1,0,1]), precision, precision)

    # Transform into a proper matrix
    T = -1/2 * scipy.sparse.kronsum(D,D)
    U = scipy.sparse.diags(V.reshape(precision**2), (0))
    H = T+U 

    # Compute eigenvectors (only those corresponding to smallest eigenvalues)
    _, eigen_vec = sparsealg.eigsh(H, k=n_states, which='SM')

    return eigen_vec.T

def plot_2D_eigenstates(potential,grid_range=(0,1),precision=100,states_to_plot= (1,2,3,4)):
    eigen_vec = compute_2D_eigenstates(potential,grid_range,precision,np.max(states_to_plot))

    #fig,ax = plt.subplots()
    for i in states_to_plot :
        plt.contourf(eigen_vec[i-1].reshape(precision,precision)**2)
        plt.title(f"N={i}")
        plt.axis("off")
        plt.show()
    
def main():
    # 2D infinite Well
    states_to_plot = np.arange(1,17)
    fig,ax = plt.subplots(4,4,figsize=(15,15))
    eigen_vec = compute_2D_eigenstates(infinite_well_2D,n_states=np.max(states_to_plot))

    for i in states_to_plot :
        ax[(i-1)%4,int((i-1)/4)].contourf(eigen_vec[i-1].reshape(100,100)**2)
        ax[(i-1)%4,int((i-1)/4)].set_title(f"N={i}")
        ax[(i-1)%4,int((i-1)/4)].axis("off")
    
    plt.suptitle("Infinite Well")
    plt.axis("off")
    plt.tight_layout()
    plt.show()

    # 2D Gaussian
    states_to_plot = np.arange(1,17)
    fig,ax = plt.subplots(4,4,figsize=(15,15))
    eigen_vec = compute_2D_eigenstates(Gaussian_2D,n_states=np.max(states_to_plot))

    for i in states_to_plot :
        ax[(i-1)%4,int((i-1)/4)].contourf(eigen_vec[i-1].reshape(100,100)**2)
        ax[(i-1)%4,int((i-1)/4)].set_title(f"N={i}")
        ax[(i-1)%4,int((i-1)/4)].axis("off")
    
    plt.suptitle("Gaussian potential")
    plt.axis("off")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()