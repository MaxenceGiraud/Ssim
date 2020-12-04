from galaxy_gen import *


def main():
    g = generate_3Dgalaxy(generate_2Dspiral_galaxy,n_arms=4)
    plot_galaxy(g)

if __name__ == "__main__":
    main()