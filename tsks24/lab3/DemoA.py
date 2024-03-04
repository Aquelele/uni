import numpy as np
from scipy import signal, misc
from matplotlib import pyplot as plt
plt.rcParams['image.interpolation'] = 'nearest'


from preamble import *
Im = np.double(plt.imread('baboon.tif'))
plt.figure(1)
plt.subplot(121)
plt.imshow(Im,'gray',clim=(0,255))
plt.title('original image')
plt.colorbar()

plt.subplot(122)
plt.imshow(Im,'gray',clim=(50,200))
plt.title('contrast image')
plt.colorbar()

plt.show(block=True)
print(Im)
print(np.min(Im))
print(np.max(Im))
print(np.min(Im,0))        # min value of dimention 0