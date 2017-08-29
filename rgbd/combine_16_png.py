import cv2
import numpy as np
import sys

img1 = cv2.imread("00034_rgb.png")
img2 = cv2.imread("00034_d.png")

print img1.dtype
print img1[100, 100]
print img2[100, 100]

#format (R-D1, G-D2, B-D3)

img3 = np.zeros((img1.shape[0], img2.shape[1], 3), np.uint16)
for i in range(img1.shape[0]):
    for j in range(img2.shape[1]):
        for k in range(3):        
            first = np.uint16(img1[i,j][k])
            second = np.uint16(img2[i,j][k])
            both = np.uint16(first << 8)            
            #print second
            #print both
            both = both | second        
            img3[i,j][k] = both
            #print img3[i,j][k]
            #sys.exit(0)


#print img3[100, 100]
cv2.imwrite("00034_com.png", img3)       

#-1 corresponds to load image as is
img4 = cv2.imread("00034_com.png", -1)
print img4.dtype
print img4[100, 100]

