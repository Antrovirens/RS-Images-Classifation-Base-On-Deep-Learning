# Python 神经网络编程
Tariq rashid[著] 中国公信出版社 中国邮电出版社

### 简单的分类器

```
A = 0.1
L = 0.5 #预设的初始值 # 进行简单的拟合  一个可循环的过程
for data in datas:
    E = data[1] - A * data[0] + data[1] / 10
    dA = L * (E / data[0])
    A = A + dA
```

### 神经网络如何工作


### 神经网络搭建

```
#scipy.special for the sigmoid function expit()
import scipy.special
self.activation_function = lambda x: scipy.special.expit(x)
```
