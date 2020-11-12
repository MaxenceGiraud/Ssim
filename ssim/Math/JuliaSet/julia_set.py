import numpy as np
import matplotlib.pyplot as plt

def juliaset(c,init_with_constant=False,posx = (-2,2),posy=(-2,2),n_iter = 100,precision =1000,display=True,colormap='Spectral',f = lambda z,c : z**2 +c,div_threshold = 2 ):
    '''Compute the divergence time of the series z_{n+1} = z_n**2 +c on the complex plane

    Parameters
    ----------
    c : complex,
        Constant term in the serie (or first term of the serie if init_with_constant is set to true)

    init_with_constant : bool,
        If set to True the constant term of the serie is fed the complex position on the grid and the first term of the serie is set to c, otherwise do the opposite.
        Default to False
    
    posx : tuple, (float,float)
        X axis of the grid

    posy : tuple, (float,float)
        Y axis of the grid

    n_iter : int,
        Number of iterations the series is done

    precision : int,
        resolution on the x axis, y resolution is determined based on the difference of the size of the x and y axis length.
    
    f : lambda function,
        Function used to compute the julia set J(f)
    
    div_threshold : float,
        threshhold from which the serie diverges

    Yields
    ------
    log_iter_div : numpy array of shape (precision,precision)
        log of the number of steps for which the series is gonna diverge (by default abs value of zn > 2)

    '''
    # Initilize gridspace
    precisiony = (max(posy)-min(posy))/(max(posx)-min(posx)) * precision # adapt y precision if grid not a square

    x = np.linspace(posx[0],posx[1],precision)
    y = np.linspace(posy[0],posy[1],int(precisiony))
    xx,yy = np.meshgrid(x,y)

    if init_with_constant : 
        z = c
        c=  xx + 1j*yy
        n_iter_diverg = np.zeros(c.shape)
    else :
        z = xx + 1j*yy
        n_iter_diverg = np.zeros(z.shape)

    # Computing the serie
    for i in range(n_iter):
        z = f(z,c)

        # Check if its gonna diverge
        #div = (np.abs(z_new)-np.abs(z))>div_threshold  
        #div = (np.abs(z_new)-np.abs(z))<div_threshold 
        div = np.abs(z)>div_threshold

        n_iter_diverg += i*div # if diverge, put index of divergence into table
        #z[div] = np.nan # and stop counting for those numbers



    log_iter_div = np.log(n_iter_diverg+1)

    if display :
        plt.figure(figsize=(15,15))
        plt.imshow(log_iter_div,cmap=colormap,extent=(posx[0],posx[1],posy[0],posy[1]))
        plt.xlabel("Re(z)")
        plt.ylabel("Im(z)")
        '''
        if init_with_constant : 
            plt.title('Mandelbrot Set')
        else :
            plt.title('Julia Set with c='+str(c)+'and '+str(inspect.getsourcelines(f)[0][0]))
        '''
        plt.plot()

    return  n_iter_diverg
