import numpy as np
import cv2

###########################  Count Objects  ###################################
# orig=cv2.imread("6.jpeg")
# a=cv2.imread("6.jpeg")
# a=cv2.cvtColor(a,cv2.COLOR_BGR2GRAY)
# r,a=cv2.threshold(a,195,255,cv2.THRESH_BINARY)
# ker=cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3))
# a=cv2.morphologyEx(a,cv2.MORPH_DILATE,ker,iterations=1)
# b=cv2.bitwise_not(a)
# c,h=cv2.findContours(b,method=cv2.RETR_LIST, mode=cv2.CHAIN_APPROX_NONE)
# list = []
# for x in c:
#     area=cv2.contourArea(x)
#     peri=cv2.arcLength(x,True)
#     list.append(area)
#     #print("Area ",area,"  Perimeter ",peri)
#     e=0.00001*peri
#     x1=cv2.approxPolyDP(x,e,True)
#     if(len(x1)>10):
#         if(area>1000):
#             cv2.drawContours(orig,[x1],-1,(255,0,0),4)
# k=1000
# count = 0
# for i in list:
#     if i > k:
#         count = count + 1
# print(str(count))
#
# cv2.imshow("Orig",orig)
# cv2.waitKey(0)

######################################  Largest Object  ########################
# image= cv2.imread('1.jpeg')
# original_image= image
#
# gray= cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
#
# edges= cv2.Canny(gray, 250,300)
# cv2.imshow("edge",edges)
# contours, hierarchy= cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
#
# def get_contour_areas(contours):
#
#     all_areas= []
#
#     for cnt in contours:
#         area= cv2.contourArea(cnt)
#         all_areas.append(area)
#
#     return all_areas


# sorted_contours= sorted(contours, key=cv2.contourArea, reverse=True)
#
#
# largest_item= sorted_contours[0]
#
# cv2.drawContours(original_image, largest_item, -1, (255,0,0),10)
# # cv2.drawContours(original_image, contours, -1, (255,0,0),10)
#
# cv2.imshow('Largest Object', original_image)
# cv2.waitKey(0)


################################  Smallest Object #############################

# orig=cv2.imread("7.jpeg")
# a=cv2.imread("7.jpeg")
# image= cv2.imread('7.jpeg')
#
# a=cv2.cvtColor(a,cv2.COLOR_BGR2GRAY)
# r,a=cv2.threshold(a,195,255,cv2.THRESH_BINARY)
# ker=cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3))
# a=cv2.morphologyEx(a,cv2.MORPH_DILATE,ker,iterations=1)
# b=cv2.bitwise_not(a)
# c,h=cv2.findContours(b,method=cv2.RETR_LIST, mode=cv2.CHAIN_APPROX_NONE)
# list = []
# for x in c:
#     area=cv2.contourArea(x)
#     peri=cv2.arcLength(x,True)
#     list.append(area)
#     e=0.00001*peri
#     x1=cv2.approxPolyDP(x,e,True)
#     if(len(x1)>10):
#         if(area>1000):
#             cv2.drawContours(orig,[x1],-1,(255,0,0),4)
# k=1000
# count = 0
# for i in list:
#     if i > k:
#         count = count + 1
#
#
#
# original_image= image
#
# gray= cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
#
# edges= cv2.Canny(gray, 250,300)
# # cv2.imshow("edge",edges)
# contours, hierarchy= cv2.findContours(b.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
#
# def get_contour_areas(contours):
#
#     all_areas= []
#
#     for cnt in c:
#         area= cv2.contourArea(cnt)
#         all_areas.append(area)
#
#     return all_areas
#
#
# sorted_contours= sorted(c, key=cv2.contourArea, reverse=True)
#
#
# smallest_item= sorted_contours[0+(count-1)]
# # largest_item= sorted_contours[2]
# cv2.drawContours(original_image, smallest_item, -1, (255,0,0),10)
# # cv2.drawContours(original_image, contours, -1, (255,0,0),10)
#
# cv2.imshow('Smallest Object', original_image)
#
# cv2.waitKey(0)


########################  Unused(Detect Objects)  ##############################
# orig=cv2.imread("1.jpeg")
# a=cv2.imread("1.jpeg")
# a=cv2.cvtColor(a,cv2.COLOR_BGR2GRAY)
# r,a=cv2.threshold(a,195,255,cv2.THRESH_BINARY)
# ker=cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3))
# a=cv2.morphologyEx(a,cv2.MORPH_DILATE,ker,iterations=1)
# b=cv2.bitwise_not(a)
# cv2.imshow("Threshold,Morph & Invert",b)
# (n,label,coord,centroid)=cv2.connectedComponentsWithStats(b)
# res=np.zeros_like(orig)
#
# for i in range(label.shape[0]):
#     for j in range(label.shape[1]):
#         if(label[i,j]==1):
#             res[i,j,:]=orig[i,j,:]
# for i in range(label.shape[0]):
#     for j in range(label.shape[1]):
#         if(label[i,j]==2):
#             res[i,j,:]=orig[i,j,:]
# for i in range(label.shape[0]):
#     for j in range(label.shape[1]):
#         if(label[i,j]==3):
#             res[i,j,:]=orig[i,j,:]
# for i in range(label.shape[0]):
#     for j in range(label.shape[1]):
#         if(label[i,j]==4):
#             res[i,j,:]=orig[i,j,:]
# for i in range(label.shape[0]):
#     for j in range(label.shape[1]):
#         if(label[i,j]==5):
#             res[i,j,:]=orig[i,j,:]
#
# cv2.imshow("Result",res)
# cv2.waitKey(0)
