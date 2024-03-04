import numpy as np
from scipy import signal, misc, ndimage
import cv2
from matplotlib import pyplot as plt
plt.rcParams['image.interpolation'] = 'nearest'
import jpeglab as jl

im1_bgr = cv2.imread('image1.png')

im1 = cv2.cvtColor(im1_bgr, cv2.COLOR_BGR2RGB)
plt.figure(0)
plt.imshow(im1)
plt.title('im1')
plt.show(block=False)

im1r = im1[:,:,0]
im1g = im1[:,:,1]
im1b = im1[:,:,2]

plt.figure(1)
plt.imshow(im1r,'gray')
plt.title('im1r')

plt.figure(2)
plt.imshow(im1g,'gray')
plt.title('im1g')

plt.figure(3)
plt.imshow(im1b,'gray')
plt.title('im1b')
plt.show(block=False)


y, cb, cr = jl.rgb2ycbcr(im1)

plt.figure(4)
plt.imshow(y,'gray', clim=(0, 255))
plt.title('y')

plt.figure(5)
plt.imshow(cb,'gray', clim=(0, 255))
plt.title('cb')

plt.figure(6)
plt.imshow(cr,'gray', clim=(0, 255))
plt.title('cr')

plt.show(block=False)


plt.figure(7)
plt.imshow(y, 'gray', clim=(0, 255))
plt.title('y')
X = 2**3 # 8
y2 = X*np.floor_divide(y,X)
plt.figure(8)
plt.imshow(y2, 'gray', clim=(0, 255))
plt.title('y2')
plt.show(block=True)
