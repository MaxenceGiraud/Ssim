#%%
import numpy as np
import matplotlib.pyplot as plt 

class Source:
    def __init__(self,position,intensity=4,freq= 30,phase=0):
        self.pos = position
        self.intensity = intensity
        self.freq = freq
        self.phase = phase
    
    def compute_wave(self,grid):
        return self.intensity * np.sin(self.freq*((grid[:,0]-self.pos[0])**2+(grid[:,1]-self.pos[1])**2)**0.5 +self.phase)

def waves_interferences(sources = [Source((0,-0.5)) ,Source((0,0.5))],posx=(0,10),posy=(-5,5),precision=150,display = True):
    ''' Compute the intensity of the resulting wave on the grid and plot it

    Parameters
    ----------
    sources : list of Source object,
            list of all sources emitting waves
    posx : tuple,
            x limit of the grid
    posy : tuple,
            x limit of the grid
    precision : int,
             number of row pixels of the grid
    display : boolean, 
    '''

    # Grid points
    precisiony = (max(posy)-min(posy))/(max(posx)-min(posx)) * precision
    x = np.linspace(posx[0],posx[1],precision)
    y = np.linspace(posy[0],posy[1],int(precisiony))
    xx,yy = np.meshgrid(x,y)
    grid = np.concatenate([xx.reshape(-1, 1), yy.reshape(-1, 1)], axis=-1)
    
    # Individual waves
    waves = []
    for source in sources :
        waves.append(source.compute_wave(grid))

    # Wave superposition
    final_wave = np.sum(waves,axis=0)
    final_wave_intensity = final_wave **2

    if display :
        plt.xlim(*posx)
        plt.ylim(*posy)
        # Wave
        plt.imshow(final_wave_intensity.reshape(xx.shape),interpolation='sinc',cmap="inferno")
        # Sources
        for source  in sources :
            plt.scatter(*source.pos,c='blue')
        plt.show()
    
    else :
        return final_wave_intensity
# %%
