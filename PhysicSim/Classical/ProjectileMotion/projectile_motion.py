import numpy as np

def projectile_motion_nodrag(m,v0,g=9.81):
    ''' Compute projection motion of an object (not drag accounted)
    Parameters
    ----------
    m : mass of the object (in kg)
    v0 : tuple of float
        Velocity of the object at t=0 (in m/s)
    g : float, 
        Gravity of the planet (m/s^2)
    
    Yields
    -----
    x : np array, shape : (1000,)
        x position of the object
    y : np array, shape : (1000,)
        y position of the object
    '''
    x_end = (2*v0[0]*v0[1]) /g
    #x_end = int(x_end)
    x = np.arange(0,x_end,(x_end/200))
    y = (v0[1]/v0[0]) *x - 0.5*g*(x/v0[0])**2
    return x,y


def projectile_motion_linear_drag(m,v0,D,beta = 1e-4,g=9.81):
    ''' Compute projection motion of an object considering only linear drag
    Parameters
    ----------
    m : mass of the object (in kg)
    v0 : tuple of float
        Velocity of the object at t=0
    D : float
        Linear size of the object (e.g. For a sphere its diameter)
    beta : float
        coefficient of linear drag (default to air on Earth)
    g : float,
        Gravity of the planet
    
    Yields
    -----
    x : np array, shape : (1000,)
        x position of the object
    y : np array, shape : (1000,)
        y position of the object
    '''
    g=9.81
    b=beta*D
    x_end = 2*v0[0]*(m/b) * (1-1/(1+((b*v0[1])/(m*g)))) # Got by put the deriv of y(x) to 0
    #R = 2*v0[0]*v0[1]/g *(1-(4/3)*(v0[1]*b)/(m*g) ) #From taylor Classical Mechanics using Taylor series
    x = np.arange(0,x_end,x_end/200)
    tau = m/b
    y = (v0[1]+tau*g)/v0[0] * x + tau**2*g*np.log(1-x/(v0[0]*tau)) 
    return x,y

def projectile_motion_quadratic_drag(m,v0,D,gamma = 0.25,g=9.81):
    ''' Compute projection motion of an object considering only Quadratic drag'''
    c = gamma * D**2
    return

def projectile_motion_drag(m,v0,D,gamma = 0.25,beta = 1e-4,g=9.81):
    ''' Compute projection motion of an object considering both Linear and Quadratic drag'''
    c = gamma * D**2
    b=beta*D
    return
