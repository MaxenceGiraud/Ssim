# Ssim -Scientific Simulations

Collection of personal projects of Math/Physics Simulations and visualisations.


## Contributions
### Author
[Maxence Giraud](https://github.com/MaxenceGiraud/)

## Requirements 

For Python code :

* [SciPy](https://www.scipy.org/)
* [NumPy](https://numpy.org/)
* [Matplotlib](https://matplotlib.org/) 
* Some other specific requirements may be specified in the project own readme.

For C++ code : 

*upcoming*


*N.B. :* Some readme have written LaTeX, you can view them locally with some capable reader (e.g. VSCode) or using extensions.

## List of simulations

### Physics
#### Classical
- [x] [N body Simulations](./ssim/psim/Classical/NBody/)
- [x] [Projectile motion](./ssim/psim/Classical/ProjectileMotion/)
- [x] [N Linked Pendulum](./ssim/psim/Classical/LinkedPendulum/) 
- [x] [N Springed Pendulum system](./ssim/psim/Classical/SpringedPendulum/)
- [ ] N Coupled Pendulum
- [ ] N Coupled Mass
- [ ] Foucault pendulum
  
#### Waves
- [x] [Waves interferences](./ssim/psim/Wave/WaveInterference) (And Double Split experiment using classical waves) at fixed time
- [ ] [Wave simulation](./ssim/psim/Waves/../Wave/wsim/)


#### E&M
- [x] [Electric Field Visualization](./ssim/psim/EM/ElectricField/)
- [x] [Magnetic Field Visualization](./ssim/psim/EM/MagneticField/)


#### Quantum 
- [x] [Eigenstates solver (1D & 2D)](./ssim/psim/Quantum/EigenstatesSolver/)
- [x] [Hydrogen atom orbitals plot](./ssim/psim/Quantum/Hydrogen/)
- [ ] Helium orbitals (using [Hartree-Fock method](https://en.wikipedia.org/wiki/Hartree%E2%80%93Fock_method))
- [ ] Quantum Double Split

#### General Relativity 
- [ ] [Black hole Visualization](./ssim/psim/GR/BlackHole/)
- [ ] Spacetime behavior arround massive object (see scienceclick video on youtube on GR visualisation for the goal of this visualization)
  
#### Cosmology 
- [x] [Galaxy visualization / simulation / collisions](./ssim/psim/Cosmology/Galaxy/)
    
#### Stellar Physics 
- [ ] Life of a star (fusion of elements, death ... What is possible ??)

#### Fluid Mechanics   
- [ ] Some Fluids flows (<https://www.youtube.com/watch?v=cvl0gUvofZk>)
- [ ] Simulate fluid flow with interaction with the env (example of 2D/3D airplane wing, boat hull ...)


### Mathematics

- [x] *[Game of Life](https://github.com/MaxenceGiraud/GameOfLife) (Available in another repo)*
- [ ] Visual of analytic continuation of a function (see 3b1b video on Riemann hypothesis)


#### Fractals   
- [x] [Julia/Fatou set](./ssim/msim/JuliaSet/)
- [x] [Koch Snowflakes](./ssim/msim/KochSnowflake/)
- [x] [Sierpiński triangle/carpet/sponge](./ssim/msim/Sierpinski/)
- [ ] Tetration fractals

#### Chaotic Maps

- [x] [Lorenz system](./ssim/msim/LorenzSystem/)
- [ ] Logistic Map Bifurcation diagram
- [ ] Poincaré map (e.g. Duffing eq)
- [ ] Exponential map
- [x] [Bogdanov map](./ssim/msim/BogdanovMap/)
- [ ] Others from [List of chaotic maps](https://en.wikipedia.org/wiki/List_of_chaotic_maps)

## Main References
*(some other references may be included in the projects own readme files)*

[1] R. TAYLOR, John. [Classical Mechanics.](https://www.uscibooks.com/taylor2.htm) University Science Books, 2005.   
[2] SHANKAR, R.. [Principles of Quantum Mechanics](https://www.springer.com/gp/book/9780306447907). Springer US, 2011.    
[3] J. GRIFFITHS, David y F. SCHROETER,  Darrell. [Introduction to Quantum Mechanics](https://www.cambridge.org/core/books/introduction-to-quantum-mechanics/990799CA07A83FC5312402AF6860311E). Cambridge University Press, 2018.   
[4] J. GRIFFITHS, David. Introduction to Electrodynamics. Pearson Education Limited, 2013.

[//]: # (    
[?] CARROLL, Sean. Spacetime and Geometry: An Introduction to General Relativity. Pearson, 2003.) 