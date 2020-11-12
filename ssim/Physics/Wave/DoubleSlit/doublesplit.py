import numpy as np
import matplotlib.pyplot as plt 

class Source:
    def __init__(self,position,intensity=4):
        self.pos = position
        self.intensity = intensity
        # self.phase = phase
    
    def compute_wave(self,grid):
        return self.intensity * np.sin(30*((grid[:,0]-self.pos[0])**2+(grid[:,1]-self.pos[1])**2)**0.5 )

def doublesplit(source1=Source((0,-0.5)) ,source2 = Source((0,0.5)),posx=(0,10),posy=(-5,5),precision=50,display = True):

    # Grid points
    precisiony = (max(posy)-min(posy))/(max(posx)-min(posx)) * precision
    x = np.linspace(posx[0],posx[1],precision)
    y = np.linspace(posy[0],posy[1],int(precisiony))
    xx,yy = np.meshgrid(x,y)
    grid = np.concatenate([xx.reshape(-1, 1), yy.reshape(-1, 1)], axis=-1)
    
    # Individual waves
    wave1 = source1.compute_wave(grid)
    wave2 = source2.compute_wave(grid)

    # Wave superposition
    final_wave = wave1 + wave2
    final_wave_intensity = final_wave **2

    if display :
        plt.xlim(*posx)
        plt.ylim(*posy)
        # Wave
        plt.scatter(grid[:,0],grid[:,1],c=final_wave_intensity,cmap=plt.cm.binary)
        # Sources
        plt.scatter(*source1.pos,c='blue')
        plt.scatter(*source2.pos,c='blue')
        plt.show()
    
    else :
        return final_wave_intensity