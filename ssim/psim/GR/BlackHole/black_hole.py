#%%
import numpy as np
from geodesic import compute_geodesic
import matplotlib.pyplot as plt
#%%

alpha=np.linspace(0,np.pi/4,300)
D=20
phi = np.arange(0,50000*np.pi/(360*60),np.pi/(360*60))
dh,inside_bh = compute_geodesic(alpha=alpha,D=D)

inside_idx =  max(inside_bh)
# %%
outside_bh = np.ones(dh.shape[0],dtype=bool)
outside_bh[inside_bh]= False

dh_cut = []
for i in range(inside_idx+1,dh.shape[0]):
    zer = np.where(dh[i]==0)[0]
    if zer.size == 0 :
        dh_cut.append(dh[i])
    else :
        dh_cut.append(dh[i,:min(zer)])

# %%
x = np.zeros((len(dh_cut),2))
y = np.zeros((len(dh_cut),2))
for i,d in enumerate(dh_cut) :
    x[i] = np.sin(phi[len(d)-1:len(d)]) * d[-2:]
    y[i] = np.cos(phi[len(d)-1:len(d)]) * d[-2:]

slope = (y[:,1]-y[:,0])/(x[:,1]-x[:,0])
intercept= y[:,1] - slope * x[:,1]

r = 200

# Compute intersection line and circle
a= (1+slope**2)
b2 = (slope*intercept)**2
delta= b2 - 4*a*(intercept**2-r**2)

x_inter = (b2 + np.sqrt(delta))/(2*a)
y_inter = slope*x_inter + intercept

theta = np.arctan2(y_inter,x_inter)
# %%

i=8

angle = np.linspace(0,2*np.pi,100)
x_circle = r * np.cos(angle)
y_circle = r * np.sin(angle)

plt.plot(x_circle,y_circle,zorder=1)

plt.plot(x[i],y[i],"-->",zorder=3)

xx = np.linspace(-120,120,100)
yy = slope[i] * xx + intercept[i]
plt.plot(xx,yy,zorder=2)


plt.plot(x_inter[i],y_inter[i],"o",zorder=4)
plt.axis("equal")

plt.ylim(-1500,1500)

# %%


def find_angles(path_list,r=100):
    ''' Given a list of path return the angles for which those path intercept with the circle of radius r

    Parameters
    -----------
    path_list : list of size n of array of shape (n_i)
        List of path 
    r : float,
        Radius of the circle
    
    Yields
    ------
    theta : array of shape (n,)
        Angles of intersection between paths and circle
    '''
    x = np.zeros((len(path_list),2))
    y = np.zeros((len(path_list),2))
    for i,d in enumerate(path_list) :
        x[i] = np.sin(phi[len(d)-1:len(d)]) * d[-2:]
        y[i] = np.cos(phi[len(d)-1:len(d)]) * d[-2:]

    slope = (y[:,1]-y[:,0])/(x[:,1]-x[:,0])
    intercept= y[:,1] - slope * x[:,1]

    # Compute intersection line and circle
    a= (1+slope**2)
    b2 = (slope*intercept)**2
    delta= b2 - 4*a*(intercept**2-r**2)

    x_inter = (b2 - np.sqrt(delta))/(2*a) # TODO : how to find if +- ???
    y_inter = slope*x_inter + intercept

    theta = np.arctan2(y_inter,x_inter)

    return theta


class SphericalImg:
    ''' Taking a classical img, use it as if it was projected on a sphere

    si = SphericalImg(img)
    si[theta,phi] = pixel of the image corresponding to the point on the sphere with spherical coordonate (r,theta,phi)

    Parameters
    ----------
    img : numpy array of shape (n,m),
        input img
    '''
    def __init__(self,img):
        self.img = img
    
    def get_coord_from_sph(self,theta,phi):
        # cosphi = 1- np.cos(phi)
        # sinphi = np.sin(phi)
        # x = (np.cos(theta)*sinphi)/cosphi # https://math.stackexchange.com/questions/3766972/inverse-of-stereographic-projection
        # y = (np.sin(theta)*sinphi)/cosphi

        # # Normalize to fit image and convert to np
        # return [np.array(((x+2)/4) * self.img.shape[0],dtype=int) ,np.array(((y+2)/4) * self.img.shape[1],dtype=int)]

        r= 1/np.arctan(phi/2)
        x = r * np.cos(theta)
        y = r * np.sin(theta)

        return x,y
        
    
    def __getitem__(self,coords):   
        x,y = self.get_coord_from_sph(*coords)     
        return self.img[x,y]
    
#%%


ib = np.linspace(0,100,1000)
xi,yi = np.meshgrid(ib,ib)
i = 5000 - (abs(xi-50)+abs(yi-50))
plt.imshow(i)
si = SphericalImg(i)
#%%
resulting_img = np.zeros((2*len(dh)-1,2*len(dh)-1))
phi = np.linspace(0.01,2*np.pi,20)

tt,pp = np.meshgrid(theta,phi)

si[theta,np.ones(theta.size)]


# %%

si.get_coord_from_sph(theta,pp)


# %%
phi = np.ones(theta.size)

cosphi = 1- np.cos(phi)
sinphi = np.sin(phi)
x = (np.cos(theta)*sinphi)/cosphi
y = (np.sin(theta)*sinphi)/cosphi
# %%

xa = np.linspace(0.01,2*np.pi-0.01,200)
a1,a2 = np.meshgrid(xa,xa)

r= 1/np.arctan(a2/2)
x = r * np.cos(a1)
y = r * np.sin(a1)

# %%
np.where(x==np.inf)

# %%

R = np.sqrt(xi**2 + yi**2)
angle = np.arctan2(yi,xi)

s_phi = 2 * np.arctan(1/R)
s_theta = angle
# %%
