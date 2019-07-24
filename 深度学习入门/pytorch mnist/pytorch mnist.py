import torch
import numpy
import matplotlib.pyplot as plt
from torchvision import datasets, transforms
from torch.autograd import Variable

print('now loading data...')
transform = transforms.Compose([transforms.ToTensor(), transforms.Normalize(mean = [0.5, 0.5, 0.5], std = [0.5, 0.5, 0.5])])

data_train = datasets.MNIST(root = './data/', transform = transform,
                            train = True, download = False)
data_test = datasets.MNIST(root = './data/', transform = transform,
                           train = False)

data_loader_train = torch.utils.data. DataLoader(dataset = data_train, batch_size = 64, shuffle = True) #shuffle：装载时随机顺序
data_loader_test = torch.utils.data.DataLoader(dataset = data_test, batch_size = 64, shuffle = True) #shuffle：装载时随机顺序
print('loading success')
print(iter(data_loader_train))
print(data_train)
images, labels = next(iter(data_loader_train))
img = torchvision.utils.make_grad(images)

img = numpy.transpose(img, (1,2,0))
std = [0.5, 0.5, 0.5]
mean = [0.5, 0.5, 0.5]

img = img * std + mean
#print([labels[i] for i in range(64)])
plt.imshow(img, cmap = 'gray')
