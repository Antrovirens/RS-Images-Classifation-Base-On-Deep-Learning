# Python 神经网络编程
Tariq rashid[著] 中国公信出版社 中国邮电出版社

## 第一章 神经神经网络如何工作

### 简单的分类器

```
A = 0.1
L = 0.5 #预设的初始值 # 进行简单的拟合  一个可循环的过程
for data in datas:
    E = data[1] - A * data[0] + data[1] / 10
    dA = L * (E / data[0])
    A = A + dA
```
