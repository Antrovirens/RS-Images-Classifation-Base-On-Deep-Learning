import numpy as np
import scipy.special
#定义三层神经网络
class neuralNetwork:
    def __init__(self, inputnodes, hiddennodes, outputnodes, learningrate):
        self.inodes = inputnodes #输入层
        self.hnodes = hiddennodes #隐藏层
        self.onodes = outputnodes #输出层
        self.lr = learningrate
        #较为复杂的权重   中心值为0 标准差为传入节点数开方的倒数(-0.5次方) 的正态分布 
        self.wih = np.random.normal(0.0, pow(self.hnodes, -0.5), (self.hnodes, self.inodes))  #100 278
        self.who = np.random.normal(0.0, pow(self.onodes, -0.5), (self.onodes, self.hnodes))  #10 100

        self.activation_function = lambda x: scipy.special.expit(x)
        pass

    def train(self, inputs_list, targets_list):

        inputs = np.array(inputs_list, ndmin = 2).T  #278*1
        targets = np.array(targets_list, ndmin = 2).T # 10*1
        
        hidden_inputs = np.dot(self.wih, inputs) #100 1
        
        hidden_outputs = self.activation_function(hidden_inputs) #100 1

        final_inputs = np.dot(self.who, hidden_outputs) #10 1

        final_outputs = self.activation_function(final_inputs)  # 10 1

        output_errors = targets - final_outputs # 10 1

        hidden_errors = np.dot(self.who.T , output_errors) # 100 1
        #更新层之间的权重 dWij = alpha * Ek * S(Ok) * (1 - S(Ok)) * Oj.T
        self.who += self.lr * np.dot((output_errors * final_outputs * (1.0 - final_outputs)), np.transpose(hidden_outputs))
        self.wih += self.lr * np.dot((hidden_errors * hidden_outputs * (1.0 - hidden_outputs)), np.transpose(inputs))
        
        pass

    def query(self, inputs_list):

        inputs = np.array(inputs_list, ndmin = 2).T   
        hidden_inputs = np.dot(self.wih, inputs)
        hidden_outputs = self.activation_function(hidden_inputs)
        final_inputs = np.dot(self.who, hidden_outputs)
        final_outputs = self.activation_function(final_inputs)

        return final_outputs

#set number
input_nodes = 784
hidden_nodes = 100
output_nodes = 10

learning_rate = 0.3
#create instance of neural network
n = neuralNetwork(input_nodes, hidden_nodes, output_nodes, learning_rate)

#train the neural network
training_data_file = open("mnist_train.csv",'r')
training_data_list = training_data_file.readlines()
training_data_file.close()
i = 1
for record in training_data_list:
    all_values = record.split(',')
    inputs = (np.asfarray(all_values[1:]) / 255.0 * 0.99) + 0.01
    #print('正在训练第' + str(i) + '个')
    i += 1
    targets = np.zeros(output_nodes) + 0.01
    targets[int(all_values[0])] = 0.99   #1*10
    n.train(inputs, targets)
    pass
#print('训练结束\n')
#test the network

test_data_file = open("mnist_test.csv",'r')
test_data_list = test_data_file.readlines()
test_data_file.close()
score = 0
num = 0
for record in test_data_list:
    all_values = record.split(',')
##    image_aarray = np.asfarray(all_values[1:]).reshape((28,28))
##    plt.imshow(image_aarray, cmap = 'Greys', interpolation = 'None')
##    plt.show()
    correct_label = int(all_values[0])
    outputs = n.query((np.asfarray(all_values[1:]) / 255.0 * 0.99) + 0.01)
    label = np.argmax(outputs)
    #print('correct:' + str(correct_label) +' result:' + str(label))
    #下面是随便写的  凑合着看看
    if label == correct_label:
        score += 1
        num +=1
    else:
        num += 1
        pass
    pass
print('score:'+ str(score))
print('num:' + str(num))
print('rate:' + str(score/num))
