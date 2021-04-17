import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

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
    
def getEnergy( pos, vel, mass, G ):
    ''' Compute kinetic energy (KE) and potential energy (PE) of simulation at a specific time

    Params
    ------
    pos   : array of shape (N,3)
        Position matrix
    vel   : array of shape (N,3)
        Velocity matrix
    mass : array of shape (N,)
        Mass vector
    G : float,
        Newton's Gravitational constant
    
    Yields
    ------
    KE : float,
        Kinetic Energy
    PE : float,
        Potential Energy
    '''
    # Kinetic Energy
    KE = 0.5 * np.sum( mass * vel**2 )


    # Potential Energy

    q = [pos[:,i:i+1] for i in range(pos.shape[1])]# Position coordonates

    
    iq = [q[i].T - q[i] for i in range(pos.shape[1])] # matrix that stores all pairwise particle separations: q_j - q_i

    # matrix that stores 1/r for all particle pairwise particle separations 
    inv_r = np.sqrt(np.sum(np.square(iq),axis=0))
    inv_r[inv_r>0] = 1.0/inv_r[inv_r>0]

    PE = G * np.sum(np.triu(-(mass*mass.T)*inv_r,1))
    
    return KE, PE
     

def generate_initial_conditions(N=100,randomseed=None):
    ''' Generate some initial conditions for N-Body simulation

    Params
    ------
    N : int,
        Number of particles
    randomseed : {None,int},
        Random seed fed into np.random.seed

    '''    
    np.random.seed(randomseed)  # set the random number generator seed
    
    mass = 20.0*np.ones((N,1))/N  # total mass of particles is 20, and each particle has the same mass

    # Randomly select positions and velocities
    pos  = np.random.randn(N,3)   
    vel  = np.random.randn(N,3)

    return pos,mass,vel

def n_body(pos,mass,vel,tEnd=10.0,dt=0.01,softening=0.1,G = 1.0,plot_energy=True,animate=True):
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

    KE,PE = getEnergy(pos,vel,mass,G) # Initial Kinetic & Potential Energy
    KE,PE = [KE],[PE]

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
        ke,pe = getEnergy(pos,vel,mass,G)
        KE.append(ke)
        PE.append(pe)

    if plot_energy:
        plot_energies(np.array(KE),np.array(PE))
    
    if animate : 
        create_animation(pos_history)
            
    return pos_history
    

def plot_energies(K,P,ax=None):
    ''' Plot Engergies and Total energy 

    Params
    ------
    K : array of size (N,),
        Kinetic energy
    T : array of size (N,),
        Potential energy
    '''
    ax = ax if ax is not None else plt.gca()
    
    ax.plot(K,label="Kinetic Engergy")
    ax.plot(P,label="Potential Engergy")
    ax.plot(K+P,label="Total Engergy")

    ax.set_xlabel("Time")
    ax.set_ylabel("Energy")
    ax.legend()
    plt.tight_layout()


def create_animation(pos,filename="nbody.mp4",play=True):
    ''' Create animation n-body simulation 

    Params
    ------
    pos : array of shape (n_frames,N,n_coord),
        Position history of particles
    filename : string,
        filename to write the video on
    play : bool,
        Whether to open the video
    '''

    def animate(i):
        ln1.set_xdata(pos[i,:,0])
        ln1.set_ydata(pos[i,:,1])
        ln2.set_xdata(pos[max(i-30,0):i+1,:,0].flatten())
        ln2.set_ydata(pos[max(i-30,0):i+1,:,1].flatten())

    plt.style.use('dark_background')
    fig, ax = plt.subplots(1,1, figsize=(8,8))
    ax.grid()
    ax.axis('off')
    ax.set_ylim(-2, 2)
    ax.set_xlim(-2,2)

    ln1, = ax.plot([],[],'o',markersize=8,c='red',zorder=1)
    ln2, = plt.plot([],[],'o',c='white',alpha=0.05,zorder=-1)

    ani = animation.FuncAnimation(fig, animate, frames=pos.shape[0], interval=50)
    ani.save(filename,writer=animation.FFMpegWriter(fps=25))

    print('ok')

    if play : 
        import os, sys, subprocess

        def open_file(filename):
            if sys.platform == "win32":
                os.startfile(filename)
            else:
                opener = "open" if sys.platform == "darwin" else "xdg-open"
                subprocess.call([opener, filename])
            
        open_file(filename)

  
if __name__== "__main__":
    pos,mass,vel = generate_initial_conditions(randomseed=42)
    pos_h = n_body(pos,mass,vel)