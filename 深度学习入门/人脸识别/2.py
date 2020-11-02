from pylab import plt
import torch as t
from torch.autograd import Variable
from torchvision.utils import make_grid
from PIL import Image
import numpy as np
import os

class Model(t.nn.Module):  #如果不把这些乱七八糟的class和transform 重写一遍会出错

    def __init__(self):
        super(Model, self).__init__()
        self.conv1 = t.nn.Sequential(t.nn.Conv2d(3, 6, kernel_size=20, stride=10, padding=0),
                                         t.nn.ReLU(),
                                         t.nn.Conv2d(6, 10, kernel_size=6, stride=1, padding=0),
                                         t.nn.ReLU(),
                                         t.nn.Conv2d(10, 16, kernel_size=5, stride=1, padding=0),
                                         t.nn.ReLU(),
                                         t.nn.MaxPool2d(stride=5, kernel_size=5))
        #
        self.dense = t.nn.Sequential(t.nn.Linear(18 * 18 * 16, 33),
                                     t.nn.ReLU(),
                                     t.nn.Linear(33, 2)
                                     )

    def forward(self, x):
        x = self.conv1(x)
        x = x.view(-1,18 * 18 * 16)
        x = self.dense(x)
        return x




lst = os.listdir('./recv/')
flag = 0
for i in range(len(lst)):

    img=Image.open('./recv/' + lst[i])

    from torchvision import transforms as T
    trans= T.Compose(
        [
            T.Resize(1000),
            T.CenterCrop(1000),
            T.ToTensor(),
            T.Normalize(mean=[.5,.5,.5],std=[.5,.5,.5])
        ]
    )

    a=trans(img)
    b = a.numpy()
    x = np.array([b])
    y = t.Tensor(x)
    fix_noise = Variable(y)
    fix_noise = fix_noise.cuda()
    net = t.load('ifempty.pkl')
    output = net(fix_noise)
    _,pred = t.max(output.data,1)

    if pred.data.item() == 1:
        print('空')
        flag = 1
    else:
        flag = 0

    if flag == 0:
        netj = t.load('ifzwh.pkl')
        output2 = netj(fix_noise)
        _, pred2 = t.max(output2.data, 1)
        if pred2.data.item() == 0:
            print('xxx')
        else:
            print('其他人')