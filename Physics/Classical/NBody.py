import numpy as np

## Constant definitions
G = 6.674e-11

def gravitation_newton(m1,m2,r):
    ''' Compute the Gravitionnal (according to Newton) force between 2 objects'''
    squared_dist = np.sign(r)*r**2 # signed squared distance
    return G * (m1+m2) / squared_dist

def acc(mass,other_mass,distance):
    return gravitation_newton(mass,other_mass,distance)/mass

def center_of_mass(list_bodies):
    masses = np.array([b.m for b in list_bodies])
    positions = np.array([b.pos for b in list_bodies])
    total_mass = np.sum(masses)
    cm = 1/total_mass *np.sum([masses[i]*positions[i] for i in range(len(list_bodies))],axis=0)
    return cm


class Body:
    def __init__(self,mass,position,velocity):
        self.m = np.array(mass)
        self.pos = np.array(position)
        self.v = np.array(velocity)
        self.pos_history = []
        self.new_pos = None

    def update_velocity(self,acceleration,dt):
        self.v = self.v + acceleration*dt
    
    def update_position(self,dt):
        self.pos_history.append(self.pos)
        self.pos = self.new_pos

    def compution_new_position(self,dt):
        self.new_pos = self.pos + self.v*dt

    def apply_new_position(self):
        self.pos_history.append(self.pos)
        self.pos=self.new_pos        

    def applied_force(self,list_bodies):
        cm = center_of_mass(list_bodies) # Center of Mass of other objects
        mass_others = np.sum([b.m for b in list_bodies]) # Total mass of other objects
        #dist = np.sqrt(np.sum((self.pos*cm)**2)) # Distance between object and Center of Mass
        dist = cm-self.pos 
        return gravitation_newton(self.m,mass_others,dist)

    def get_acceleration(self,list_bodies):
        F = self.applied_force(list_bodies)
        return F/self.m

    def update(self,list_bodies,dt):
        acc = self.get_acceleration(list_bodies)
        self.update_velocity(acc,dt)
        self.compution_new_position(dt)


class Universe:
    def __init__(self,list_bodies):
        self.bodies = list_bodies
        self.n_bodies = len(self.bodies)
    
    def add_body(self,body):
        self.bodies.append(body)
        self.n_bodies = len(self.bodies)

    def update(self,dt):
        ## Compute new positons and update the rest
        for body in self.bodies :
            other_bodies = [o for o in self.bodies if o!= body]
            body.update(other_bodies,dt)

        ## Apply the changes to the positions
        for body in self.bodies : 
            body.apply_new_position()
            
    def update_(self,t,dt):
        '''Update t seconds using dt timestep'''
        for dtt in np.arange(0,t,dt):
            self.update(dtt)

    def total_energy(self):
        pass
    
