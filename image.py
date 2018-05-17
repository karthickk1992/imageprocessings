import cv2
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
from collections import Counter
import pyautogui
import time
import os
import shutil
import ctypes
firstalg=0
count = 2
lock=1
counttwo=0
# Take screenshot
while 1:
   try:
        time.sleep(3)
        firstalg=0
        a = []
        pic = pyautogui.screenshot()
        print(count)
       
                     
           
                
       
            #           0                  1               2                    3
            #    0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 
           
       # nural = [8,2,2,1,1,1,2,2,2,2,2,2,1,1,2,2,2,2,2,1,1,1,1,1,1,1,1,1,3,1,1,3,1]
          #                    0             1                   2                     3                    4                 5                    6
          #      0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0           1                     2
        nural = [8,2,2,1,1,1,2,1,2,2,2,2,2,2,2,2,1,2,2,2,2,2,1,1,1,1,2,2,2,2,2,1,1,1,1,2,2,2,2,2,1,1,1,1,2,2,2,2,2,1,1,1,2,3,1,1,3,1]
      #  nural =  [8,2,2,1,1,3]

       # print(nural[count])
        # Save the image
        pic.save('C:\imageprocessing\main.png') 
        img = cv2.imread('C:\imageprocessing\main.png',0)
        img2 = img.copy()
        template = cv2.imread('C:\\imageprocessing\\'+str(count)+".png",0)
    # path = './1.jpg'
    # path=path + count

   ###############################################################

        img_rgb = cv.imread('C:\imageprocessing\main.png')
        img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)
        template = cv.imread('C:\\imageprocessing\\'+str(count)+".png",0)
        w, h = template.shape[::-1]
        res = cv.matchTemplate(img_gray,template,cv.TM_CCOEFF_NORMED)
        threshold = 0.6
        loc = np.where( res >= threshold)
        for pt in zip(*loc[::-1]):
            firstalg=1
            cv.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
        cv.imwrite('res.png',img_rgb)
    ############################################################

    

    # template = cv2.imread(str('C:\imageprocessing\++.jpg',0)
        w, h = template.shape[::-1]

        # All the 6 methods for comparison in a list
        methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
                    'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

        for meth in methods:
           
            img = img2.copy()
            method = eval(meth)

            # Apply template Matching
            res = cv2.matchTemplate(img,template,method)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

            # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
            if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
                top_left = min_loc
            else:
                top_left = max_loc
            bottom_right = (top_left[0] + w, top_left[1] + h)
        

            cv2.rectangle(img,top_left, bottom_right, (0,0,255),4)
            #shutil.copy(os.path.join("C:\imageprocessing\dummy.jpg"), os.path.join("C:\imageprocessing\main.jpg"))
            # plt.subplot(121),plt.imshow(res,cmap = 'gray')
            # plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
            # plt.subplot(122),plt.imshow(img,cmap = 'gray')
            # plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
            
            #print(top_left,bottom_right)
            a.append((top_left))
            #pyautogui.doubleClick(top_left)
            plt.suptitle(meth)
            #plt.show()
        z=Counter(a)
        # print("sdfsdsdfdfdfsdfsdf")
       # print(z)
        first1 =  0
        second1 = 0
        first2 =  0
        second2 = 0
        for i,j in z.most_common(1):
            first1 = (i)
            second1 = (j)
           
        for i,j in z.most_common(2):
            first2 = (i)
            second2 = (j)

        # print(first1)
        # print(second1)

        # print(first2)
        # print(second2)
        if nural[count] ==3:
           if lock==1:
            if second1 >=3 :
             if second1 >second2 and firstalg==1 :
                lock=0
                second1=0
                second2=0
                
                a = []
                #time.sleep(5)
                print("greaer than3")
             
                pyautogui.rightClick(top_left)
               # time.sleep(3)
                
                
                # print(first1)
                count =count +1
                lock=1
        #   break
    
        if nural[count] ==2:
           if lock==1:
            if second1 >=3 :
             if second1 >second2 and firstalg==1:
                lock=0
                second1=0
                second2=0
                
                a = []
                #time.sleep(5)
                print("greaer than2")
                #time.sleep(3)
                pyautogui.doubleClick(top_left)
                time.sleep(3)
                # print(first1)
                
                count =count +1
                lock=1
                
        #   break

        if nural[count] ==1:
           if lock==1:
            if second1 >=3 :
             if second1 >second2 and firstalg==1:
                    lock=0
                  #  shutil.copy(os.path.join("C:\imageprocessing\dummy.jpg"), os.path.join("C:\imageprocessing\main.jpg"))
                    second1=0
                    second2=0
                    
                    a = []
                   # print(lock)
                    if count ==7 and count ==8:
                       time.sleep(6)
                    if count ==4:
                                #time.sleep(2)
                                x, y =top_left
                              #  print(x)
                               # print(y)
                                ctypes.windll.user32.SetCursorPos(x,y)
                                #ctypes.windll.user32.SetCursorPos(647, 120)
                                ctypes.windll.user32.mouse_event(2, 0, 0, 0,0) # left down
                                time.sleep(.1)
                                ctypes.windll.user32.mouse_event(4, 0, 0, 0,0) # left up
                                print("others")  
                    else:
                            time.sleep(2)
                            pyautogui.PAUSE = 2.5
                            pyautogui.FAILSAFE = True
                            pyautogui.click(top_left)
                           # print(top_left)
                            print("ccc")  
                 #   break
                   # time.sleep(2)
                    # print(first1)
                   
                    top_left=0
                    count =count +1
                    lock=1
                    #print(lock)
                    
        #   break
        if count >=56:
            print("56 to 1")
            time.sleep(223)
            count = 1
        if count ==2:
             print("two  count=",counttwo)
             counttwo=counttwo+1
             if counttwo ==20:
                pyautogui.press('f5')
                counttwo=0
       # time.sleep(1)
   except:
    print("xc")
    #time.sleep(1)
    









