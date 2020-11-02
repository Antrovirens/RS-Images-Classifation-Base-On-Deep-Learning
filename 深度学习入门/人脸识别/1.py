import torch as t
from torch.utils import data
import os
from PIL import Image
import numpy as np
from torchvision import transforms as T
from torch import nn
from torch.autograd import Variable
from torch.optim import Adam
from torchvision.utils import make_grid
from torch.utils.data import DataLoader

transform = T.Compose(               #归一化
    [
        T.Resize(1000),
        T.CenterCrop(1000),
        T.ToTensor(),
        T.Normalize(mean=[.5,.5,.5],std=[.5,.5,.5])
    ]
)


#在这个class里重写你的数据集
class twoface(data.Dataset):
    def __init__(self,root,transforms=None):
        imgs = os.listdir(root)
        self.imgs = [os.path.join(root,img) for img in imgs]
        self.transforms = transforms

    def __getitem__(self, index):
        img_path = self.imgs[index]
        label = 1 if 'empty' in img_path.split('/')[-1] else 0  #定义标签：图片名中有label
        data = Image.open(img_path)
        if self.transforms:
            data = self.transforms(data)
        return data,label

    def __len__(self):
        return len(self.imgs)


dataset = twoface('./data1/',transforms=transform)       #transform 用在这里
data_loader_train = t.utils.data.DataLoader(dataset=dataset,
                                            batch_size=1,   #batch_size 要=1
                                            shuffle=True,
                                            num_workers=0)

data_loader_test = t.utils.data.DataLoader(dataset=dataset,
                                            batch_size=1,
                                            shuffle=True,
                                            num_workers=0)


class Model(t.nn.Module):
    def __init__(self):
        super(Model, self).__init__()
        self.conv1 = t.nn.Sequential(t.nn.Conv2d(3, 6, kernel_size=20, stride=10, padding=0),  #模型这块如果你图片格式不对的话要重新算
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

model = Model().cuda()
print(model)

cost = t.nn.CrossEntropyLoss()
optimizer = t.optim.Adam(model.parameters())
n_epochs = 5

for epoch in range(n_epochs):
    running_loss = 0.0
    running_correct = 0
    print("Epoch {}/{}".format(epoch, n_epochs))
    print("-" * 10)

    for datas in data_loader_train:
        realone,label = datas
        realone, label = Variable(realone).cuda(), Variable(label).cuda()
        output = model(realone)
        _,pred = t.max(output.data,1)
        optimizer.zero_grad()
        loss = cost(output, label)
        loss.backward()
        optimizer.step()
        running_loss += loss.data[0]
        running_correct += t.sum(pred == label)

        testing_correct = 0
        for datak in data_loader_test:
            X_test, y_test = datak
            X_test, y_test = Variable(X_test).cuda(), Variable(y_test).cuda()
            outputs = model(X_test)
            _, pred = t.max(outputs.data, 1)
            testing_correct += t.sum(pred == y_test.data)
        print(
            "Loss is:{:.4f}, Train Accuracy is:{:.4f}%, Test Accuracy is:{:.4f}".format(running_loss / len(dataset),
                                                                                        100 * running_correct / len(
                                                                                            dataset),
                                                                                        100 * testing_correct / len(
                                                                                            dataset)))
t.save(model, 'ifempty.pkl')