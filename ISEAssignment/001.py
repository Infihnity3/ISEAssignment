################################  Import  ######################################
import cv2

################################  Select Image  ################################
select = "8.jpeg"
original = cv2.imread(select)
original1 = cv2.imread(select)
original2 = cv2.imread(select)
image = cv2.imread(select)

################################  Count Objects  ###############################
a = cv2.imread(select)
a = cv2.cvtColor(a, cv2.COLOR_BGR2GRAY)
r, a = cv2.threshold(a, 195, 255, cv2.THRESH_BINARY)
ker = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))
a = cv2.morphologyEx(a, cv2.MORPH_DILATE, ker, iterations = 1)
b = cv2.bitwise_not(a)
c, h = cv2.findContours(b, method = cv2.RETR_LIST, mode = cv2.CHAIN_APPROX_NONE)

list = []
for x in c:
    area = cv2.contourArea(x)
    peri = cv2.arcLength(x, True)
    list.append(area)
    e = 0.00001 * peri
    x1 = cv2.approxPolyDP(x, e, True)
    if(len(x1) > 10):
        if(area > 1000):
            cv2.drawContours(original, [x1], -1, (255, 0, 0), 10)
k = 1000
count = 0
for i in list:
    if i > k:
        count = count + 1
print("Number of Objects: " + str(count))
cv2.imshow("Number of Objects", original)
################################################################################

################################  Smallest Object  #############################
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 250, 300)
contoursS, hierarchy = cv2.findContours(b.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
sortedContoursS = sorted(c, key = cv2.contourArea, reverse = True)
smallest = sortedContoursS[0 + (count - 1)]
cv2.drawContours(original1, smallest, -1, (255, 0, 0), 10)
cv2.imshow("Smallest Object", original1)
################################################################################

################################  Largest Object  ##############################
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 250, 300)
contoursL, hierarchy = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
sortedContoursL = sorted(contoursL, key = cv2.contourArea, reverse = True)
largest = sortedContoursL[0]
cv2.drawContours(original2, largest, -1, (255, 0, 0), 10)
cv2.imshow("Largest Object", original2)
################################################################################

################################  Detect GreyScaled ############################
if len(image.shape) == 3:
    print("This is a coloured image")
elif len(image.shape) == 2:
    print("This is a grayscale image")
################################################################################
cv2.waitKey(0)
