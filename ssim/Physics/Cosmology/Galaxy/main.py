from galaxy_gen import *
from simulate_nbody import simulate_nbody


def main():
    g = generate_3Dgalaxy(generate_2Dspiral_galaxy,n_arms=4)
    g2 = generate_3Dgalaxy(generate_2Dspiral_galaxy,n_arms=4)
    g2[:,2] +=  -2
    plot_galaxy(np.concatenate((g2,g)))

if __name__ == "__main__":
    main()