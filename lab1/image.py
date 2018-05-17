import cv2
import numpy as np
from matplotlib import pyplot as plt
from collections import Counter
import pyautogui
import time
count = 1

# Take screenshot
while True:
   try:     
        time.sleep(5)
        a = []
        pic = pyautogui.screenshot()
        print(count)
       
            #           0                  1               2                    3
            #    0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 
            #2,2,1,1,1,2,1,2,2,2,2,2,2,2,2,1,2,2,2,2,2,1,1,1,1,2,2,2,2,2,1,1,1,1,2,2,2,2,2,1,1,1,1,2,2,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1
       # nural = [8,2,2,1,1,1,2,2,2,2,2,2,1,1,2,2,2,2,2,1,1,1,1,1,1,1,1,1,3,1,1,3,1]
        nural = [8,2,2,1,1,1,2,1,2,2,2,2,2,2,2,2,1,2,2,2,2,2,1,1,1,1,2,2,2,2,2,1,1,1,1,2,2,2,2,2,1,1,1,1,2,2,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

        print(nural[count])
        # Save the image
        pic.save('C:\imageprocessing\main.jpg') 
        img = cv2.imread('C:\imageprocessing\main.jpg',0)
        img2 = img.copy()
        template = cv2.imread('C:\\imageprocessing\\'+str(count)+".png",0)
    # path = './1.jpg'
    # path=path + count

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
        print(z)
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
            if second1 >=3 :
             if second1 >second2:
                print("greaer than")
                time.sleep(1)
                pyautogui.rightClick(top_left)
                # print(first1)
                count =count +1
                time.sleep(1)
                second1=0
                a = []
        #   break
    
        if nural[count] ==2:
            if second1 >=3 :
             if second1 >second2:
                print("greaer than")
                time.sleep(1)
                pyautogui.doubleClick(top_left)
                # print(first1)
                count =count +1
                time.sleep(1)
                second1=0
                a = []
        #   break

        if nural[count] ==1:
            if second1 >=3 :
             if second1 >second2:
                    print("greaer than")
                    time.sleep(1)
                    pyautogui.click(top_left)
                    # print(first1)
                    count =count +1
                    time.sleep(1)
                    second1=0
                    a = []
        #   break
        if count ==33:
            count = 1
   except:
    print("xc")
    time.sleep(1)
    









