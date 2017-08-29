import cv2
import numpy as np
from libtiff import TIFF

img1 = cv2.imread("00034_rgb.png")
img2 = cv2.imread("00034_d.png")

img3 = np.concatenate((img1, img2), axis=2)

print img1.shape
print img2.shape
print img3.shape

#cv2.imwrite("c3_image.tiff", img)
tif = TIFF.open('c6_img.tiff', mode='w')
tif.write_image(img3)
