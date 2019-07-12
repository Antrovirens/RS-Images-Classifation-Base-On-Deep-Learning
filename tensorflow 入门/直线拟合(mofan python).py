import tensorflow as tf
import numpy as np

# 使用 NumPy 生成假数据(phony data), 总共 100 个点.
x_data = np.float32(np.random.rand(2, 100)) # 随机输入
y_data = np.dot([0.100, 0.200], x_data) + 0.300  #np.dot 向量点乘

# 构造一个线性模型
# 
b = tf.Variable(tf.zeros([1]))
W = tf.Variable(tf.random_uniform([1, 2], -1.0, 1.0))
y = tf.matmul(W, x_data) + b

# 最小化方差
loss = tf.reduce_mean(tf.square(y - y_data))
optimizer = tf.train.GradientDescentOptimizer(0.5)
train = optimizer.minimize(loss)

# 初始化变量
init = tf.global_variables_initializer()

# 启动图 (graph)
sess = tf.Session()
sess.run(init)

# 拟合平面
for step in range(0, 201):   #py37
    sess.run(train)
    if step % 20 == 0:
        print(step, sess.run(W), sess.run(b))   #print()

# 得到最佳拟合结果 W: [[0.100  0.200]], b: [0.300]



#输出结果为：
#0 [[-0.01733944 0.58398485]] [0.38418597]
#20 [[0.07247503 0.28437114]] [0.26719967]
#40 [[0.10012777 0.22671382]] [0.284668]
#60 [[0.10250892 0.20942475]] [0.29321364]
#80 [[0.10157281 0.20359424]] [0.2970676]
#100 [[0.10077173 0.20143798]] [0.29874715]
#120 [[0.10034854 0.2005909 ]] [0.29946762]
#140 [[0.100152 0.20024626]] [0.29977435]
#160 [[0.10006522 0.20010337]] [0.29990453]
#180 [[0.10002777 0.20004351]] [0.29995963]
#200 [[0.10001177 0.20001836]] [0.29998294]

#随着总数目的提高，拟合的结果也随之接近于真实值
#这是从官网上找出来的一个例子，由于中文论坛的版本很老，长期没有更新，里面的bug也是一堆: tf中文论坛的get start guide。经过格式修改后只剩下一个警告：

#WARNING:tensorflow:From C:\Users\sheld\Anaconda3\envs\env_tf\lib\site-packages\tensorflow\python\framework\op_def_library.py:263: colocate_with (from tensorflow.python.framework.ops) is deprecated and will be removed in a future version.
#Instructions for updating:
#Colocations handled automatically by placer.
