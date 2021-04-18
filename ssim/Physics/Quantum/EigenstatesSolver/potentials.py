import numpy as np

def infinite_well_1D(x):
    return np.zeros(len(x)) 

def infinite_well_2D(x,y):
    return np.zeros((len(x),len(y)))

def finite_well_1D(x,well_range=(0.25,0.75)):
    box= np.where(x>well_range[0],1,0) + np.where(x<well_range[1],1,0)
    return np.where(box==2,0,1e15)

def finite_well_2D(x,y,well_range_x=(0.25,0.75),well_range_y=(0.25,0.75)):
    box = np.where(x>well_range_x[0],1,0) + np.where(x<well_range_x[1],1,0) + np.where(y>well_range_y[0],1,0) + np.where(y<well_range_y[1],1,0)
    return np.where(box==4,0,1e15)

def Gaussian_1D(x,mu=0.5,sigma=0.1):
    return np.exp(-(x-mu)**2/(2*sigma**2))

def Gaussian_2D(x,y,mu_x = 0.3,mu_y=0.3,sigma_x=0.1,sigma_y=0.1):
    return np.exp(-(x-mu_x)**2/(2*sigma_x**2))*np.exp(-(y-mu_y)**2/(2*sigma_y**2))