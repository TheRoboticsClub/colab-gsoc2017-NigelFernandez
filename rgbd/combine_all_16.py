import cv2
import numpy as np


folders = ['Train', 'Test']
lim = [(0, 256), (256, 321)]
for j1 in range(len(folders)):
    folder = folders[j1]
    for i1 in range(lim[j1][0], lim[j1][1]):
        name1 = folder + "/Depth/" + str(i1).zfill(5) + "_d.png"
        name2 = folder + "/RGB/" + str(i1).zfill(5) + "_rgb.png"
        img1 = cv2.imread(name1)
        img2 = cv2.imread(name2)
        img3 = np.zeros((img1.shape[0], img2.shape[1], 3), np.uint16)
        for i in range(img1.shape[0]):
            for j in range(img2.shape[1]):
                for k in range(3):        
                    first = np.uint16(img1[i,j][k])
                    second = np.uint16(img2[i,j][k])
                    both = np.uint16(first << 8)            
                    both = both | second        
                    img3[i,j][k] = both
        name3 = folder + "/Combine16/" + str(i1).zfill(5) + "_c16.png"
        print i1
        cv2.imwrite(name3, img3)
