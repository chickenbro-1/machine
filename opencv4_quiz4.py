'''
1.提取图像的连通域
wangziheng
'''
import numpy
import cv2
import numpy as np
def generate_random_color():
    return numpy.random.randint(0,256,3)
def fill_color(img1,img2):
    h,w = img1.shape
    res = np.zeros((h,w,3),img1.dtype)
    random_color = {}
    for c in range(1,count):
        random_color[c] = generate_random_color()
    for i in range(h):
        for j in range(w):
            item = img2[i][j]
            if item == 0 :
                pass
            else:
                res[i,j,:] =random_color[item]
    return res
file_name = 'rice2.png'
#图像转灰度
rice = cv2.imread(file_name,cv2.IMREAD_GRAYSCALE)
#转换二值图像
rice_BW = cv2.threshold(rice,50,255,cv2.THRESH_BINARY)
#统计连通域
count,res =cv2.connectedComponents(rice_BW[1],ltype=cv2.CV_16U)
#给连通域填充颜色
result = fill_color(rice,res)
input()
cv2.imshow('origin',rice)
cv2.imshow('Result',result)
cv2.waitKey(0)
cv2.destroyAllWindows()