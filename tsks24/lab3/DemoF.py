import numpy as np
from scipy import signal, misc
from matplotlib import pyplot as plt
plt.rcParams['image.interpolation'] = 'nearest'

from preamble import *

Im = np.double(plt.imread('circle.tif'))


b = np.array([0.5,0.5])
b2 = np.convolve(b,b).reshape(1,3)

d = np.array([1,-1.0])
cd = np.convolve(b, d).reshape(1, 3)
sobelx = np.array([[1., 0., -1.], [2., 0., -2.], [1., 0., -1.]]) / 8
sobely = sobelx.T

Imsobelx = signal.convolve2d(Im,sobelx,'same')
Imsobely = signal.convolve2d(Im,sobely,'same')

mangngrad_sobel = np.sqrt(Imsobelx**2 + Imsobely**2)

plt.figure(4)
plt.subplot(221)
plt.imshow(mangngrad_sobel,'gray',clim=(0, 155))
plt.title('magngrad sobel')
plt.colorbar()

plt.subplot(223)
plt.imshow(mangngrad_sobel,'gray',clim=(90, 160))
plt.title('magngrad sobel')
plt.colorbar()

Imcdx = signal.convolve2d(Im, cd, 'same')
Imcdy = signal.convolve2d(Im, cd.T, 'same')

mangngrad_cd = np.sqrt(Imcdx**2 + Imcdy**2)


plt.subplot(222)
plt.imshow(mangngrad_cd,'gray',clim=(0, 155))
plt.title('magngrad centraldiff')
plt.colorbar()


Imsobely = signal.convolve2d(Im,sobelx.T,'same')
plt.subplot(224)
plt.imshow(mangngrad_cd,'gray',clim=(90, 160))
plt.title('magngrad centraldiff')
plt.colorbar()



plt.show(block=True)