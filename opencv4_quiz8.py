import cv2 as cv
import numpy as np
# 读取图像 转灰度 得到二值图像 自适应阈值
image =cv.imread('water_coins.jpg')
gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
_,thresh = cv.threshold(gray,0,255,cv.THRESH_BINARY_INV + cv.THRESH_OTSU)

#kernel = cv.getStructuringElement(cv.MORPH_RECT,(3,3))
kernel = np.ones((3,3),np.uint8)
open = cv.morphologyEx(thresh,cv.MORPH_OPEN,kernel,iterations=2)
sure_bg = cv.dilate(open,kernel,iterations=5)
#cv.imshow('dilate',sure_bg)
dist_transform = cv.distanceTransform(open,cv.DIST_L2,5)
ret,sure_fg=cv.threshold(dist_transform,0.7*dist_transform.max(),255,cv.THRESH_BINARY)
#cv.imshow('distanceTransform',sure_fg)
surface_fg = np.uint8(sure_fg)
unknown = cv.subtract(sure_bg, surface_fg)
#cv.imshow('unknown',unknown)
ret,makers = cv.connectedComponents(surface_fg)
makers += 1
makers[unknown == 255] =0
makers = cv.watershed(image,makers)
#分水岭 边缘线标记为红色
image[makers == -1] = [0,0,255]
cv.imshow('result',image)
cv.waitKey(0)
cv.destroyAllWindows()
