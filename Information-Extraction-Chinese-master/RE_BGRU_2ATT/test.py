import numpy as np
#train_y = np.load('./data/train_y.npy')
#train_word = np.load('./data/train_word.npy')
#train_pos1 = np.load('./data/train_pos1.npy')
#train_pos2 = np.load('./data/train_pos2.npy')
#print(type(train_y))
#print(train_y[0])
#print(len(train_y[0]))
#<class 'numpy.ndarray'>
#ndarray对象是用于存放同类型元素的多维数组
import tensorflow as tf
c=tf.constant(value=1)
# assert c.graph is tf.get_default_graph()
#print(c.graph)
#print(tf.get_default_graph())
# with 语句适用于对资源进行访问的场合，
# 确保不管使用过程中是否发生异常都会执行必要的“清理”操作，
# 释放资源，比如文件使用后自动关闭、线程中锁的自动获取和释放等。
with tf.variable_scope("foo"):
    with tf.variable_scope("bar"):
        v = tf.get_variable("v", [1])
        assert v.name == "foo/bar/v:0"
        print(v.name)
#python assert断言是声明其布尔值必须为真的判定，如果发生异常就说明表达示为假。
#共享variable的基本示例：
with tf.variable_scope("foo"):
    v = tf.get_variable("v", [1])
with tf.variable_scope("foo", reuse=True):
    v1 = tf.get_variable("v", [1])
assert v1 == v
import datetime
time_str = datetime.datetime.now().isoformat()
print(time_str)