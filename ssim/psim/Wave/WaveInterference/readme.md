# Waves interferences experiment 

Simulate N sources of waves and how they interfere with each other.
This can be used to recreate the Double slit experiment, and does by default (the 2 sources are considered to be the 2 holes)


## Usage 

### Double Slit experiment
```python3
from waveinterference import waves_interferences,Source

source1 = Source((0,0.5),4)
source2 = Source((0,-0.5),4)
waves_interferences([source1,source2],precision=150)
```
![double_slit](./.img/double_slit.svg)

### Using more than 2 sources

```python3
source3 = Source((-2,-1),intensity=8)
w=waves_interferences([source1,source2,source3],precision=400,posy=(-10,10),posx=(-10,10))
```
![3sources](./.img/3sources.svg)


## TODO
- [x] Implement double slit experiment
- [x] Extend to n sources
- [ ] Add possibility of wave blocking object