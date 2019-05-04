
import os
import shutil
import numpy as np
import cv2 
import matplotlib.pyplot as plt
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
path = #source path
dst1=#important files path
dst2=#unimportant files path
files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
            files.append(os.path.join(r, file))


#shutil.move(src,dst)
print("done")
for i in files:
    test_image = cv2.imread(i)
    test_image_gray = cv2.cvtColor(test_image, cv2.COLOR_BGR2GRAY)
    haar_cascade_face = cv2.CascadeClassifier('snippet.xml')
    faces_rects = haar_cascade_face.detectMultiScale(test_image_gray, scaleFactor = 1.2, minNeighbors = 5);
    s=len(faces_rects)
    if s==0:
        shutil.move(i,dst2)
        pass
    else:
        config = ('-l eng --oem 1 --psm 3')
        im = cv2.imread(i, cv2.IMREAD_COLOR)
        text = pytesseract.image_to_string(im, config=config)
        if text=="":
            shutil.move(i,dst1)  
        else:
            shutil.move(i,dst2)       
print("cool")        

def convertToRGB(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)    
