import cv2
img1 = cv2.imread('messi.jpg')
img2 = cv2.imread('opencv_logo_bb.png')
rows,cols,channels = img2.shape
row,col,channel = img1.shape
roi = img1[row - rows:row,0:cols]
img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
#如果是白底黑字，加入下面这一行
#img2gray = cv2.bitwise_not(img2gray)

ret,mask = cv2.threshold(img2gray,10,255,cv2.THRESH_BINARY)
#ret,mask_inv = cv2.threshold(img2gray,10,255,cv2.THRESH_BINARY_INV)
mask_inv = cv2.bitwise_not(mask)
img1_background = cv2.bitwise_and(roi,roi,mask=mask_inv)
cv2.imshow('bg',img1_background)
img2_fontgrand = cv2.bitwise_and(img2,img2,mask=mask)
cv2.imshow('fg',img2_fontgrand)
dst= cv2.add(img1_background,img2_fontgrand)
cv2.imshow('dst',dst)
row,col,channels = img1.shape
img1[row - rows:row,0:cols] = dst
cv2.imshow('rest',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
