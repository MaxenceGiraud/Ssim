import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def generate_1arm2D(n_points = 500,a=1.5,b=0.4):
    ''' Generate an arm of of galaxy '''
    theta=np.random.randn(n_points)
    x=a*np.exp(b*theta)*np.cos(theta) + np.random.normal(0, 0.25, n_points)
    y=a*np.exp(b*theta)*np.sin(theta) + np.random.normal(0, 0.25, n_points)
    
    return np.array([x,y])

def rotate(points,phi):
    R = [[ np.cos(phi), -np.sin(phi) ], [ np.sin(phi), np.cos(phi) ]]
    return points.T @ R

def generate_2Dspiral_galaxy(n_points=2000,n_arms=3):
    n_center = int(n_points/4)
    arm_samples = int((n_points-n_center)/n_arms)
    points = np.zeros((n_points,2))
    
    for i in range(n_arms):
        angle = 2*i*np.pi/n_arms#np.random.normal(2*i*np.pi/n_arms,np.pi/(n_arms*10))
        p = generate_1arm2D(arm_samples)
        points[i*arm_samples:arm_samples*(i+1)] = rotate(p,angle)

    # Center of the galaxy
    points[-n_center:] = np.random.normal(0,0.4,2*n_center).reshape((n_center,2))

    return points

def generate_2Delliptical_galaxy(n_points=2000,max_radius=3):
    x = np.random.normal(0,1.8,size=n_points)
    y = np.random.normal(0,1.5,size=n_points)
    to_reduce = np.where(x**2+y**2 > max_radius**2,1,0 )
    galaxy = np.array([x,y]).T
    galaxy[to_reduce] /= 4
    return galaxy

def add_zdim(points):
    z = np.random.normal(0,0.04,size=points.shape[0]).reshape((-1,1))
    return np.concatenate((points,z),axis=1)

def generate_3Dgalaxy(gen2d=generate_2Dspiral_galaxy,n_points=2000,*args,**kwargs):
    return add_zdim(gen2d(n_points=n_points,*args,**kwargs))

def plot_galaxy(galaxy):
    if galaxy.shape[1] == 2 :
        plt.plot(galaxy[:,0],galaxy[:,1],"+",c='black')
        plt.axis('equal')
        plt.show()
    elif galaxy.shape[1] == 3 :
        fig = plt.figure()
        ax = fig.gca(projection="3d")
        ax.set_zlim(-2,2)
        ax.plot(galaxy[:,0],galaxy[:,1],galaxy[:,2],"+",c='darkgreen')
        plt.show()
    else : 
        raise Exception
