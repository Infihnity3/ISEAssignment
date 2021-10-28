import cv2
import numpy as np
orig=cv2.imread("002.jpeg")
a=cv2.imread("002.jpeg")
# cv2.imshow("orig",a)
a=cv2.cvtColor(a,cv2.COLOR_BGR2GRAY)
# cv2.imshow("grey",a)
r,a=cv2.threshold(a,140,255,cv2.THRESH_BINARY)
cv2.imshow("thresh",a)
ker=cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3))
a=cv2.morphologyEx(a,cv2.MORPH_DILATE,ker,iterations=1)
cv2.imshow("Morphed",a)


# res=np.zeros_like(orig)
# for i in range(label.shape[0]):
#     for j in range(label.shape[1]):
#         if(label[i,j]==0):
#             res[i,j,:]=orig[i,j,:]
#
# cv2.imshow("Res",res)
#
(n,label,coord,centroid)=cv2.connectedComponentsWithStats(a)
filter=np.zeros_like(orig)
for (x,y,w,h,area) in coord:
    if(area>100 and area<8000):
        # cv2.rectangle(orig,(x,y),(x+w,y+h),thickness=2,color=(0,0,255))
        cv2.rectangle(filter,(x,y),(x+w,y+w),(255,255,255),-1)

new_im=np.zeros_like(orig)
new_im[:,:,2]=255
cv2.imshow("Original",orig)
cv2.imshow("Filter",filter)
temp_res=cv2.bitwise_and(orig,filter)
new_im=new_im + temp_res
cv2.imshow("New",new_im)

cv2.imshow("temp Result",temp_res)
cv2.waitKey(0)