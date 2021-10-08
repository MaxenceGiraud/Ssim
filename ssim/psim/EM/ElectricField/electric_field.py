import numpy as np 
import matplotlib.pyplot as plt


def electric_field(q, r0, x, y):
    '''Compute the electric field vector E=(Ex,Ey) due to charge q at r0
    '''
    den = np.hypot(x-r0[0], y-r0[1])**2
    E = q * (x - r0[0]) / den, q * (y - r0[1]) / den
    return E

def display_electric_field(n_charges=4,pos_charges='random'):
    # Grid
    nx, ny = 50,50
    x = np.linspace(-2.5, 2.5, nx)
    y = np.linspace(-2.5, 2.5, ny)
    X, Y = np.meshgrid(x, y)

    # Create a multipole with n charges 
    charges = []
    for i in range(n_charges):
        q = i%2 * 2 - 1
        if pos_charges == "equal" :
            charges.append((q, (np.cos(2*np.pi*i/n_charges), np.sin(2*np.pi*i/n_charges))))
        elif pos_charges == "random" :
            charges.append((q,np.random.normal(0,0.7,n_charges)))
        else :
            raise ValueError

    # Electric field vector, E=(Ex, Ey)
    Ex, Ey = np.zeros((ny, nx)), np.zeros((ny, nx))
    for charge in charges:
        ex, ey = electric_field(*charge, x=X, y=Y)
        Ex += ex
        Ey += ey
    
    # Plot the vector field
    color = 2 * np.log(np.hypot(Ex, Ey))
    plt.streamplot(x, y, Ex, Ey, color=color, linewidth=1, cmap="plasma",
                density=1.5, arrowstyle='->', arrowsize=1,zorder=1)

    # Add dots for the charges themselves
    charge_colors = {True: 'red', False: 'blue'}
    for q, pos in charges:
        plt.plot(*pos,"o",c=charge_colors[q>0],zorder=2)

    plt.axis("off")
    plt.axis('equal')
    plt.show()

if __name__ == "__main__":
    display_electric_field(5,'equal')