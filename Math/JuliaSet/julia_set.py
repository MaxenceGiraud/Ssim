import numpy as np
import matplotlib.pyplot as plt

def juliaset(c,mandelbrot=False,posx = (-2,2),posy=(-2,2),n_iter = 100,precision =1000):
    '''Compute the divergence time of the series z_{n+1} = z_n**2 +c on the complex plane

    Parameters
    ----------
    c : complex,
        (ignored if mandelbrot is set to True)

    mandelbrot : bool,
    
    posx

    posy

    n_iter

    precision

    Yields
    ------
    n_iter_diverg : numpy array of shape (precision,precision)
                    Number of steps for which the series is gonna diverge (abs value > 2)

    '''

    # Initilize gridspace
    x = np.linspace(posx[0],posx[1],precision)
    y = np.linspace(posy[0],posy[1],precision)
    xx,yy = np.meshgrid(x,y)
    if mandelbrot : 
        z = 0
        c=  xx + 1j*yy
        n_iter_diverg = np.zeros(c.shape)
    else :
        z = xx + 1j*yy
        n_iter_diverg = np.zeros(z.shape)

    # Computing the serie
    for i in range(n_iter):
        z = z**2 +c
        div = np.abs(z)>2 # Check if its gonna diverge
        n_iter_diverg += i*div # if diverge, put index of divergence into tabe
        z[div] = np.nan # and stop counting for those numbers

    return  n_iter_diverg
