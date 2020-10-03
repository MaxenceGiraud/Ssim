import numpy as np
from ..NBody.NBody import gravitation_newton,acc,Body


class Stage:
    def __init__(self,empty_mass,fuel_mass,thrust,specific_impulse):
        self.empty_mass = empty_mass
        self.fuel_mass = fuel_mass
        self.thrust = thrust
        self.specific_impulse = specific_impulse

class Rocket(Body):
    def __init__(self,stages,direction,plan):
        self.stages = stages # List of stages, the first one being the one at the bottom of the rocket
        self.direction = direction # direction of the rocket
        self.plan = plan


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