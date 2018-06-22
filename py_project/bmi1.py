import numpy as np
import pandas as pd
import tensorflow as tf

csv = pd.read_csv("datasets/bmi.csv")
print(csv)

bclass = {"this":[1,0,0], "normal":[0,1,0], "fat":[0,0,1] }
csv["label_pat"] = csv["label"].apply(lambda x:np.array(bclass[x]))
test_csv = csv[15000:20000]
text_pat = text_csv[["weight","height"]]
text_ans = list(test_csv["label_pat"])
x = tf.placeholder(tf.float32, [None, 2])
y = tf.placeholder(tf.float32, [None, 3])
W = tf.Variable(tf.zeros([2,3]))
b = tf.Variable(tf.zeros([3]))
y = tf.nn.softmax(tf.matmul(x, W) + b)
cross_entropy = -tf.reduce_sum(y_ * tf.log(y))
# opti