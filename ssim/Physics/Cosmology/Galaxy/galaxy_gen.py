import numpy as np

def generate_1arm_galaxy(n_points = 500,a=1.5,b=0.6):
    ''' Generate an arm of of galaxy '''
    theta=np.random.randn(n_points)
    x=a*np.exp(b*theta)*np.cos(theta)
    y=a*np.exp(b*theta)*np.sin(theta)

    sx=np.random.normal(0, 0.25, n_points)
    sy=np.random.normal(0, 0.25, n_points)
    
    return np.array([x+sy, y+sx])

def rotate(points,phi):
    R = [[ np.cos(phi), -np.sin(phi) ], [ np.sin(phi), np.cos(phi) ]]
    return points.T @ R

def generate_spiral_galaxy(n_arms=3,n_points=1000):
    n = int(n_points/n_arms)
    points = np.zeros((n_points,2))
    for i in range(n_arms):
        angle = 2*i*np.pi/n_arms#np.random.normal(2*i*np.pi/n_arms,np.pi/(n_arms*10))
        p = generate_1arm_galaxy(n)
        points[i*n:n*(i+1)] = rotate(p,angle)
    return points[:(i+1)*n]