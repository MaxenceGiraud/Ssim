import numpy as np
import matplotlib.pyplot as plt

def bogdanov_map(eps=0,k=1.2,mu=0,posx=(-0.7,1.3),posy=(-1,1),precision=800,iter=200,display=True):
    
    # Initilize gridspace
    precisiony = int((max(posy)-min(posy))/(max(posx)-min(posx)) * precision) # adapt y precision if grid not a square
    xa = np.linspace(posx[0],posx[1],precision)
    ya = np.linspace(posy[0],posy[1],precisiony)
    x,y = np.meshgrid(xa,ya)
    
    n_iter_diverg = np.zeros(x.shape)

    def bogdanov_step(x,y):
        y = y*(1+eps+mu*x) + k*x*(x-1)
        x = x+y
        return x,y 
    
    for _ in range(iter):
        not_div = np.where(np.abs(y)>2,False,True) + np.where(np.abs(x)>2,False,True)
        n_iter_diverg[not_div] += 1

        x[not_div],y[not_div] = bogdanov_step(x[not_div],y[not_div])
    
    if display :
        plt.imshow(np.sqrt(n_iter_diverg),cmap=plt.cm.binary)
        plt.show()
    
    return n_iter_diverg

def main():
    b = bogdanov_map(precision=1500)

if __name__ == "__main__":
    main()