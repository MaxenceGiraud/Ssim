# Hydrogen simulation using Quantum Mechanics

## Usage 
```python
from quantumhydrogen import plot_hydrogen_orbitals

## Quantum numbers
n=3
l=2
m=0

# 1D plot (Radial wavefunction)
plot_hydrogen_orbitals(n,l,m,posy=None)

# 2D plot
plot_hydrogen_orbitals(n,l,m)

# 3d plot (UPCOMING)
plot_hydrogen_orbitals(n,l,m,posz=(-12,12))

```
## Hydrogen Wave Function Equations
### Hydrogen Wavefunction

The hydrogen wavefunction equals to : 

$$\psi_{n \ell m}(r, \theta, \phi)=R_{n \ell}(r) Y_{\ell}^{m}(\theta, \phi)$$

With n,l,m the first 3 [quantum numbers](https://en.wikipedia.org/wiki/Quantum_number), $R_{n \ell}$ the radial wavefunction and $Y_{\ell}^{m}$ the angular wavefunction.

### Angular wavefunction / Spherical Harmonics
The regularized angular wavefunction (called spherical harmonics) equals to : 
$$Y_{\ell}^{m}(\theta, \phi)=\sqrt{\frac{(2 \ell+1)}{4 \pi} \frac{(\ell-m) !}{(\ell+m) !}} e^{i m \phi} P_{\ell}^{m}(\cos \theta)$$

Where $P_{\ell}^{m}$ is an [associated Legendre polynomial](https://en.wikipedia.org/wiki/Associated_Legendre_polynomials), defined by the diffential equation :

$$ {\frac {d}{dx}}\left[(1-x^{2}){\frac {d}{dx}}P_{\ell }^{m}(x)\right]+\left[\ell (\ell +1)-{\frac {m^{2}}{1-x^{2}}}\right]P_{\ell }^{m}(x)=0$$

### Radial Wavefunction

The Radial wavefunction equals to :

$$  R_{n \ell}(r) = \sqrt{\left(\frac{2}{n a}\right)^{3} \frac{(n-\ell-1) !}{2 n(n+\ell) !}} e^{-r / n a}\left(\frac{2 r}{n a}\right)^{\ell}\left[L_{n-\ell-1}^{2 \ell+1}(2 r / n a)\right] $$

Where $L_{n}^{\alpha}$ is an [associated Laguerre polynomial](https://en.wikipedia.org/wiki/Laguerre_polynomials), defined to be the solutions to the differential equations :

$$ x\,y'' + (\alpha +1 - x)\,y' + n\,y = 0 $$


## TODO
- [x] Compute wavefunction of hydrogen
- [x] Plot orbitals
- [ ] Compute laguerre and legendre polynomials without scipy.
- [ ] Add possibility to fully either compute using scipy or only personnalized functions.
- [ ] Plot 3D orbitals
  
## Some external references

- <https://kforinas.pages.iu.edu/physlets/quantum/hydrogen.html>
