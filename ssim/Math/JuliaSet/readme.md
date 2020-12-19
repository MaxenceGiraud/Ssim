# Julia Set

Compute the Julia set.

## Usage

```python
from julia_set import juliaset

# Mandelbrot set
mandel = juliaset(c=0,init_with_constant=True,display=True)

# Other julia set
j = juliaset(c=0.1-0.21j,display=True)
```
You can find further examples in the notebook [julia.ipynb](./julia.ipynb)

## Details 

*(upcoming)*


## TODO

- [x] Implement Julia set
- [x] Add option for Mandelbrot
- [x] Add the possibility to have custom functions
- [ ] Optimize Computations
- [ ] Add possibility for quaternions and visualisation of it

## Some external links

- <https://en.wikipedia.org/wiki/Julia_set>
- <https://en.wikipedia.org/wiki/Newton_fractal>
- <https://en.wikibooks.org/wiki/Pictures_of_Julia_and_Mandelbrot_sets>
- <http://www.hiddendimension.com/FractalMath/Convergent_Fractals_Main.html>