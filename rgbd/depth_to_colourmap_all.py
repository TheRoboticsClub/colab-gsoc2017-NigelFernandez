import cv2
import numpy as np

def rescale(x):
    #rescale from 0-10000 to 0-255
    return np.uint8(255 * float(x) / 10000)
    
    
folders = ['Train', 'Test']
lim = [(0, 256), (256, 321)]
for j1 in range(len(folders)):
    folder = folders[j1]
    for i1 in range(lim[j1][0], lim[j1][1]):
        name1 = folder + "/Depth/" + str(i1).zfill(5) + "_d.png"
        img1 = cv2.imread(name1)
        img2 = np.zeros((img1.shape[0], img1.shape[1], 1), np.uint8)
        for i in range(img1.shape[0]):
            for j in range(img1.shape[1]):       
                    first = np.uint16(img1[i,j][1])
                    second = np.uint16(img1[i,j][2])
                    both = np.uint16(first << 8 | second )            
                    both = rescale(both)       
                    img2[i,j] = both        
        name2 = folder + "/GrayDepth/" + str(i1).zfill(5) + "_gd.png"              
        cv2.imwrite(name2, img2) 
        img3 = cv2.applyColorMap(img2, cv2.COLORMAP_JET)  
        name3 = folder + "/ColourMap/" + str(i1).zfill(5) + "_cmap.png"              
        cv2.imwrite(name3, img3) 
        print i1  
