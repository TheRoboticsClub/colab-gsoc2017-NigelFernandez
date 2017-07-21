import os

fr = open('val.txt', 'r')
fw = open('file_name_list.txt', 'w')

file_names = []
for line in fr:
    file_names.append(line.rstrip())

for name in file_names[0:50]:
    os.system('cp VOCdevkit_trainval/VOC2012/JPEGImages/' + name + '.jpg' + ' ./Pictures/')
    os.system('cp VOCdevkit_trainval/VOC2012/Annotations/' + name + '.xml' + ' ./Annotations/') 
    fw.write(name + '\n')
