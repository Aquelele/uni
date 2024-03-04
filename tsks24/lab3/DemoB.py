import numpy as np
from scipy import signal, misc
from matplotlib import pyplot as plt
plt.rcParams['image.interpolation'] = 'nearest'


from preamble import *


graycmap = plt.get_cmap('gray',256)
gray_vals = graycmap(np.arange(256))
gray_vals[200:] = [0, 0, 1, 1] # Blue
gray_vals[:50] = [0, 1, 0, 1] # Green
plt.colormaps.register(graycmap.from_list('bggray', gray_vals))


Im = np.double(plt.imread('baboon.tif'))
plt.figure(2)
plt.subplot(121)
plt.imshow(Im,'bggray', clim=(0,255))
plt.title('original image')
plt.colorbar()

plt.subplot(122)
plt.imshow(Im,'jet', clim=(0,255))
plt.title('jet image')
plt.colorbar()

plt.show(block=True)


"""gray_vals[200:] = [1, 0, 0, 1]
print(gray_vals[150:])

plt.colormaps.register(graycmap.from_list('modgray', gray_vals))
plt.show('modgray')
print()"""