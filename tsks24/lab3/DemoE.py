import numpy as np
from scipy import signal, misc
from matplotlib import pyplot as plt
plt.rcParams['image.interpolation'] = 'nearest'

from preamble import *

plt.figure(4)
Im = np.double(plt.imread('baboon.tif'))
plt.subplot(221)
plt.imshow(Im,'gray',clim=(0,255))
plt.title('original image')
plt.colorbar()

b = np.array([0.5,0.5])
b2 = np.convolve(b,b).reshape(1,3)

d = np.array([1,-1.0])
cd = np.convolve(b, d).reshape(1, 3)
sobelx = np.array([[1., 0., -1.], [2., 0., -2.], [1., 0., -1.]]) / 8

Imsobelx = signal.convolve2d(Im,sobelx,'same')
plt.subplot(223)
plt.imshow(Imsobelx,'gray',clim=(-128,127))
plt.title('sobelx image')
plt.colorbar()


Imsobely = signal.convolve2d(Im,sobelx.T,'same')
plt.subplot(224)
plt.imshow(Imsobely,'gray',clim=(-128,127))
plt.title('sobely image')
plt.colorbar()

Imsobel = np.sqrt(Imsobelx**2 + Imsobely**2)
plt.subplot(222)
plt.imshow(Imsobel,'gray',clim=(0,255))
plt.title('magngrad image')
plt.colorbar()


plt.show(block=True)