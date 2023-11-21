import numpy as np

# Python 'range' only supports integer values
r = range(-10, 11, 2)

# The Numpy library provides 'arange' which allows float values
r = np.arange(-10, 11, 0.5)
for _ in r:
    print( _, end=', ' )
