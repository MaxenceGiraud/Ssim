import numpy as np
import matplotlib.pyplot as plt

def juliaset(c,mandelbrot=False,posx = (-2,2),posy=(-2,2),n_iter = 100,precision =1000,display=True,colormap='Spectral'):
    '''Compute the divergence time of the series z_{n+1} = z_n**2 +c on the complex plane

    Parameters
    ----------
    c : complex,
        (ignored if mandelbrot is set to True)
        Constant term in the serie

    mandelbrot : bool,
        If set to True compute the mandelbrot set, otherwise compute a julia set. Default to False
    
    posx : tuple, (float,float)
        X axis of the grid

    posy : tuple, (float,float)
        Y axis of the grid

    n_iter : int,
        Number of iterations the series is done

    precision : int,
        resolution on the x axis, y resolution is determined based on the difference of the size of the x and y axis length.

    Yields
    ------
    n_iter_diverg : numpy array of shape (precision,precision)
        Number of steps for which the series is gonna diverge (abs value > 2)

    '''

    # Initilize gridspace
    precisiony = (max(posy)-min(posy))/(max(posx)-min(posx)) * precision # adapt y precision if grid not a square
    x = np.linspace(posx[0],posx[1],precision)
    y = np.linspace(posy[0],posy[1],int(precisiony))
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
        n_iter_diverg += i*div # if diverge, put index of divergence into table
        z[div] = np.nan # and stop counting for those numbers

    log_iter_div = np.log(n_iter_diverg+1)

    if display :
        plt.figure(figsize=(15,15))
        plt.imshow(log_iter_div,cmap=colormap,extent=(posx[0],posx[1],posy[0],posy[1]))
        plt.xlabel("Re(z)")
        plt.ylabel("Im(z)")
        if mandelbrot : 
            plt.title('Mandelbrot Set')
        else :
            plt.title('Julia Set with c='+str(c))
        plt.plot()

    return  log_iter_div
