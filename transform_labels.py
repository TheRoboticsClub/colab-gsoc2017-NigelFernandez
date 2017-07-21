from bs4 import BeautifulSoup

fr0 = open('file_name_list.txt', 'r')

for line in fr0:
    file_name = line.rstrip()
    fr = open('annotations/' + file_name + '.xml', 'r')    
    fw = open('Labels/' + file_name + '.txt', 'w')
    xml_str = fr.read()
    y = BeautifulSoup(xml_str, 'xml')
    l = y.annotation.findAll("object")
    for el in l:
        fw.write(el.next.next.string + " " + el.bndbox.xmin.string + " " + el.bndbox.ymin.string + " " + el.bndbox.xmax.string + " " + el.bndbox.ymax.string + '\n') 

