import numpy as np
import matplotlib.pyplot as plt

##file_object = open('classification cal sample.txt')
###不要把open放在try中，以防止打开失败，那么就不用关闭了
##try:
##    #file_context = file_object.read()
##    #file_context是一个string，读取完后，就失去了对test.txt的文件引用
##    file_context = open(file).read().splitlines() 
##    #file_context是一个list，每行文本内容是list中的一个元素
##finally:
##    file_object.close()
###除了以上方法，也可用with、contextlib都可以打开文件，且自动关闭文件，
###以防止打开的文件对象未关闭而占用内存file_object = open('test.txt','rU')

datas = []  #初始化
file_object = open('classification cal sample.txt','r')
try:
    for line in file_object:
        # do_somthing_with(line) #line带"\n"
        line = line.replace(',',' ').replace('\n','')  #去除无用字符
        num = list(map(float,line.split()))  # 把空白行分离开，映射到表结构 参见python自带函数map() 
        datas.append(num) #后续拓展表
        #print(datas)
finally:
    file_object.close() #文件流关闭

plt.figure(num = 2019, figsize = (5, 5)) #初始化图形，指定figure的编号并指定figure的大小
for data in datas:
    a = data[0] # xi
    b = data[1] # yi
    k = b / a
    x = np.linspace(0, a, int(50 * a))
    y = k * x
    plt.plot(x,y,color = 'black', linewidth = 1.0, linestyle = '--') #定义线性

# y = A * x    E = dA * x     dA= L * (E / x)
A = 0.1
L = 0.5 #预设的初始值
# 进行简单的拟合  一个可循环的过程
for data in datas:
    E = data[1] - A * data[0] + data[1] / 10
    dA = L * (E / data[0])
    A = A + dA
    
x = np.linspace(0, 5, 250) #绘制图形
y = A * x
plt.plot(x,y,color = 'green', linewidth = 1.0)
plt.show()
