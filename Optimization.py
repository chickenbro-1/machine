import cv2 as cv
import numpy as np

def judge_shape(val):
    if val == 3:
        cv.putText(image, text='Triangle', org=center, fontFace=1, fontScale=5, color=(0, 0, 0))
    elif val == 4:
        cv.putText(image, text='Rectangle', org=center, fontFace=1, fontScale=5, color=(0, 0, 0))
    elif val == 5:
        cv.putText(image, text='pentagon', org=center, fontFace=1, fontScale=5, color=(0, 0, 0))
    elif val == 6:
        cv.putText(image, text='hexagon', org=center, fontFace=1, fontScale=5, color=(0, 0, 0))
    elif val == 10:
        cv.putText(image, text='star', org=center, fontFace=1, fontScale=5, color=(0, 0, 0))
    else:
        cv.putText(image, text='circle', org=center, fontFace=1, fontScale=5, color=(0, 0, 0))
def get_center(contours):
    min_rect = cv.minAreaRect(contours)
    center = (int(min_rect[0][0]),int(min_rect[0][1]))
    return center

if __name__ == '__main__':
    image = cv.imread('shape.png')
    gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    ret,binary = cv.threshold(gray,150,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
    contours, hierarchy = cv.findContours(binary, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    res = image.copy()

    for i in range(len(contours)):
        approx = cv.approxPolyDP(contours[i], 2, closed=True)
        val ,cx,cy = approx.shape[:3]

        cv.drawContours(res, [approx], 0, (200, 0, 255), 3)
        center = get_center(contours[i])

        if hierarchy[0][i][3] != -1:
            continue
        elif hierarchy[0][i][2] != -1:
            cv.putText(image, text='ring', org=center, fontFace=1, fontScale=5, color=(0, 0, 0))
        else:
            judge_shape(val)
            cv.imshow('ApproxPolyDP', image)
    cv.waitKey(0)
    cv.destroyAllWindows()
