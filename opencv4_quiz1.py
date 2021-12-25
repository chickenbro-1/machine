import cv2 as cv
import numpy as np
def add_noisy(image, n=10000):
    result = image.copy()
    w, h = image.shape[:2]
    for i in range(n):
        # 分别在宽和高的范围内生成一个随机值，模拟代表x, y坐标
        x = np.random.randint(1, w)
        y = np.random.randint(1, h)
        if np.random.randint(0, 2) == 0:
            # 生成白色噪声（盐噪声）
            result[x, y] = 0
        else:
            # 生成黑色噪声（椒噪声）
            result[x, y] = 255
    return result
if __name__ == '__main__':
    file_name = "123.jpg"
    img = cv.imread(file_name)
    image_noisy = add_noisy(img, 10000)
    cv.imshow('img_noisy',image_noisy)
    img_3 = cv.medianBlur(image_noisy,3)
    img_9 = cv.medianBlur(image_noisy,9)
    cv.imshow('img_3',img_3)
    cv.imshow('img_9',img_9)
    cv.waitKey(0)
    cv.destroyAllWindows()
