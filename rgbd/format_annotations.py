import cv2
import numpy as np
import json

folders = ['Train', 'Test']
lim = [(0, 256), (256, 321)]
for j in range(len(folders)):
    folder = folders[j]
    for i in range(lim[j][0], lim[j][1]):
        name = folder + "/Depth/" + str(i).zfill(5) + "_d.png"
        img = cv2.imread(name)
        width = img.shape[1]
        height = img.shape[0]
        #print width, height
        f = open(folder + "/Annotations/" + str(i).zfill(5) + ".json", 'r')
        data = json.load(f)
        #print data
        f1 = open(folder + "/AnnotationsFormatted/yolod_map_morton/" + str(i).zfill(5) + "_cmap.txt", 'w')

        '''
        Annotation format for darknet:
        <object-class> - integer number of object from 0 to (classes-1)
        <x> <y> <width> <height> - float values relative to width and height of image, it can be equal from 0.0 to 1.0
        for example: <x> = <absolute_x> / <image_width> or <height> = <absolute_height> / <image_height>
        atention: <x> <y> - are center of rectangle (are not top-left corner)
        '''
        
        for el in data:
            x = el['x']
            y = el['y']
            w = el['w']
            h = el['h']
            x_centre = x + float(w)/2
            y_centre = y + float(h)/2
            rel_x = float(x_centre) / width
            rel_y = float(y_centre) / height
            rel_w = float(w) / width
            rel_h = float(h) / height
            f1.write("0 " + str(rel_x) + " " + str(rel_y) + " " + str(rel_w) + " " + str(rel_h) + "\n")
        
        f.close()
        f1.close()
