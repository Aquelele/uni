import numpy as np
from scipy import signal, misc
from matplotlib import pyplot as plt
plt.rcParams['image.interpolation'] = 'nearest'

from preamble import *
Im = np.load('pattern.npy')
plt.figure(9)
plt.subplot(221)
plt.imshow(Im,'gray',clim=(-1,1))
plt.title('original pattern')

Im2 = Im[::2, ::2]
plt.subplot(222)
plt.imshow(Im2,'gray',clim=(-1,1))
plt.title('downsampled pattern')

b = np.array([0.5,0.5])
b2 = np.convolve(b,b).reshape(1,3)
aver = signal.convolve2d(b2,b2.T)

Imaver = signal.convolve2d(Im, aver,'same')
Imaver = signal.convolve2d(Imaver, aver,'same')
Imaver = signal.convolve2d(Imaver, aver,'same')
plt.subplot(223)
plt.imshow(Imaver,'gray',clim=(-1,1))
plt.title('LP-filtered image')

Imaver2 = Imaver[::2, ::2]
plt.subplot(224)
plt.imshow(Imaver2,'gray',clim=(-1,1))
plt.title('downsampled LP-filtered image')



plt.show(block=True)