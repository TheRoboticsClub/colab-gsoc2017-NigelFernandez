import os
import random

rootdir = os.getcwd()
print rootdir
path = ""
i = 0
file_names = []
for dirpath, dirname, files in os.walk(rootdir):        
    for file_ in files:
        file1 = file_.split("-")        
        file2 = file_.split(".")  
        #print file1
        #print file2
        if (len(file1) == 2):
            depth_files.append(os.path.join(dirpath, file1[0]))
                                                     
                                                            
        '''
            os.system("cp " + os.path.join(dirpath, file_) + " /home/nigel/Documents/Yolod/Data/All/" + str(i).zfill(5) +"_d.png")
        if (file2[1] == "png"):
            os.system("cp " + os.path.join(dirpath, file_) + " /home/nigel/Documents/Yolod/Data/All/" + str(i).zfill(5) +"_rgb.png")
            i += 1            
        '''

print len(file_names)
print file_names[0:20]

i = 0
random.shuffle(file_names)
lim = int(0.8*len(file_names))
print lim
for file_ in file_names[:lim]:
    os.system("cp " + os.path.join(dirpath, file_) + ".png /home/nigel/Documents/Yolod/Data/All/Train/RGB/" + str(i).zfill(5) +"_rgb.png")
    os.system("cp " + os.path.join(dirpath, file_) + "-depth.png /home/nigel/Documents/Yolod/Data/All/Train/Depth/" + str(i).zfill(5) +"_d.png")
    os.system("cp " + os.path.join(dirpath, file_) + ".json /home/nigel/Documents/Yolod/Data/All/Train/Annotations/" + str(i).zfill(5) +".json")
    i+=1
for file_ in file_names[lim:]:
    os.system("cp " + os.path.join(dirpath, file_) + ".png /home/nigel/Documents/Yolod/Data/All/Test/RGB/" + str(i).zfill(5) +"_rgb.png")
    os.system("cp " + os.path.join(dirpath, file_) + "-depth.png /home/nigel/Documents/Yolod/Data/All/Test/Depth/" + str(i).zfill(5) +"_d.png")
    os.system("cp " + os.path.join(dirpath, file_) + ".json /home/nigel/Documents/Yolod/Data/All/Test/Annotations/" + str(i).zfill(5) +".json")
    i+=1    
