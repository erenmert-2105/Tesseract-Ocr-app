import pyautogui
import win32api
import time 
from PIL import ImageGrab
import os
import numpy as np
import pytesseract
import pandas as pd
import re
import sys




def get_loc(key_code):
    n=0
    counter=0
    a=win32api.GetKeyState(key_code)
    b=a
    while True:
            
        
        
        a=win32api.GetKeyState(key_code)
        
        time.sleep(0.1)
        
        
        if a == b:
            continue
            time.sleep(0.1)
        elif a!= b:
            a = b
            x, y = pyautogui.position()
            return x,y
        
pytesseract.pytesseract.tesseract_cmd = 'C:/Users/meren/AppData/Local/Programs/Tesseract-OCR/tesseract.exe'
custom_oem_psm_config = r'--oem 3 --psm 4'
           
     

key_code=83

print("INFORMATION")
print("This program takes your selected areas at tabeles as image and export as excel file ")

print("resolution metters between %100 and %150 just works fine")
time.sleep(2)
print("mode1 : only name")
print("mode2 : name + count")
print("If you are using mod2, you need to select the numbers column first and also select that column in pairs. ")
time.sleep(1)
mode = input("plese chose mode_1(1) or mode_2(2) ")
#%%
if mode ==str(2):
    while True:
        prb=0
        print("select areas with pressing key s and mause over location, please point count collumn then name collumn")
        
        a,b=get_loc(key_code)   
        #print(a,b)
        print("one_done, three to go !")
        time.sleep(1)
        c,d=get_loc(key_code) 
        #print(c,d)
        print("second_done, two to go !")
        time.sleep(1)
        a1,b1=get_loc(key_code) 
        #print(a1,b1)
        print("third_done, one to go !")
        time.sleep(1)
        c1,d1=get_loc(key_code) 
        #print(c1,d1)
        print("forth_done, all done !")
        time.sleep(0.3)
        print("precessing..")
        time.sleep(0.5)
        
        try:
            im=ImageGrab.grab(bbox=(a,b,c,d))   
            im1=ImageGrab.grab(bbox=(a1,b1,c1,d1)) 
        except:
            prb=1
        
        if prb ==1:
            inpt2 = input("There is problem with selected areas. Do you wanna try again or exit try(1), exit(2) ")
            if inpt2==str(2):
                print("Good by..")
                time.sleep(3)
                sys.exit()
                break
            else:
                print("restarting...")
                time.sleep(3)
        else:
            im = im.convert('L')
            im1 = im1.convert('L')
            im = np.array(im) 
            im1 = np.array(im1)
                
            
            
            # Open the image and perform OCR on it
            
            text = pytesseract.image_to_string(im, lang='tur')
            text1= pytesseract.image_to_string(im1, lang='tur')
            
            
            
            text = re.findall(r'\d+\.\d+|\d+,\d+|\d+', text)
            text1 = text1.split("\n")
            text1 = [item for item in text1 if item != '']
            
            text=np.array(text)
            text = np.char.replace(text, ",", ".")
            text1=np.array(text1)
            
            try:
                df = pd.DataFrame({'Names': text1, 'Numbers': text})
                writer = pd.ExcelWriter('C:/Users/meren/Desktop/my_list.xlsx', engine='xlsxwriter')
                df.to_excel(writer, index=False, sheet_name='Sheet1')
                writer.save()
                print("successful !")
            except Exception as e:
                print("Error,  something went wrong, probably resolution not fit:", e)
            finally:
                inpt = input("Do you wanna continue yes(1), no(2) ")
                while True:
                    if inpt == str(1) or str(2):
                        break
                    else:
                        inpt = input("Do you wanna continue yes(1), no(2) ")
                if inpt == str(2):     
                    print("Good by..")
                    time.sleep(3)
                    sys.exit()
                    break
#%%                    
elif mode == str(1):
    while True:
        prb=0
        print("please select areas of name colmn only with pressing key s")
        
        a,b=get_loc(key_code)   
        #print(a,b)
        print("one_done, one to go !")
        time.sleep(1)
        c,d=get_loc(key_code) 
        #print(c,d)
        print("second_done, done !")
        
        try:
            im=ImageGrab.grab(bbox=(a,b,c,d))           
        except:
            prb=1        

        if prb ==1:
            inpt2 = input("There is problem with selected areas. Do you wanna try again or exit try(1), exit(2) ")
            if inpt2==str(2):
                print("Good by..")
                time.sleep(3)
                sys.exit()
                break
            else:
                print("restarting...")
                time.sleep(3)
        else:
            im = im.convert('L')
            im = np.array(im)
            print("precessing..")
            time.sleep(0.5)
            
            text = pytesseract.image_to_string(im, lang='tur')
            text = text.split("\n")
            text = [item for item in text if item != '']
            text1=np.array(text)
            text = np.zeros_like(text1)
            
            try:
                df = pd.DataFrame({'Names': text1, 'Numbers': text})
                writer = pd.ExcelWriter('C:/Users/meren/Desktop/my_list.xlsx', engine='xlsxwriter')
                df.to_excel(writer, index=False, sheet_name='Sheet1')
                writer.save()
                print("successful !")
            except Exception as e:
                print("Error,  something went wrong:", e)
            finally:
                inpt = input("Do you wanna continue yes(1), no(2) ")
                while True:
                    if inpt == str(1) or str(2):
                        break
                    else:
                        inpt = input("Do you wanna continue yes(1), no(2) ")
                if inpt == str(2):     
                    print("Good by..")
                    time.sleep(3)
                    sys.exit()
                    break
            
                
#%%                
else:
    print("Unsupported input, sytem is going to terminate it self in ")
    print("3 seconds")
    time.sleep(1)
    print("2 seconds")
    time.sleep(1)
    print("1 second")
    time.sleep(1)
    print("Good by..")
    sys.exit()
            








