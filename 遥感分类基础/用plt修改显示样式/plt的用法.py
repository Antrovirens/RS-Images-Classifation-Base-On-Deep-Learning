

import numpy as np
import matplotlib.pyplot as plt

for i in range(0,15):
    # 1 柱状图
    dateOne = np.zeros([2])
    dateOne[0] = i;
    dateOne[1] = i;
    y = np.zeros([2])
    y[0] = 10
    y[1] = 20
    plt.plot(dateOne,y,'r',lw=8)
plt.show()


#Tanh Function
plt.figure()
x1 = np.linspace(-10, 0, 500)
y1 = 0 * x1
plt.plot(x1, y1, c= 'blue')


x2 = np.linspace(0, 10, 500)
y2 = x2
plt.plot(x2, y2, c= 'blue')

plt.grid(True, linestyle = '--')
plt.xlabel('input')
plt.ylabel('output')
plt.title('ReLU Function',color = 'blue')
plt.show()

###Tanh Function
##plt.figure()
##x = np.linspace(-10, 10, 1000)
###x = np.arange(-10,10)
##y1 = (np.exp(x) - np.exp(-x)) / (np.exp(x) + np.exp(-x))
##plt.plot(x, y1, c= 'blue')
##plt.grid(True, linestyle = '--')
##plt.xlabel('input')
##plt.ylabel('output')
##plt.title('Tanh Function',color = 'blue')
##plt.show()


###Sigmoid Function
##plt.figure()
##x = np.linspace(-10, 10, 1000)
###x = np.arange(-10,10)
##y1 = 1 / (1 + np.exp(-x))
##plt.plot(x, y1, c= 'blue')
##plt.grid(True, linestyle = '--')
##plt.xlabel('input')
##plt.ylabel('output')
##plt.title('Sigmoid Function',color = 'blue')
##plt.show()

##plt.figure()
##x1 = [0,1]
##y1 = [0,1]
##x2 = [1,0]
##y2 = [0,1]
##plt.scatter(x1, y1, c = 'red' )
##plt.scatter(x2, y2, c = 'green')
##x = np.linspace(-0.5, 1.5, 50)
##
##y1 = -1 * x + 0.5
##y2 = -1 * x + 1.5
##
##plt.plot(x, y1, c= 'blue')
##plt.plot(x, y2, c= 'blue')
##plt.show()
##x = np.linspace(-1, 1, 50)
##
##
### figure 1
##y1 = 2 * x + 1
##plt.figure()
##plt.plot(x, y1)
##
##
### figure 2
##y2 = x**2
##plt.figure()
##plt.plot(x, y2)
##
##
### figure 3，指定figure的编号并指定figure的大小, 指定线的颜色, 宽度和类型
###一个坐标轴上画了两个图形
##y2 = x**2
##plt.figure(num = 5, figsize = (4, 4))
##plt.plot(x, y1)
##plt.plot(x, y2, color = 'red', linewidth = 1.0, linestyle = '--')
##plt.show()
