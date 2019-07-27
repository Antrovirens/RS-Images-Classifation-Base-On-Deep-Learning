#
# pytorch mnist.py
# @author bulbasaur
# @description
# @created 2019-07-26T16:27:57.935Z+08:00
# @last-modified 2019-07-27T19:53:01.562Z+08:00
#
"""docstring
fucking PEP8
"""

import torch
import numpy
import matplotlib.pyplot as plt
from torchvision import datasets, transforms, utils
from torch.autograd import Variable


class Model(torch.nn.Module):
    def __init__(self):
        super(Model, self).__init__()
        self.conv1 = torch.nn.Sequential(
            torch.nn.Conv2d(1, 64, kernel_size=3, stride=1, padding=1),
            torch.nn.ReLU(),
            torch.nn.Conv2d(64, 128, kernel_size=3, stride=1, padding=1),
            torch.nn.ReLU(), torch.nn.MaxPool2d(stride=2, kernel_size=2))

        self.dense = torch.nn.Sequential(torch.nn.Linear(14 * 14 * 128, 1024),
                                         torch.nn.ReLU(),
                                         torch.nn.Dropout(p=0.5),
                                         torch.nn.Linear(1024, 10))

    def forward(self, x):
        x = self.conv1(x)
        x = x.view(-1, 14 * 14 * 128)
        x = self.dense(x)
        return x

 
TRANSFORM = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5])
])

DATA_TRAIN = datasets.MNIST(root='C:/Users/sheld/Desktop/data/',
                            transform=TRANSFORM,
                            train=True,
                            download=False)
DATA_TEST = datasets.MNIST(root='C:/Users/sheld/Desktop/data/',
                           transform=TRANSFORM,
                           train=False)

DATA_LOADER_TRAIN = torch.utils.data.DataLoader(
    dataset=DATA_TRAIN, batch_size=64, shuffle=True)  # shuffle：装载时随机顺序
DATA_LOADER_TEST = torch.utils.data.DataLoader(dataset=DATA_TEST,
                                               batch_size=64,
                                               shuffle=True)  # shuffle：装载时随机顺序


# print(iter(DATA_LOADER_TRAIN))
# print(DATA_TRAIN)
# IMAGES, LABELS = next(iter(DATA_LOADER_TRAIN))
# IMG = utils.make_grid(IMAGES)

# IMG = numpy.transpose(IMG, (1, 2, 0))
# STD = [0.5, 0.5, 0.5]
# MEAN = [0.5, 0.5, 0.5]

# IMG = IMG * STD + MEAN
# # print([labels[i] for i in range(64)])
# plt.imshow(IMG, cmap='gray')

model = Model()
cost = torch.nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters())

#print(model)

n_epochs = 5

for epoch in range(n_epochs):
    running_loss = 0.0
    running_correct = 0
    print('Epoch {}/{}'.format(epoch, n_epochs))
    print('-' * 10)
    for DATA in DATA_LOADER_TRAIN:
        X_train, Y_train = DATA
        X_train, Y_train = Variable(X_train), Variable(Y_train)
        Outputs = model(X_train)
        _, pred = torch.max(Outputs.data, 1)
        optimizer.zero_grad()
        loss = cost(Outputs, Y_train)

        loss.backward()
        optimizer.step()
        running_loss += loss.data[0]
        running_correct += torch.sum(pred == Y_train.data)

    test_correct = 0
    for DATA in DATA_LOADER_TEST:
        X_test, Y_test = DATA
        X_test, Y_test = Variable(X_test), Variable(Y_test)
        Outputs = model(X_test)
        _, pred = torch.max(Outputs.data, 1)
        test_correct += torch.sum(pred == Y_test.data)

    print('Loss is :{:4f}, Train Accuracy is:{:4f}%, Test Accuracy is:{:4f}'.
          format(running_loss / len(DATA_TRAIN), 100 * running_correct /
                 len(DATA_TRAIN), 100 * test_correct) / len(DATA_TEST))
