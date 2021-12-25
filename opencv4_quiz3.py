import cv2 as cv
file_name = '123.jpg'
image =cv.imread(file_name)
result_high = cv.Canny(image, 100, 200, apertureSize=3)
result_low = cv.Canny(image, 20, 40, apertureSize=3)

result_gauss = cv.GaussianBlur(image, (3, 3), 5)
result_gauss = cv.Canny(result_gauss, 100, 200, apertureSize=3)

cv.imshow('Result_high', result_high)
cv.imshow('Result_low', result_low)
cv.imshow('Result_gauss', result_gauss)
cv.waitKey(0)
cv.destroyAllWindows()
