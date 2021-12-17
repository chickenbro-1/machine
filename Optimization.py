import numpy
"""
精确搜索方法 分割方法 二分法
"""
def bisection(start,end,func,dfunc,epsilon=1e-4,appendix=False):
    '''Bisection Method for exact line search'''
    if appendix == True:
        start0, end0 = start, end   # save initial search interval
    iterNum = 0
    while True:
        # compute middle point and its derivation
        middle = (start + end) / 2
        dfMiddle = dfunc(middle)
        if abs(dfMiddle) < epsilon or end - start < epsilon:
            break
        # update start or end point
        elif dfMiddle > 0:
            end = middle
        else:
            start = middle
        iterNum += 1
    minPoint = middle
    minValue = func(minPoint)
    if appendix == True:
        print("方法：二分法\n")
        print("初始区间：[%.2f, %.2f]; 最终区间：[%f, %f]" % (start0,end0,start,end))
        print("极小值点：%.4f; 极小值：%.4f; 迭代次数：%d" % (minPoint,minValue,iterNum))
    return minPoint, minValue, iterNum
"""
精确搜索方法 分割方法 黄金分割法
"""

def goldenSection(start,end,func,epsilon=1e-4,appendix=False):
    '''Golden Section Method for exact line search'''

    if appendix == True:
        start0, end0 = start, end   # save initial search interval

    # find two insertion points using fixed ratio
    from math import sqrt
    ratio = sqrt(5) / 2 - 0.5
    intervalLen = end - start
    middleL = start + (1 - ratio) * intervalLen
    middleR = start + ratio * intervalLen

    iterNum = 0
    while intervalLen >= epsilon:
        # update start or end point and two insertion points
        if func(middleL) > func(middleR):
            start = middleL
            intervalLen = end - start
            middleL = middleR
            middleR = start + ratio * intervalLen
        else:
            end = middleR
            intervalLen = end - start
            middleR = middleL
            middleL = start + (1 - ratio) * intervalLen
        iterNum += 1
    minPoint = (start + end) / 2
    minValue = func(minPoint)
    if appendix == True:
        print("方法：黄金分割法\n")
        print("初始区间：[%.2f, %.2f]; 最终区间：[%f, %f]" % (start0,end0,start,end))
        print("极小值点：%.4f; 极小值：%.4f; 迭代次数：%d" % (minPoint,minValue,iterNum))
    return minPoint, minValue, iterNum
"""
精确搜索方法 插值法 牛顿法
"""
def newton(x0,func,dfunc,ddfunc,epsilon=1e-4,appendix=False):
    '''Newton Method for exact line search'''
    if appendix == True:
        initial = x0   # save initial point
    # make sure that conditions of loop are available
    # also make sure no loop if df(x0) = 0
    x1 = x0
    diffX = epsilon + 1
    iterNum = 0
    while diffX >= epsilon and abs(dfunc(x1)) >= epsilon:
        x1 = x0 - dfunc(x0)/ddfunc(x0)
        diffX = abs(x1 - x0)
        x0 = x1
        iterNum += 1

    minPoint = x0
    minValue = func(x0)
    if appendix == True:
        print("方法：一点二次插值法（牛顿法）\n")
        print("初始点：%.2f" % (initial))
        print("极小值点：%.4f; 极小值：%.4f; 迭代次数：%d" % (minPoint,minValue,iterNum))
    return minPoint, minValue, iterNum
"""
非精确搜索方法 
"""
def inexactLineSearch(func,dfunc,start=0,end=1e10,rho=0.1,sigma=0.4,criterion='Wolfe Powell',appendix=False):
    '''Inexact Line Search Method with four available criterion:
    1.Armijo Goldstein
    2.Wolfe Powell
    3.Strong Wolfe Powell
    4.Simple
    '''

    if appendix == True:
        alpha0 = (start + end) / 2   # save initial point

    # reduce unnecessary caculations in loop
    f0, df0 = func(0), dfunc(0)
    rhoDf0 = rho * df0
    boundary3 = sigma * df0
    boundary4 = sigma * abs(df0)

    iterNum = 0
    while True:
        alpha = (start + end) / 2
        boundary1 = f0 + rhoDf0 * alpha
        boundary2 = f0 + boundary3 * alpha
        fAlpha, dfAlpha = func(alpha), dfunc(alpha)

        # different criterions have same condition1 to avoid too large alpha
        condition1 = (fAlpha <= boundary1)
        # different criterions have different condition2 to avoid too small alpha
        if criterion == 'Armijo Goldstein':
            condition2 = (fAlpha >= boundary2)
        elif criterion == 'Wolfe Powell':
            condition2 = (dfAlpha >= boundary3)
        elif criterion == 'Strong Wolfe Powell':
            condition2 = (abs(dfAlpha) <= boundary4)
        else:
            condition2 = True

        # update start or end point or stop iteration
        if condition1 == False:
            end = alpha
        elif condition2 == False:
            start = alpha
        else:
            minPoint = alpha
            minValue = fAlpha
            break
        iterNum += 1

    if appendix == True:
        print("方法：非精确线搜索；准则：%s\n" % criterion)
        print("初始点：%.2f" % (alpha0))
        print("停止点：%.4f; 停止点函数值：%.4f; 迭代次数：%d" % (minPoint,minValue,iterNum))
    return minPoint, minValue, iterNum

def f(x, y):
    return (1 - x) ** 2 + 100 * (y - x * x) ** 2


def H(x, y):
    return np.matrix([[1200 * x * x - 400 * y + 2, -400 * x],
                      [-400 * x, 200]])


def grad(x, y):
    return np.matrix([[2 * x - 2 + 400 * x * (x * x - y)],
                      [200 * (y - x * x)]])




bisection(0,1,func,dfunc,1e-5,True)   # 二分法
goldenSection(0,1,func,1e-5,True)   # 黄金分割法
newton(0,func,dfunc,ddfunc,1e-5,True)   # 一点二次插值法（牛顿法）
inexactLineSearch(func,dfunc,appendix=True) # 非精确线搜索
import numpy as np
def f(x, y):
    return (1 - x) ** 2 + 100 * (y - x * x) ** 2
def H(x, y):
    return np.matrix([[1200 * x * x - 400 * y + 2, -400 * x],
                      [-400 * x, 200]])
def grad(x, y):
    return np.matrix([[2 * x - 2 + 400 * x * (x * x - y)],
                      [200 * (y - x * x)]])
def delta_newton(x, y):
    alpha = 1.0
    delta = alpha * H(x, y).I* grad(x, y)
    return delta
x = np.matrix([[-0.2],[0.3]])
tol = 0.00001
xv = [x[0, 0]]
yv = [x[1, 0]]
num = 0
for t in range(100):
    delta = delta_newton(x[0, 0], x[1, 0])
    if abs(delta[0, 0]) < tol and abs(delta[1, 0]) < tol:
        break
    x = x - delta
    xv.append(x[0, 0])
    yv.append(x[1, 0])
    num = num + 1
print(num)


