import cv2
import numpy as np

#source: http://code.activestate.com/recipes/577558-interleave-bits-aka-morton-ize-aka-z-order-curve/
def part1by1(n):
        n&= 0x0000ffff
        n = (n | (n << 8)) & 0x00FF00FF
        n = (n | (n << 4)) & 0x0F0F0F0F
        n = (n | (n << 2)) & 0x33333333
        n = (n | (n << 1)) & 0x55555555
        return n


def unpart1by1(n):
        n&= 0x55555555
        n = (n ^ (n >> 1)) & 0x33333333
        n = (n ^ (n >> 2)) & 0x0f0f0f0f
        n = (n ^ (n >> 4)) & 0x00ff00ff
        n = (n ^ (n >> 8)) & 0x0000ffff
        return n


def interleave2(x, y):
        return part1by1(x) | (part1by1(y) << 1)


def deinterleave2(n):
        return unpart1by1(n), unpart1by1(n >> 1)


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
                    first = np.uint8(img1[i,j][k])
                    second = np.uint8(img2[i,j][k])
                    img3[i,j][k] = np.uint16(interleave2(first, second))
        name3 = folder + "/Combine16Morton/" + str(i1).zfill(5) + "_m16.png"
        print i1
        cv2.imwrite(name3, img3)
