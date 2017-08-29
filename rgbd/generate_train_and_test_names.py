f = open('train_yolod_map_morton.txt', 'w')

for i in range(256):
    f.write("data/custom/yolod_map_morton/" + str(i).zfill(5) + "_cmap.png" + "\n")
f.close()

'''
f = open('train_custom_depth.txt', 'w')

for i in range(256):
    f.write("data/custom/depth/" + str(i).zfill(5) + "_d.png" + "\n")
f.close()
'''

f = open('test_yolod_map_morton.txt', 'w')
for i in range(256, 320):
    f.write("data/custom/yolod_map_morton/" + str(i).zfill(5) + "_cmap.png" + "\n")
f.close()

'''
f = open('test_custom_depth.txt', 'w')
for i in range(256, 320):
    f.write("data/custom/depth/" + str(i).zfill(5) + "_d.png" + "\n")
f.close()
'''
