'''
2.利用形态学操作 对图像进行边缘检测
wangziheng
'''
import cv2
import numpy as np
from matplotlib import pyplot as plt
file_name = 'rice2.png'
#生成5*5矩形结构
kernel = cv2.getStructuringElement(0,(5,5))
#读取图像，转灰度
image = cv2.imread(file_name,cv2.IMREAD_GRAYSCALE)
#对图像进行二值化
keys = cv2.threshold(image,130,255,cv2.THRESH_BINARY)[1]
#图形学梯度运算
gradient_image = cv2.morphologyEx(keys,cv2.MORPH_GRADIENT,kernel)
str = cv2.getStructuringElement(0,(3,3))
dilate_image = cv2.dilate(keys,str)
erode_image = cv2.erode(keys,str)
sub_image = dilate_image - erode_image
cv2.imshow('gradient_image',gradient_image)
cv2.imshow('dilate_erode_image',sub_image)
cv2.waitKey(0)
cv2.destroyAllWindows()