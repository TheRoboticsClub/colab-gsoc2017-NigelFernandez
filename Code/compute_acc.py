import json
from operator import itemgetter
from finding_iou import find_iou
    
fr0 = open('file_name_list.txt', 'r')
fw = open('accuracy_stats.txt', 'w')

fw.write('file_name' + ' ' + 'total_pred' + ' ' + 'correct' + ' ' + 'incorrect' + ' ' + 'total_truth' + ' ' + 'missed' + '\n')
for line in fr0:
    file_name = line.rstrip()
    fr1 = open('Labels/' + file_name + '.txt', 'r')
    fr2 = open('Pictures/out/' + file_name + '.json', 'r')
    pred = json.load(fr2)
    pred_objs = []
    for el in pred:
        pred_objs.append([el['label'], int(el['topleft']['x']), int(el['topleft']['y']), int(el['bottomright']['x']), int(el['bottomright']['y']), int(el['confidence'])])   
    print (pred_objs)
    truth_objs = []  
    for line in fr1:
        line = line.rstrip().split(' ')
        vals = line[1:]
        vals = [int(val) for val in vals]
        truth_objs.append([line[0]] + vals)
        
    print (truth_objs)
    pred_objs.sort(key=lambda x: x[5], reverse=True)
    print (pred_objs)

    total_pred = len(pred_objs)
    total_truth = len(truth_objs)
    incorrect = 0
    correct = 0
    missed = 0
    for pred_obj in pred_objs:
        #store all objects in truth_objs having same name as pred_obj in objs
        objs = []
        for truth_obj in truth_objs:
            if (truth_obj[0] == pred_obj[0]):
                objs.append(truth_obj)
        if (len(objs) == 0):
            incorrect += 1
            continue
        iou_list = []
        for obj in objs:
            iou_list.append([obj, find_iou(pred_obj[1], pred_obj[2], pred_obj[3], pred_obj[4], obj[1], obj[2], obj[3], obj[4])])
        iou_list.sort(key = lambda x : x[1], reverse=True)
        print (iou_list)
        if (iou_list[0][1] > 0.5):
            correct += 1
            truth_objs.remove(iou_list[0][0])
        else:
            incorrect += 1
    missed += len(truth_objs)

    fw.write(file_name + ' ' + str(total_pred) + ' ' + str(correct) + ' ' + str(incorrect) + ' ' + str(total_truth) + ' ' + str(missed) + '\n')
    
#sorted_obj = sorted(obj_pred.items(), key=operator.itemgetter(1))    
