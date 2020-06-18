import cv2
import numpy as np
from datetime import datetime
import os

cap=cv2.VideoCapture(0)
for i in range(0,5):
    ret,frame=cap.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imwrite("jk.jpg",gray)
    cv2.waitKey(65)
    
cap.release()
cv2.destroyAllWindows()
x=datetime.now()
s=str(".jpg")
t=x.strftime("%m%d%y%H%M%S")
z4=str(t)+s
try:
    
    os.rename("jk.jpg",z4)
except:
    pass

