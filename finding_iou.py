def find_iou(tl1x, tl1y, br1x, br1y, tl2x, tl2y, br2x, br2y):    
    #iou of -1 means no overlap, iou of 0 means rectangles touch each other at perimeter
    bl2x = tl2x
    bl2y = br2y
    tr2x = br2x
    tr2y = tl2y
    
    bl1x = tl1x
    bl1y = br1y
    tr1x = br1x
    tr1y = tl1y    
    #check if rectangles overlap
    #br1 is inside rectangle 2
    #or bl1 is inside rectangle 2
    #or br2 is inside rectangle 1
    #or bl2 is inside rectangle 1    
    if ( ((tl1x <= tl2x and tl2x <= br1x) and (tl1y <= tl2y and tl2y <= br1y)) \
        or ((tl1x <= tr2x and tr2x <= br1x) and (tl1y <= tr2y and tr2y <= br1y)) \
        or ((tl1x <= br2x and br2x <= br1x) and (tl1y <= br2y and br2y <= br1y)) \
        or ((tl1x <= bl2x and bl2x <= br1x) and (tl1y <= bl2y and bl2y <= br1y)) \
        
        or ((tl2x <= tl1x and tl1x <= br2x) and (tl2y <= tl1y and tl1y <= br2y)) \
        or ((tl2x <= tr1x and tr1x <= br2x) and (tl2y <= tr1y and tr1y <= br2y)) \
        or ((tl2x <= br1x and br1x <= br2x) and (tl2y <= br1y and br1y <= br2y)) \
        or ((tl2x <= bl1x and bl1x <= br2x) and (tl2y <= bl1y and bl1y <= br2y)) ):        
        
        '''
        if ((tl2x < br1x and br1x < br2x) and (tl2y < br1y and br1y < br2y)):
            print ('case1')
        elif ((tl2x < bl1x and bl1x < br2x) and (tl2y < bl1y and bl1y < br2y)):
            print ('case2')
        elif ((tl1x < br2x and br2x < br1x) and (tl1y < br2y and br2y < br1y)):
            print ('case3')
        else:
            print ('case4')
        '''
        #find intersection box co-ordinates
        boxtlx = max(tl1x, tl2x)
        boxtly = max(tl1y, tl2y)
        boxbrx = min(br1x, br2x)
        boxbry = min(br1y, br2y)
        
        #print (boxtlx, boxtly, boxbrx, boxbry)
        intersection_area = abs(boxtlx - boxbrx) * abs(boxtly - boxbry)
        #print (intersection_area)
        box1_area = abs(tl1x - br1x) * abs(tl1y - br1y)        
        box2_area = abs(tl2x - br2x) * abs(tl2y - br2y)
        #print (box1_area, box2_area)
        union_area = box1_area + box2_area - intersection_area
        #print (union_area)
        iou = float(intersection_area) / union_area
        return iou
    else:
        return -1


if __name__ == '__main__':
    tl1x = 170
    tl1y = 98
    br1x = 354
    br1y = 339
    
    tl2x = 174
    tl2y = 101
    br2x = 349
    br2y = 351
    print (find_iou(tl1x, tl1y, br1x, br1y, tl2x, tl2y, br2x, br2y))
