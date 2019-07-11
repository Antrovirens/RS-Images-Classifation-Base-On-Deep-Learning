import numpy as np
import matplotlib.pyplot as plt

data_file = open("mnist_train_100.csv",'r')
data_list = data_file.readlines()
data_file.close()
##print(data_list[5])

all_values = data_list [5].split(',')
##image_aarray = np.asfarray(all_values[1:]).reshape((28,28))
##plt.imshow(image_aarray, cmap = 'Greys', interpolation = 'None')
##plt.show()
scaled_input = (np.asfarray(all_values[1:]) / 255.0 * 0.99) + 0.01
##print(scaled_input)
onodes = 10
targets = np.zeros(onodes) + 0.01
targets[int(all_values[0])] = 0.99
print(targets)
