import numpy as np
from scipy import signal, misc
from matplotlib import pyplot as plt
plt.rcParams['image.interpolation'] = 'nearest'

Im = np.load('pirat.npy')

laplace = np.array([[0., 1., 0.], [1., -4., 1.], [0., 1., 0.]])

plt.figure(2)
plt.subplot(121)
plt.imshow(Im,'gray',clim=(0,255))
plt.title('original image')
plt.colorbar()

Imlaplace = signal.convolve2d(Im,laplace,'same')
plt.subplot(122)
plt.imshow(Imlaplace,'gray',clim=(-100,100))
plt.title('laplace image')
plt.colorbar()

plt.show(block=False)

ImHP = - Imlaplace

ImSharp = Im + ImHP
ImSharp2 = Im + 2 * ImHP

plt.figure(3)
plt.subplot(121)
plt.imshow(ImSharp,'gray',clim=(0,255))
plt.title('sharp image')
plt.colorbar()

plt.subplot(122)
plt.imshow(ImSharp2,'gray',clim=(0,255))
plt.title('sharper image')
plt.colorbar()

plt.show(block=True)


