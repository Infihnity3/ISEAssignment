import numpy as np
import cv2
import matplotlib.pyplot as plt

def dumf(x):
    return(0)
a=cv2.imread("001.jpeg")
a=cv2.cvtColor(a,cv2.COLOR_BGR2GRAY)
cv2.imshow("Orig",a)
b=a
cv2.imshow("Laplacian",b)
cv2.imshow("Threshold",b)
cv2.createTrackbar("kernel","Laplacian",1,10,dumf)
cv2.createTrackbar("sigma","Laplacian",1,10,dumf)
cv2.createTrackbar("thresh","Threshold",100,dumf)

while(1):
    ker=cv2.getTrackbarPos("kernel","Laplacian")
    sig = cv2.getTrackbarPos("sigma", "Laplacian")
    thresh=cv2.getTrackbarPos("thresh", "Threshold")
    # ker=6
    # sig=10
    # thresh=254
    if(ker%2==0):
        ker=ker+1     # Make kernel size always odd
    b = cv2.GaussianBlur(a, ksize=(ker, ker), sigmaX=sig)  # Blurring to remove noise
    b = cv2.Laplacian(b, -1, ksize=ker) # Determine edge features
    cv2.imshow("Laplacian", b)
    r,c=cv2.threshold(b,thresh,255,cv2.THRESH_BINARY)
    cv2.imshow("Threshold", c)
    key=cv2.waitKey(10)
    if(key==32 or ker==-1 or sig ==-1):
        break




# def dumf(x):
#     return(1)
# a=cv2.imread("stationary.jpeg")
# a=cv2.cvtColor(a,cv2.COLOR_BGR2GRAY)
# r,a=cv2.threshold(a,200,255,cv2.THRESH_BINARY)
# cv2.imshow("Image",a)
# # k=np.array([[0,1,0],[1,1,1],[0,1,0]])  # Manually create a structuring element
# k=cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3))
# print(k)
# b=a
# cv2.imshow("Eroded",b)
# cv2.imshow("Dilated",b)
# cv2.imshow("Open",b)
# cv2.imshow("Close",b)
# cv2.namedWindow("Operation")
# cv2.createTrackbar("Iteration","Operation",0,20,dumf)
# while(1):
#     iter=cv2.getTrackbarPos("Iteration","Operation")
#     b1=cv2.morphologyEx(a,cv2.MORPH_DILATE,kernel=k,iterations=iter)
#     b2 = cv2.morphologyEx(a, cv2.MORPH_ERODE, kernel=k, iterations=iter)
#     b3=cv2.morphologyEx(a, cv2.MORPH_OPEN, kernel=k, iterations=iter) # Erode (Dilate (img))
#     b4 = cv2.morphologyEx(a, cv2.MORPH_CLOSE, kernel=k, iterations=iter) # Dilate (Erode(img))
#     cv2.imshow("Dilated", b1)
#     cv2.imshow("Eroded", b2)
#     cv2.imshow("Open", b3)
#     cv2.imshow("Close", b4)
#     key=cv2.waitKey(10)
#     if(key==32 or iter==-1):
#         break






# orig=cv2.imread("stationary.jpeg")
# a=cv2.imread("stationary.jpeg")
# cv2.imshow("Orig",a)
# a=cv2.cvtColor(a,cv2.COLOR_BGR2GRAY)
# r,a=cv2.threshold(a,130,255,cv2.THRESH_BINARY)
# ker=cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3))
# a=cv2.morphologyEx(a,cv2.MORPH_DILATE,ker,iterations=2)
# cv2.imshow("MASK",a)
# res=np.zeros_like(orig)
# res[:,:,2]=255
# for i in range(orig.shape[0]):
#     for j in range(orig.shape[1]):
#         if(a[i,j]==255):
#             res[i,j,:]=orig[i,j,:]
# cv2.imshow("Res",res)
# cv2.waitKey(0)






# orig=cv2.imread("stationary.jpeg")
# a=cv2.imread("stationary.jpeg")
# # cv2.imshow("orig",a)
# a=cv2.cvtColor(a,cv2.COLOR_BGR2GRAY)
# # cv2.imshow("grey",a)
# r,a=cv2.threshold(a,140,255,cv2.THRESH_BINARY)
# cv2.imshow("thresh",a)
# # ker=cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3))
# # a=cv2.morphologyEx(a,cv2.MORPH_DILATE,ker,iterations=1)
# # cv2.imshow("Morphed",a)
# #
# (n,label,coord,centroid)=cv2.connectedComponentsWithStats(a)
# # res=np.zeros_like(orig)
# # for i in range(label.shape[0]):
# #     for j in range(label.shape[1]):
# #         if(label[i,j]==0):
# #             res[i,j,:]=orig[i,j,:]
# #
# # cv2.imshow("Res",res)
# #
# filter=np.zeros_like(orig)
# for (x,y,w,h,area) in coord:
#     if(area>0 and area<6000):
#         # cv2.rectangle(orig,(x,y),(x+w,y+h),thickness=2,color=(0,0,255))
#         cv2.rectangle(filter,(x,y),(x+w,y+w),(255,255,255),-1)
#
# new_im=np.zeros_like(orig)
# new_im[:,:,2]=255
# cv2.imshow("Orig",orig)
# cv2.imshow("Filter",filter)
# temp_res=cv2.bitwise_and(orig,filter)
# cv2.imshow("New",new_im)
#
# cv2.imshow("temp Result",temp_res)
# cv2.waitKey(0)

















#######################################  Others  #############################

# img = cv2.imread("opm.png")   #To read an image file
# cv2.imshow("Colors", img)       # Create a window "Fruits" and display the image
# copy = np.copy(img)
# copy[:, :, 0] = 0   #Blue
# # copy[:,:,1]=0   #Green
# copy[:, :, 2] = 0   #Red
#
# cv2.imshow("copy", copy)
# cv2.waitKey(0)
#
#  img=cv2.imread("darkim.jpg")   #To read an image file
# # cv2.imshow("Colors",img)       # Create a window "Colors" and display the image
#
# copy=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  # Gray_Scale converted image
# cv2.imshow("Gray_image",img)
# # copy=255-copy                              # Linear Transformation
# c=70
# copy=np.uint8(c*np.log10(1+copy))
# print(copy)
# cv2.imshow("Transformed",copy)
#
# cv2.waitKey(0)

# def f(x):
#     print(x)
#     return(0)
#
# img=cv2.imread("darkim.jpg")   #To read an image file
# copy=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  # Gray_Scale converted image
# cv2.imshow("Image",img)
# cv2.createTrackbar("c","Image",10,100,f)
#
# while(True):
#     c=cv2.getTrackbarPos("c","Image")
#     new_im=np.uint8(c*np.log10(1+copy))
#     cv2.imshow("Image",new_im)
#     key=cv2.waitKey(100)
#     if(key==32):
#         break

# c=70
# x=np.linspace(0,255,300)
# y=c*np.log10(1+x)
#
# x1=np.array([3,5,10,20,200,210])
# y1=c*np.log10(1+x1)
# print(x1)
# print(y1)
# plt.figure(0)
# plt.plot(x,y)
# plt.scatter(x1,y1)
# plt.show()
