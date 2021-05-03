import numpy as np
import sympy as smp
import matplotlib.pyplot as plt
from scipy.integrate import quad


def get_magnetic_field_f(l,nd=3):
    t, x, y, z = smp.symbols('t, x, y, z')

    r = smp.Matrix([x, y, z])
    sep = r-l

    integrand = smp.diff(l, t).cross(sep) / sep.norm()**3

    dBxdt = smp.lambdify([t, x, y, z], integrand[0])
    dBydt = smp.lambdify([t, x, y, z], integrand[1])
    dBzdt = smp.lambdify([t, x, y, z], integrand[2])

    if nd ==3 : 
        def magnetic_field(x, y, z):
            return np.array([quad(dBxdt, 0, 2*np.pi, args=(x, y, z))[0],
                            quad(dBydt, 0, 2*np.pi, args=(x, y, z))[0],
                            quad(dBzdt, 0, 2*np.pi, args=(x, y, z))[0]])

    magnetic_field = np.vectorize(magnetic_field, signature='(),(),()->(n)')

    return magnetic_field

def display_magnetic_field(wire='triloop',display="3d"):
    '''
    wire : str,
        Wire shape, either : 'loop','triloop','3dswirl'
    display : str,  
        Type of display, either 3d or 2d
    '''
    t  = smp.symbols('t')
    if wire == 'loop':
        wire = smp.Matrix([smp.cos(t), smp.sin(t), 0])
    elif wire == 'triloop':
        wire = (1+(3/4)*smp.sin(3*t))*smp.Matrix([smp.cos(t), smp.sin(t), 0])
    elif wire == '3dswirl' :
        wire = smp.Matrix([smp.cos(t), smp.sin(t), (t-smp.pi)/smp.pi])
    else : raise ValueError

    x = np.linspace(-2, 2, 10)
    xx, yy, zz = np.meshgrid(x, x, x)

    print("Computing analytic formulation of magnetic field")
    magnetic_field = get_magnetic_field_f(wire)

    print("Computing magnetic field")
    B_field = magnetic_field(xx,yy,zz)
    Bx,By,Bz = B_field[:,:,:,0],B_field[:,:,:,1],B_field[:,:,:,2]

    print("Plotting")

    if display=='2D' or display == '2d' :
        # 2D Plot
        Bx_plot,By_plot = Bx[:,:,0],By[:,:,0]
        color = 2 * np.log(np.hypot(Bx_plot, By_plot))
        plt.streamplot(xx[:,:,0], yy[:,:,0], Bx_plot, By_plot, color=color, linewidth=1, cmap="plasma",
                    density=1.5, arrowstyle='->', arrowsize=1,zorder=1)

        # Display wire
        wire_f = smp.lambdify([t], wire)
        phi = np.linspace(0, 2*np.pi, 100)
        w = wire_f(phi)
        plt.plot(w[0,0],w[1,0],zorder=2)


        plt.axis("off")
        plt.axis('equal')
        plt.show()


    elif display == "3D" or display == "3d":
        ax = plt.figure().add_subplot(projection='3d')

        ax.quiver(xx, yy, zz, Bx/2, By/2, Bz/2, length=0.1, normalize=False,color="blue")

        # Display wire
        wire_f = smp.lambdify([t], wire)
        phi = np.linspace(0, 2*np.pi, 100)
        w = wire_f(phi)
        ax.plot(w[0,0],w[1,0],w[2,0],zorder=2,c="red")

        plt.axis("off")
        plt.show()
    else :
        raise ValueError

if __name__ == "__main__":
    display_magnetic_field()