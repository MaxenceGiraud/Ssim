import numpy as np
import matplotlib.pyplot as plt

def sierpinski_carpet(iter = 5,display=True):

    def draw(squares):
        for i in range(squares.shape[1]):
            plt.fill(squares[:,i].real,squares[:,i].imag,c='black')

    if display :
        plt.xlim(0,1)
        plt.ylim(0,1)

    for i in range(iter):
        size = 3**i
        x = np.arange(1,size+1)
        y = np.arange(1,size+1)
        xx,yy = np.meshgrid(x,y)
        c = 1/(size+1)
        c = (c*xx+c*yy*1j).flatten()
        r = 1/(4+2**(3*i+1))
        rj = r * 1j

        squares = np.zeros((4,size**2),dtype=complex)
        squares[0] = c-r-rj
        squares[1] = c-r+rj
        squares[2] = c+r+rj
        squares[3] = c+r-rj
        
        if display :
            draw(squares)
    
    if display : 
        plt.axis('equal')
        plt.show()

def main():
    sierpinski_carpet(3)

if __name__ == "__main__":
    main()