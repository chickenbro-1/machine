import cv2 as cv
if __name__ == '__main__':
    image = cv.imread('shape.png')
    gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    ret,binary = cv.threshold(gray,150,255,cv.THRESH_BINARY_INV+cv.THRESH_OTSU)
    contours, hierarchy = cv.findContours(binary, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    res = image.copy()
    for i in range(len(contours)):
        approx = cv.approxPolyDP(contours[i], 2, closed=True)
        val ,cx,cy = approx.shape[:3]
        if hierarchy[0][i][3] != -1:
            continue
        elif hierarchy[0][i][2] != -1:
            print('contours{} is a ring'.format(i+1))
        else:
            if val == 3:
                print('contours{} is a riangle'.format(i+1))
            elif val == 4:
                print('contours{} is a Rectangle'.format(i+1))
            elif val == 5:
                print('contours{} is a pentagon'.format(i+1))
            elif val == 6:
                print('contours{} is a hexagon'.format(i+1))
            elif val == 10:
                print('contours{} is a star'.format(i+1))
            else:
                print('contours{} is a circle'.format(i+1))


