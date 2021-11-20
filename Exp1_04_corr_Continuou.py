import matplotlib.pyplot as plt
import numpy as np

def rect_wave(x,c,c0): #起点为c0，宽度为c的矩形波
    if x>=(c+c0):
        r=0.0
    elif x<c0:
        r=0.0
    else:
        r=1
    return r
x1 = np.arange(-0.0001, 1.0, 0.001)
y1=np.array([rect_wave(t-1,0.99,-1.0) for t in x1])*2
plt.ylim(0,2)
plt.subplot(3,1,1)
plt.plot(x1,y1,color='red')
x2 =np.arange(-0.001, 2.0, 0.001)
y2 = x2
plt.subplot(3,1,2)
plt.plot(x2,y2,color='red')

print(len(y1))
print(len(y2))

x3 = np.arange(-0.0001,3.0, 0.001)
y3 = np.correlate(y1,y2)
print(len(y3))
input()
plt.subplot(3,1,3)
plt.plot(x3,y3,color='red')
plt.show()