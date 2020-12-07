# N-Body Simulation

N-Body Simulation using Newton's Laws

NB : Supports only 2D systems as of now

## How to use

```python
from Nbody import Body,Universe

# Create the Bodies objects
BodyA = Body(name='BodyA',mass=100,position=[0,0],velocity=[2,0])
BodyB = Body(name='BodyB',mass=100,position=[0,1000],velocity=[2,0])

# Create the Universe containing the bodies
U = Universe([BodyA,BodyB])

# Do the Simulation for 1000s with 0.1s intervals
U.update(1000,0.1)
```

## TODO

- [x] Implement 2-Body sim
- [x] Support for N bodies
- [x] Support for any number of dimensions
- [x] Optimize Computations (vectorized version in another subproject [here](../../Cosmology/Galaxy/simulate_nbody.py) in a non-OOP way).
- [ ] Solve using Lagrangian mechanics (section 8 Taylor)