import cv2
import numpy as np
import sys

img1 = cv2.imread("00034_d.png")
img2 = np.zeros((img1.shape[0], img1.shape[1], 1), np.uint8)

def rescale(x):
    #rescale from 0-10000 to 0-255
    return np.uint8(255 * float(x) / 10000)

for i in range(img1.shape[0]):
    for j in range(img1.shape[1]):       
            first = np.uint16(img1[i,j][1])
            second = np.uint16(img1[i,j][2])
            both = np.uint16(first << 8 | second )            
            both = rescale(both)       
            img2[i,j] = both
            #print img3[i,j][k]
            #sys.exit(0)

cv2.imwrite("gray.png", img2)   
img3 = cv2.applyColorMap(img2, cv2.COLORMAP_JET)         
cv2.imwrite("jet.png", img3) 

print img3.shape
