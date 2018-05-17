import cv2
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import msvcrt
import datetime
#ekanath25   sathish0792

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
from collections import Counter
import pyautogui
import time
import os
import shutil
import ctypes
secondimagecount=0
firstalg=0
count = 1
lock=1
counttwo=0
name="karthick"
# Take screenshot




chrome_options = Options()
chrome_options.add_argument("--disable-infobars")
browser = webdriver.Chrome(executable_path = "C:\chromedriver_win32\chromedriver.exe",chrome_options=chrome_options)
position=1
nowdatetime=str((datetime.datetime.now()))
tab=0;
logincount=1
sessionstart=1
while 1:
  time.sleep(8);
  try: 
   print(nowdatetime)
   print(position)
  # time.sleep(1)
   if position ==1:
    try:
     browser.get("https://portal.demoemc.com/reg-login/login.html")
     position=position+1
    except:
     print ("open")
    
#ekanath25   sathish0792
    n = 3
    
   
    if n ==1:
       
        name ="karthick"
        
    if n ==2:
        name ="rajkumar"
      
    if n ==3:
        name ="ramesh"
        
    if n ==4:
        name ="sathish0792"
      
    if n ==5:
        name ="ekanath25"
        


   if position ==2:
    try:
      browser.maximize_window()
      username = browser.find_element_by_name('uname')
      username.send_keys(name)
      password = browser.find_element_by_name('pass')
      password.send_keys('UPEIXRAA@2')
      position=position+1
    except:
     print ("login send")

   if position ==3:
    try:
     form = browser.find_element_by_id('submit')
     form.submit()
     position=position+1
     logincount=1
    except:
       print ("opegee")
       logincount=logincount+1
       if logincount >=50:
          print("login try than50")
          
          time.sleep(20)
          browser.quit()
          chrome_options = Options()
          chrome_options.add_argument("--disable-infobars")
          browser = webdriver.Chrome(executable_path = "C:\chromedriver_win32\chromedriver.exe",chrome_options=chrome_options)
          position=1
          nowdatetime=str((datetime.datetime.now()))
          tab=0;
          logincount=1
          position=ActionChains
      
   if position ==4:
    try:
     time.sleep(4)
     form = browser.find_element_by_id('500001247')
     form.click()
     #time.sleep(4)
     logincount=1
     position=position+1
   
     
    except:
     print ("open login")
     logincount=logincount+1
     print("logincount",logincount)
     if logincount >=50:
       print("login time exceeded")
       time.sleep(20)
       browser.quit()
       chrome_options = Options()
       chrome_options.add_argument("--disable-infobars")
       browser = webdriver.Chrome(executable_path = "C:\chromedriver_win32\chromedriver.exe",chrome_options=chrome_options)
       position=1
       nowdatetime=str((datetime.datetime.now()))
       tab=0;
       logincount=1
       position=1

     

   if position ==5:
    try:
     #time.sleep(4)
    # //*[@id="500001247"]/div[2]/a/i
     
     elem =  browser.find_element_by_xpath('//*[@id="500001247"]/div[2]/a/i')
     elem.click()
     time.sleep(4)
     
     position=position+1
    except:
      print ("opegee")
      
   if position ==6:
    try:
     time.sleep(4)
     text= "Sessions Available Pre-Provisioned";
     x=browser.find_element_by_xpath(("//*[contains(text(),'"+text+"')]"));
     x=str(x);
     if "selenium.webdriver.remote.webelement.WebElement" in x:
       position=position+1
    except:
      print ("opegee")
      logincount=logincount+1
      print("logincount",logincount)
      if logincount >=50:
       print("login count greater than50")
       sessionname = browser.find_element_by_xpath('  //*[@id="startSession"]/a')
       sessionname.click()
       time.sleep(3)
       sessionname = browser.find_element_by_xpath('//*[@id="signOutLink"]')
       sessionname.click()
       time.sleep(20)
       browser.quit()
       chrome_options = Options()
       chrome_options.add_argument("--disable-infobars")
       browser = webdriver.Chrome(executable_path = "C:\chromedriver_win32\chromedriver.exe",chrome_options=chrome_options)
       position=1
       nowdatetime=str((datetime.datetime.now()))
       tab=0;
       logincount=1
       position=1
   if position ==7:
    try:
     sessionname = browser.find_element_by_xpath('//*[@id="sessionName"]')
     sessionname.clear();
    
     sessionname.send_keys(nowdatetime)
     time.sleep(3)
    # with open("read.txt", "w") as myfile:
     # myfile.write(notepadvalue)
      #myfile.close();
       
     position=position+1
    except:
     print ("open v spear")

   if position ==8:
    try:
     time.sleep(4)
     form1 = browser.find_element_by_xpath('//*[@id="purpose"]')
     form1.click()
     time.sleep(4)
     position=position+1
    except:
     print ("purpose")

   if position ==9:
    try:
     time.sleep(4)
     form2 = browser.find_element_by_xpath('//*[@id="ui-id-4"]')
     form2.click()
     time.sleep(4)
     position=position+1
    except:
     print ("uid")

   if position ==10:
    try:
     time.sleep(4)
     sessionname = browser.find_element_by_xpath('//*[@id="duration"]')
     sessionname.clear();
     sessionname.send_keys('7')
     time.sleep(4)
     position=position+1
    except:
     print ("duration")

   if position ==11:
    try:
     sessionname = browser.find_element_by_xpath('//*[@id="durationHours"]')
     sessionname.clear();
     sessionname.send_keys('24')
     position=position+1
    except:
     print ("hours")


   if position ==12:
    try:
     time.sleep(4)
     sessionname = browser.find_element_by_xpath('//*[@id="submitStartSession"]')
     sessionname.click()
     time.sleep(50)
     sessionstart=1

     position=position+1
    except:
     sessionstart=sessionstart+1
     if sessionstart >=50:
       print("sessionstart  count greater than50")
       time.sleep(20)
       browser.quit()
       chrome_options = Options()
       chrome_options.add_argument("--disable-infobars")
       browser = webdriver.Chrome(executable_path = "C:\chromedriver_win32\chromedriver.exe",chrome_options=chrome_options)
       position=1
       nowdatetime=str((datetime.datetime.now()))
       tab=0;
       logincount=1
       position=1
       sessionstart=1



     print ("session start")
  

   if position ==13:
    try:
     print ("Sleep started") 
     
     time.sleep(100)
     print ("seconditions sleep To refresh") 
     
     browser.refresh();
     time.sleep(80)
    
     
     
     
     user = browser.find_element_by_xpath("//*[@name='"+nowdatetime+"']")
     actionChains = ActionChains(browser)
     actionChains.double_click(user).perform()
     nowdatetime=str((datetime.datetime.now()))
     position=position+1
    except:
     print ("session start")


   if position ==14:
    try:
      print ("session start")
      try:
        time.sleep(2)
        firstalg=0
        a = []
        pic = pyautogui.screenshot()
        print(count,"image")
       
                     
           
                
       
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
                            time.sleep(1)
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
            time.sleep(20)
            browser.quit()
            chrome_options = Options()
            chrome_options.add_argument("--disable-infobars")
            browser = webdriver.Chrome(executable_path = "C:\chromedriver_win32\chromedriver.exe",chrome_options=chrome_options)
            position=1
            nowdatetime=str((datetime.datetime.now()))
            tab=0;
            position=1
  
            count = 1
            clear = lambda: os.system('cls')
            clear()
        if count ==2:
             print("two  count=",counttwo)
             counttwo=counttwo+1
             if counttwo ==20:
               # pyautogui.press('f5')
                pyautogui.click(x=72, y=40)
                counttwo=0
                secondimagecount=secondimagecount+1
                print("two count 10 times count=",secondimagecount)
                if secondimagecount >=10:
                   time.sleep(5)
                   browser.quit()
                   chrome_options = Options()
                   chrome_options.add_argument("--disable-infobars")
                   browser = webdriver.Chrome(executable_path = "C:\chromedriver_win32\chromedriver.exe",chrome_options=chrome_options)
                   nowdatetime=str((datetime.datetime.now()))
                   secondimagecount=0
                   position=1
                   count = 1




       # time.sleep(1)secondimagecount=0

      except:
       print("xc")
    #time.sleep(1)

       # allWindowHandles =0
       # allWindowHandles = len(browser.window_handles)
       # allWindowHandles = len(browser.window_handles)
       # print(allWindowHandles)
        
        
        #if allWindowHandles==3:
        #    tab=1
            
        #if (tab==1 and  allWindowHandles==2):
        #    sessionname = browser.find_element_by_xpath('//*[@id="signOutLink"]')
        #    sessionname.click()
         ##   time.sleep(20)
          #  browser.quit()
          #  chrome_options = Options()
          #  chrome_options.add_argument("--disable-infobars")
          #  browser = webdriver.Chrome(executable_path = "C:\chromedriver_win32\chromedriver.exe",chrome_options=chrome_options)
          #  position=1
          #  nowdatetime=str((datetime.datetime.now()))
          #  tab=0;
          #  position=1
            
       
    except:
     print ("lenth error")









   
    if msvcrt.kbhit():
  	  if ord(msvcrt.getch()) == 27:
	      break

  except:
      print ("final try catch")



  








