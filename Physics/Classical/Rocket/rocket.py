import numpy as np
from .NBody import gravitation_newton,acc

class Rocket:
    def __init__(self,mass_empty,specific_impulse,fuel_capacity,fuel_density,fuel_rate):
        self.specific_impulse = specific_impulse # seconds
        self.fuel = fuel_capacity # In Kg
        #self.fuel_capacity = fuel_capacity
        #self.fuel_density = fuel_density
        self.fuel_rate = fuel_rate # In Kg/s
        self.mass_empty = mass_empty # In Kg
        self.mass_full = self.mass_empty + self.fuel # In Kg

        self.v = 0 # m/s
        self.pos = 0 # Height in m

    @property
    def mass(self):
         # Forbid mass to be lower than rocket with no fuel
        return max(self.mass_empty,self.mass_empty + self.fuel)


    def delta_v(self,g=9.81):
        return self.specific_impulse*g * np.log(self.mass_empty/self.mass_full)

    def get_acc(self,planet,dt):
        f = self.get_force(planet,dt)
        return f/self.mass

    def update_position(self,dt):
        self.pos = self.pos + self.v*dt
        if self.pos < 0 : # Collision with planet
            self.pos = 0
        
    def update_velocity(self,acc,dt):
        self.v = self.v + acc*dt

    def update_fuel(self,dt):
        self.fuel = max(self.fuel - self.fuel_rate*dt,0) # Forbid negative fuel

    def get_force(self,planet,dt):
        f_planet = -gravitation_newton(planet.mass,self.mass,self.pos+planet.radius)
        thrust = self.fuel_rate*dt * self.specific_impulse  # TODO check thrust equation

        return f_planet + thrust

class Planet:
    def __init__(self,mass,radius):
        self.mass = mass # In kg
        self.radius = radius # In m


def simulate_rocket_launch(rocket,planet,t,dt=0.1):
    pass