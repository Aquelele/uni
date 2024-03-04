import numpy as np
from scipy import signal, misc
from matplotlib import pyplot as plt
plt.rcParams['image.interpolation'] = 'nearest'

Im = np.double(plt.imread('circle.tif'))


laplace = np.array([[0., 1., 0.], [1., -4., 1.], [0., 1., 0.]])

plt.figure(2)
plt.subplot(121)
plt.imshow(Im,'gray',clim=(0,255))
plt.title('original image')
plt.colorbar()

Imlaplace = signal.convolve2d(Im,laplace,'same')
plt.subplot(122)
plt.imshow(Imlaplace,'gray',clim=(-128,127))
plt.title('laplace image')
plt.colorbar()

plt.show(block=True)