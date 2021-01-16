# Lorenz system

## Usage 
Simply call the function with the parameters of the system you want : 
```python
plot_lorenz_system(rho= 28,sigma= 10,beta= 8/3)
```
![Lorenz](./img/lorenz.png)

## Explanation

The Lorenz system is the following system of ordinary differential equations :

$$\frac{\mathrm {d} x}{\mathrm {d} t}=\sigma (y-x)\\
{\frac {\mathrm {d} y}{\mathrm {d} t}}=x(\rho -z)-y\\
{\frac {\mathrm {d} z}{\mathrm {d} t}}=xy-\beta z$$