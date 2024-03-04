import numpy as np
from scipy import signal, misc
from matplotlib import pyplot as plt
plt.rcParams['image.interpolation'] = 'nearest'


from preamble import *

b = np.array([0.5,0.5])
b2 = np.convolve(b,b).reshape(1,3)
aver = signal.convolve2d(b2,b2.T)





plt.figure(3)
Im = np.double(plt.imread('baboon.tif'))
plt.subplot(121)
plt.imshow(Im,'gray',clim=(0,255))
plt.title('original image')
plt.colorbar()

Imaver = signal.convolve2d(Im, aver,'same')
plt.subplot(122)
plt.imshow(Imaver,'gray',clim=(0,255))
plt.title('1x image')
plt.colorbar()

plt.show(block=False)
#help(signal.convolve2d)

aver *= 1.1

Imaver1 = signal.convolve2d(Im, aver,'same')
Imaver2 = signal.convolve2d(Imaver1, aver,'same')
Imaver3 = signal.convolve2d(Imaver2, aver,'same')

plt.figure(4)
plt.subplot(121)
plt.imshow(Im,'gray',clim=(0,255))
plt.title('original image')
plt.colorbar()

plt.subplot(122)
plt.imshow(Imaver3,'gray',clim=(0,255))
plt.title('3x image')
plt.colorbar()
plt.show(block=True)