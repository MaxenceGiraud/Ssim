import numpy as np
import matplotlib.pyplot as plt
from galaxy_gen import generate_spiral_galaxy


def main():
    g = generate_spiral_galaxy(3)
    plt.plot(g[:,0],g[:,1],"+",c='black')
    plt.axis('equal')
    plt.show()

if __name__ == "__main__":
    main()