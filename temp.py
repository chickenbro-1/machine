import cv2 as cv


if __name__ == '__main__':
    image = cv.imread('shape.png')
    canny = cv.Canny(image, 80, 160, 3)
    kernel = cv.getStructuringElement(0, (3, 3))
    canny = cv.dilate(canny, kernel=kernel)
    contours, hierarchy = cv.findContours(canny, mode=0, method=2)
    print(hierarchy)
    for i in range(len(contours)):
        approx = cv.approxPolyDP(contours[i], 4, closed=True)
        val,cn,cm = approx.shape[:3]
        if hierarchy[0][i][3] != -1:
            pass
        elif hierarchy[0][i][2] != -1:
            print('contours is a ring')
        else:
            if val == 3:
                print('contours is a riangle')
            elif val == 4:
                print('contours is a Rectangle')
            elif val == 5:
                print('contours is a pentagon')
            elif val == 6:
                print('contours is a hexagon')
            elif val == 10:
                print('contours is a star')
            else:
                print('contours is a circle')

