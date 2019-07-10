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

expit函数，也称为logistic sigmoid函数，定义为expit（x）= 1 /（1 + exp（-x））。 它是logit函数的反函数。  
参数：x:ndarray  
　　　ndarray的元素应用expit函数  
输出：out:ndarray  
　　　与x形状相同的ndarray,它的元素是对应元素输入expit函数的结果  
```
>>> import numpy as np
>>> from scipy.special import expit

>>> expit([-np.inf, -1.5, 0, 1.5, np.inf])
array([ 0.        ,  0.18242552,  0.5       ,  0.81757448,  1.        ])
```
```
#scipy.special for the sigmoid function expit()
import scipy.special
self.activation_function = lambda x: scipy.special.expit(x)
```
