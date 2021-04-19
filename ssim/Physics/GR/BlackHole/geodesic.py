import numpy as np

def compute_geodesic(alpha,D=50,dphi = np.pi/(360*60),n_iter_max=50000):
    '''
    Params
    ------
    alpha : ,
        angle of of geodesic from obserser
    D : float,
        Distance between center of BH and observer (we use a distance unit the radius of the black hole (which is fixed to 1))
    '''

    schwarz_radius = 1 # Fix the Schwarzschild radius of the BH

    # Integration constants/steps
    dphi = np.pi/(360*60)
    # phi_end = 1.1*np.pi
    
    # Initial conditions
    u  = 1/(D * np.ones(len(alpha)))
    u_d = 1/(D*np.tan(alpha)) # derivative of u wrt phi
    u_dd = 1.5 * schwarz_radius * u**2 - u

    phi = 0

    # phi_hist = np.zeros((len(alpha),n_iter_max))
    D_hist = np.zeros((len(alpha),n_iter_max))
    D_hist[:,0] = D * np.ones(len(alpha))

    idx_tocompute = np.ones(len(alpha),dtype=bool) # idx not to compute anymore as either inside BH or diverged
    idx_inside_bh = []
    arr= np.arange(len(alpha))

    for i in range(1,n_iter_max) :

        # Update params/ Integrate
        phi += dphi
        u_d[idx_tocompute] += u_dd[idx_tocompute] * dphi
        u[idx_tocompute] += u_d[idx_tocompute] * dphi 
        u_dd[idx_tocompute] = 1.5 * schwarz_radius * u[idx_tocompute]**2 - u[idx_tocompute]

        d_tmp = 1/u[idx_tocompute]
        if phi > dphi:
            # Geodesics that diverges
            diverg = np.where(abs(d_tmp - D_hist[idx_tocompute,i-1])>0.2)[0]
            idx_tocompute[np.where(idx_tocompute==True)[0][diverg]] = False
            d_tmp = 1/u[idx_tocompute]
        
        D_hist[idx_tocompute,i] = d_tmp
        # Geodesics inside BH
        inside_bh  = np.where(abs(d_tmp) <= schwarz_radius)[0]
        current_to_compute = np.where(idx_tocompute==True)[0]
        idx_inside_bh.extend(arr[current_to_compute[inside_bh]])
        idx_tocompute[current_to_compute[inside_bh]] = False
    
    return D_hist,idx_inside_bh


def main():
    import matplotlib.pyplot as plt

    alpha=np.linspace(0,np.pi/2,20)
    D=50
    dh,inside_bh = compute_geodesic(alpha=alpha)
    phi = np.arange(0,50000*np.pi/(360*60),np.pi/(360*60))

    dh_cut = []
    for i in range(dh.shape[0]):
        zer = np.where(dh[i]==0)[0]
        if zer.size == 0 :
            dh_cut.append(dh[i])
        else :
            if i in inside_bh :
            # last_non_zero = zer[1]
                zer = zer[1:]
            dh_cut.append(dh[i,:min(zer)])

    fig, ax = plt.subplots(figsize=(10,10))
    [ax.plot(np.sin(phi[:len(dh_cut[i])]) * dh_cut[i],np.cos(phi[:len(dh_cut[i])]) * dh_cut[i],c="grey") for i in range(int(dh.shape[0]))]
    ax.set_xlim((-D,D))
    ax.set_ylim((-D,D+D/5))

    ax.invert_yaxis()
    ax.set_xticks([])
    ax.set_yticks([])
    ax.scatter(0,D,c='red',label='Observer') # Observer

    bh = plt.Circle((0, 0), 1, color='black',label='Black Hole')# Black hole
    ax.add_patch(bh)
    plt.gca().set_aspect('equal', adjustable='box')
    ax.legend()

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()