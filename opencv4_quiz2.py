import cv2 as cv
file_name = 'noisy_123.jpg'
img =cv.imread(file_name)
#双边滤波
res1 = cv.bilateralFilter(img ,9,200,200)
cv.imshow('bilateral_filter',res1)
#高斯滤波
res2 = cv.GaussianBlur(img,(5,5),10,20)
cv.imshow('Gaussian_filter',res2)
cv.waitKey(0)
cv.destroyAllWindows()
