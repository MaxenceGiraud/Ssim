import numpy as np

## Constant definitions
G = 6.674e-11

def update_nbody(pos,v,mass,step = 0.01):
    ''' Simulate 1 step of N Body system

    Parameters
    ----------
    pos : array of size (n,d),
        positions of the bodies (n bodies with d dimensions).
    v : array of size n,
        Velocity of bodies.
    mass : array of size n,
        mass of bodies
    time : float,
        Time of the simulation
    step : float,
        Time step

    Yields
    ------
    new_pos : array of size (n,d),
        New positions
    v : array of size n,
        New velocities
    '''
    # Compute new position
    new_pos = pos + v * step

    # Compute new velocity/acc
    center_ofmass =  ( np.sum(mass * pos,axis=0) - mass *pos) / np.sum(mass) 
    dist_squared = np.sum((pos - center_ofmass)**2,axis=1) # dist between points and CM of other points
    g =  G * (mass * (np.sum(mass)-mass) ) / dist_squared.reshape(-1,1) # gravional force
    acc_direction_unnormalized = center_ofmass - pos  
    acc_direction = acc_direction_unnormalized/np.linalg.norm(acc_direction_unnormalized,axis=1).reshape(-1,1)
    acc = g * acc_direction / mass # Compute acceleration
    v = v+ acc * step # new velocity
    
    return new_pos,v

def simulate_nbody(pos,v,mass,time = 100,step = 'auto',max_dist= 1,return_pos_history=True):
    ''' Simulate N Body system

    Parameters
    ----------
    pos : array of size (n,d),
        positions of the bodies (n bodies with d dimensions).
    v : array of size n,
        Velocity of bodies.
    mass : array of size n,
        mass of bodies
    time : float,
        Time of the simulation
    step : float or 'auto',
        Step of each iteration. If set to auto use the max_dist param to compute it.
    max_dist : float,
        maxium distance for 1 iter (used only when step is set to 'auto').
    return_pos_history  : Boolean,
        Whether to return the all history of positions or simply last positions.

    Yields
    ------
    pos_history : array of size (time/step,n,d),
        History of positions of particles
    '''
    
    pos_history = [pos]
    t = 0
    while t < time :
        if step == 'auto':
            step_t =   max(max_dist/np.sum(v**2,axis=1).max(),0.1)
        else : 
            step_t = step

        new_pos,v = update_nbody(pos_history[-1],v,mass,step=step_t)
        pos_history.append(new_pos)
        t += step_t
    
    if return_pos_history: 
        return pos_history
    
    else :
        return pos_history[-1]