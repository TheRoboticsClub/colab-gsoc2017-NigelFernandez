import cv2
import numpy as np
import json 

img = cv2.imread("00034_rgb.png")
width = img.shape[0]
height = img.shape[1]
f = open("00034.json", "r")
data = json.load(f)

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
    print("0 " + str(rel_x) + " " + str(rel_y) + " " + str(rel_w) + " " + str(rel_h) + "\n")
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
    cv2.imshow('image',img)
    cv2.waitKey(0)
