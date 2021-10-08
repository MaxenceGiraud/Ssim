# N-Body Simulation

N-Body Simulation using Newton's Laws


https://user-images.githubusercontent.com/24920752/115122080-913c4b00-9fa5-11eb-806d-71617ab46a85.mp4

## How to use 

```python
# Generate points
pos,mass,vel = generate_initial_conditions(N=50)

pos_h = n_body(pos,mass,vel,animate=True) # Perform simulation


# Create 3D animation
create_3D_animation(pos_h)
```

## TODO

- [x] Implement 2-Body sim
- [x] Support for N bodies
- [x] Support for any number of dimensions
- [x] Optimize Computations (vectorize)
- [x] Create 2D animation
- [x] Create 3D animation 
