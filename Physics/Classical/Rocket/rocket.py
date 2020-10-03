import numpy as np
from ..NBody.NBody import gravitation_newton,acc,Body


class Stage:
    def __init__(self,empty_mass,fuel,thrust,specific_impulse):
        self.empty_mass = empty_mass
        self.fuel = fuel
        self.thrust = thrust
        self.specific_impulse = specific_impulse

        self.fuel_rate = 0

    @property
    def mass(self):
        return self.empty_mass + self.fuel

    def update_fuel(self,dt):
        self.fuel = max(self.fuel - self.fuel_rate*dt,0)

        if self.fuel == 0: # False if not more fuel in the stage
            return False
        else : 
            return True

class Rocket(Body):
    def __init__(self,name,mass,position,velocity,stages,direction,plan):
        assert (np.sqrt(np.sum(np.array(direction)**2)) >= 0.999) and  (np.sqrt(np.sum(np.array(direction)**2)) <= 1.001), "Direction vector should have magnitude 1"

        self.name
        self.stages = stages # List of stages, the first one being the one at the bottom of the rocket
        self.direction = direction # direction of the rocket (vector with magnitude 1)
        self.plan = plan # TODO determine plan structure (list of direction/ lambda function ??)

        self.mass_empty = mass
        self.pos = position
        self.velovity = velocity
    
    @property
    def mass(self):
        mass_stages = np.sum([stage.mass for stage in self.stages]) # Combined mass of all stages
        return  mass_stages + self.mass_empty

    def get_acceleration(self,list_bodies):
        f_other_objects = self.applied_force(list_bodies)

        # TODO Compute thrust of current stage
        # TODO if stage fuel empty, detach stage
        # TODO update fuel

        if len(self.stages) != 0 :
            thrust = self.stages[0]
        else :
            thrust = 0

        f = f_other_objects + thrust
        return f

    def delta_v(self,g=9.81):
        return np.sum([stage.specific_impulse for stage in self.stages])*g * np.log(self.mass_empty/self.mass)


class Planet(Body):
    def __init__(self,name,mass,position,velocity,radius):
        self.name = name
        self.mass = mass
        self.radius = radius
        
        self.pos = position
        self.velocity = velocity
