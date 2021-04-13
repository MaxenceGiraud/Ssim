#%%
import sympy as smp
from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt
from copy import deepcopy
from matplotlib import animation
from matplotlib.animation import PillowWriter

# def n_pendulum(n_pendulum):
#%%

t, m, g, k = smp.symbols('t m g k')

n_pendulum = 3

# %%

thetas = [smp.symbols(r'\theta_{}'.format(i), cls=smp.Function)(t) for i in range(n_pendulum)]
thetas_d = [smp.diff(thetas[i],t) for i in range(n_pendulum)]
thetas_dd = [smp.diff(thetas_d[i],t) for i in range(n_pendulum)]

r = [smp.symbols(r'r_{}'.format(i), cls=smp.Function)(t) for i in range(n_pendulum)]
r_d = [smp.diff(r[i],t) for i in range(n_pendulum)]
r_dd = [smp.diff(r_d[i],t) for i in range(n_pendulum)]
#%%

x = [smp.symbols(r'x_{}'.format(i), cls=smp.Function) for i in range(n_pendulum)]
y = [smp.symbols(r'y_{}'.format(i), cls=smp.Function) for i in range(n_pendulum)]
#%%
T = 0 # Kinetic energy
V = 0 # Potential energy

for i in range(n_pendulum):
    # params = [thetas[j] for j in range(i+1)]
    # params.extend([r[j] for j in range(i+1)])
    # x[i] = x[i](*params)
    # y[i] = y[i](*params)

    if i ==0 :
        x[0] = (1+r[0])*smp.cos(thetas[0])
        y[0] = -(1+r[0])*smp.sin(thetas[0])

    else :
        x[i] = x[i-1] + (1+r[i])*smp.cos(thetas[i])
        y[i] = y[i-1] - (1+r[i])*smp.sin(thetas[i])
    
    T = T + smp.diff(x[i], t)**2 + smp.diff(y[i], t)**2 
    V = V + m*g*y[i] + 1/2 * k * r[i]**2

T = 1/2*m*T
L = T-V # Lagrangian
# %%

## Lagrange equations

LE = [smp.diff(L,thetas[i]) - smp.diff(smp.diff(L,thetas_d[i]),t) for i in range(n_pendulum)]
LE_r = [smp.diff(L,r[i]) - smp.diff(smp.diff(L,r_d[i]),t) for i in range(n_pendulum)]

LE.extend(LE_r) 
LE = [LE[i].simplify() for i in range(len(LE))] 
# %%
params = deepcopy(thetas_dd)
params.extend(r_dd)
sols = smp.solve(LE, (*params),simplify=False, rational=False)
#%%
all_params = [m,k,g]
all_params.extend(thetas)
all_params.extend(thetas_d)
all_params.extend(r)
all_params.extend(r_d)

# Create functions to use with our numerical methods
dwdt_f = [smp.lambdify(all_params,sols[thetas_dd[i]]) for i in range(n_pendulum)]
dthetasdt_f = [smp.lambdify(thetas_d[i], thetas_d[i]) for i in range(n_pendulum)]
dvdt_f = [smp.lambdify(all_params,sols[r_dd[i]]) for i in range(n_pendulum)]
drdt_f = [smp.lambdify(r_d[i], r_d[i]) for i in range(n_pendulum)]

# %%

# Define our system of ODEs


def dSdt(S, t):
    S_np = np.reshape(S,(int(len(S)/n_pendulum),n_pendulum))
    thetas,r , w ,v = S_np
    return [
        *[dthetasdt_f[i](w[i]) for i in range(n_pendulum)],
        *[drdt_f[i](v[i]) for i in range(n_pendulum)],
        *[dwdt_f[i](m,k,g,*thetas,*w,*r,*v)for i in range(n_pendulum)],
        *[dvdt_f[i](m,k,g,*thetas,*w,*r,*v) for i in range(n_pendulum)]
    ]

# %%

# Define constants
t = np.linspace(0, 20, 1000)
g = 9.81
m=1
k=10

#%%
# Solve ODEs
theta_init = [np.pi/2,(3/2)*np.pi/2]
r_init = [0 for i in range(n_pendulum)]
w_init = [0 for i in range(n_pendulum)]
v_init = [5 for i in range(n_pendulum)]

ans = odeint(dSdt, y0=[*theta_init,*r_init,*w_init,*v_init], t=t)
# %%


# Compute x,y coordonates
def get_xy(thetas,r):

    x = [(1+r[0])*np.cos(thetas[0])]
    y = [-(1+r[0])*np.sin(thetas[0])]

    for i in range(1,n_pendulum):
        x.append(x[i-1] + (1+r[i])*np.cos(thetas[i]))
        y.append(y[i-1] - (1+r[i])*np.sin(thetas[i]))

    return x,y

x,y = get_xy(ans.T[:n_pendulum],ans.T[n_pendulum:n_pendulum*2])

# %%

def animate(i):
    ln1.set_data([[0,*[x[j][i] for j in range(n_pendulum)]], [0,*[y[j][i] for j in range(n_pendulum)]]])
    
fig, ax = plt.subplots(1,1, figsize=(8,8))
ax.grid()
ln1, = plt.plot(*[[] for _ in range(n_pendulum)], 'ro--', lw=3, markersize=8)
ax.set_ylim(-10, 10)
ax.set_xlim(-15,10)
ani = animation.FuncAnimation(fig, animate, frames=1000, interval=50)
ani.save('2npen.gif',writer='pillow',fps=50)
# %%
