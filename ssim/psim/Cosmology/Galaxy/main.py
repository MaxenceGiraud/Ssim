from galaxy_gen import *
from simulate_nbody import n_body
import matplotlib.pyplot as plt
import matplotlib.animation as animation

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
        ln2.set_xdata(pos[max(i-30,0):i,:,0].flatten())
        ln2.set_ydata(pos[max(i-30,0):i,:,1].flatten())

    plt.style.use('dark_background')
    fig, ax = plt.subplots(1,1, figsize=(15,15))
    ax.grid()
    ax.axis('off')
    ax.set_ylim(-2, 2)
    ax.set_xlim(-2,2)

    ln1, = ax.plot([],[],'o',markersize=8,c='red',zorder=1)
    ln2, = ax.plot([],[],'o',c='white',alpha=0.05,zorder=-1)

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

def main():
    g = generate_3Dgalaxy(generate_2Dspiral_galaxy,n_points=200,n_arms=4)
    # g2 = generate_3Dgalaxy(generate_2Dspiral_galaxy,n_arms=4)
    # g2[:,2] +=  -2
    # plot_galaxy(np.concatenate((g2,g)))

    v = generate_velocity(g)

    mass = 20.0*np.ones((g.shape[0],1))/g.shape[0]

    posh = n_body(g,mass,v)
    create_animation(posh,filename='testgal.mp4')

    

if __name__ == "__main__":
    main()

#%%
g = generate_3Dgalaxy(generate_2Dspiral_galaxy,n_points=200,n_arms=4)
# v = generate_velocity(g)
v = np.zeros(g.shape)

mass = 20.0*np.ones((g.shape[0],1))/g.shape[0]

posh = n_body(g,mass,v,tEnd=5,dt=0.01)
create_animation(posh,filename='testgal.mp4')

#%%
g = generate_2Dspiral_galaxy(20)
v = generate_velocity(g,False)
# %%

ratio = g[:,1]/g[:,0]
v = np.vstack((-ratio,np.ones(g.shape[0]))).T
# v = v * 0.1/np.linalg.norm(v,axis=1).reshape(-1,1)
# %%
