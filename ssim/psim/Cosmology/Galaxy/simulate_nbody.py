import numpy as np

def getAcc( pos, mass, G, softening):
    ''' Compute  acceleration on each particles using Newton's Law 
    Params
    ------
    pos   : array of shape (N,n_coord)
        Position matrix
    mass : array of shape (N,)
        Mass vector
    G : float,
        Newton's Gravitational constant
    softening : float,
        Softening length

    Yields
    ------
    acc : array of shape (N,n_coord)
        Acceleration matrix
    '''

    q = [pos[:,i:i+1] for i in range(pos.shape[1])] # Position coordonates
    
    iq = [q[i].T - q[i] for i in range(pos.shape[1])] # matrix that stores all pairwise particle separations: q_j - q_i

    # matrix that stores 1/r^3 for all particle pairwise particle separations 
    sumsq = np.sum(np.square(iq),axis=0)
    inv_r3 = (sumsq + softening**2)
    inv_r3[inv_r3>0] = inv_r3[inv_r3>0]**(-1.5)

    acc = (G * (iq * inv_r3) @ mass).reshape(len(q),pos.shape[0]).T

    return acc

def n_body(pos,mass,vel,tEnd=10.0,dt=0.01,softening=0.1,G = 1.0):
    ''' N-Body Simulation

    Params
    ------
    pos   : array of shape (N,3)
        Position matrix
    vel   : array of shape (N,3)
        Velocity matrix
    mass : array of shape (N,)
        Mass vector
    tEnd : int,
        Duration of the simulation
    dt : float,
        Timestep duration
    softening : float,
        softening length
    G : float,
        Newton's Gravitational Constant
    plot_energy : bool,
        Plot the Kinetic and potential energy (safety check to see if simulation went ok)
    animate : bool,
        Whether to create animation of the Simulation
    '''

    t  = 0 # current time of the simulation
    Nt = int(np.ceil(tEnd/dt))# number of timesteps


    # Convert to Center-of-Mass frame
    vel -= np.mean(mass * vel,0) / np.mean(mass)
    
    # calculate initial gravitational accelerations
    acc = getAcc( pos, mass, G, softening )

    pos_history = np.zeros((Nt,*pos.shape))

    # Simulation Main Loop
    for i in range(Nt):
        # (1/2) kick
        vel += acc * dt/2.0
        
        # drift
        pos += vel * dt
        
        # update accelerations
        acc = getAcc(pos, mass, G, softening )
        
        # (1/2) kick
        vel += acc * dt/2.0
        
        t += dt # update time
        
        pos_history[i] = pos
            
    return pos_history