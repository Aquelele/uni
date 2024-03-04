import numpy as np
from scipy import signal, misc
from matplotlib import pyplot as plt
plt.rcParams['image.interpolation'] = 'nearest'


from preamble import *
Im = np.load('pirat2.npy')
IM = np.fft.fftshift(np.fft.fft2(np.fft.ifftshift(Im)))
plt.figure(10)
plt.subplot(221), plt.imshow(np.abs(IM),'gray'), plt.colorbar()
plt.subplot(222), plt.imshow(np.angle(IM),'gray'), plt.colorbar()
plt.subplot(223), plt.imshow(np.real(IM),'gray'), plt.colorbar()
plt.subplot(224), plt.imshow(np.imag(IM),'gray'), plt.colorbar()

plt.show(block=False)


maxV = -0.1 * np.min(np.real(IM))

plt.figure(11)
plt.subplot(221)
plt.imshow(np.abs(IM),'gray', clim=(0, maxV))
plt.title('abs image')
plt.colorbar()

plt.subplot(222)
Imangle = np.angle(IM)
Imangle[np.abs(IM) < 10*np.mean(np.abs(IM))] = 0
plt.imshow(Imangle,'gray')
plt.title('angle image')
plt.colorbar()

plt.subplot(223)
plt.imshow(np.real(IM),'gray', clim=(-maxV, maxV))
plt.title('real image')
plt.colorbar()

plt.subplot(224)
plt.imshow(np.imag(IM),'gray', clim=(-maxV, maxV))
plt.title('imag image')
plt.colorbar()

plt.show(block=True)