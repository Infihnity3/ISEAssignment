import numpy as np
import matplotlib.pyplot as plt
import cv2

orig=cv2.imread("1.jpg")
a=cv2.imread("1.jpg")
cv2.imshow("Orig",a)
a=cv2.cvtColor(a,cv2.COLOR_BGR2GRAY)
r,a=cv2.threshold(a,130,255,cv2.THRESH_BINARY)
ker=cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3))
a=cv2.morphologyEx(a,cv2.MORPH_DILATE,ker,iterations=2)
cv2.imshow("MASK",a)
res=np.zeros_like(orig)
res[:,:,2]=255
for i in range(orig.shape[0]):
    for j in range(orig.shape[1]):
        if(a[i,j]==255):
            res[i,j,:]=orig[i,j,:]
cv2.imshow("Res",res)
cv2.waitKey(0)

import cv2
import numpy as np
orig=cv2.imread("coin.jpg")
a=cv2.imread("coin.jpg")
cv2.imshow("Orig",a)
a=cv2.cvtColor(a,cv2.COLOR_BGR2GRAY)
r,a=cv2.threshold(a,130,255,cv2.THRESH_BINARY)
ker=cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3))
a=cv2.morphologyEx(a,cv2.MORPH_DILATE,ker,iterations=2)
cv2.imshow("MASK",a)
(n,label,coord,centroid)=cv2.connectedComponentsWithStats(a)
res=np.zeros_like(orig)
for i in range(label.shape[0]):
    for j in range(label.shape[1]):
        if(label[i,j]==0):
            res[i,j,:]=orig[i,j,:]
cv2.imshow("Label-1",res)
cv2.waitKey(0)

import cv2
import numpy as np
orig=cv2.imread("coin.jpg")
a=cv2.imread("coin.jpg")
a=cv2.cvtColor(a,cv2.COLOR_BGR2GRAY)
r,a=cv2.threshold(a,130,255,cv2.THRESH_BINARY)
ker=cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3))
a=cv2.morphologyEx(a,cv2.MORPH_DILATE,ker,iterations=2)
cv2.imshow("MASK",a)
(n,label,coord,centroid)=cv2.connectedComponentsWithStats(a)
res=np.zeros_like(orig)
for i in range(label.shape[0]):
    for j in range(label.shape[1]):
        if(label[i,j]==2):
            res[i,j,:]=orig[i,j,:]
for (x,y,w,h,area) in coord:
    cv2.rectangle(orig,(x,y),(x+w,y+h),thickness=2,color=(0,0,255))
cv2.imshow("Orig",orig)
cv2.imshow("Label-1",res)
cv2.waitKey(0)
