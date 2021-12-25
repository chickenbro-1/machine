'''
3.实现对视频的动画效果实时渲染
先对 图像进行中值滤波，消除原图像的噪声
在对 图像的边界进行检测，
然后 设置结构元素，对边界进行膨胀，对边缘值进行缩放
对非边缘图像处理
先使用双边滤波 再抹除细节
合并 非边缘图像和边缘，返回结果
wangziheng
'''
import cv2
import numpy as np
def cartoon(image):
    #确定并膨胀（dilate）图像边界
    imgmedian = cv2.medianBlur(image,7) #消除噪声
    edges = cv2.Canny(imgmedian,80,130) #用Canny算法检测边缘
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(4,4)) #设置结构元素（数字越大越模糊）
    edges = cv2.dilate(edges,kernel,iterations=1) #膨胀边界 （膨胀次数越大 效果越明显）

    #缩放边缘值为1 转换类型

    edges = edges / 255
    edges = 1 - edges
    edgesf = edges.astype('float')
    edgesf = cv2.blur(edgesf,(3,3)) #均值滤波

    # 确定区域颜色 进行粗化处理
    imgBF = cv2.bilateralFilter(image,9,150,150)
    result = imgBF /25 # 抹除细节
    result = result.astype('uint8')
    result = result*25 # 数值越大 卡通效果越明显 色块越大

    result = result.astype('float')
    cannyChannels = cv2.merge([edgesf,edgesf,edgesf]) #图像多通道合并
    result = np.multiply(result,cannyChannels)
    result = result.astype('uint8')
    return result

cap = cv2.VideoCapture(0)
while(1):
    ret, frame = cap.read()
    ce = cartoon(frame)
    cv2.imshow("capture", ce)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

