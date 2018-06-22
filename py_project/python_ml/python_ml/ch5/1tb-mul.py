# 1tb-mul.py

# $ mkdir log_dir
# $ python 1tb_mul.py

# $ tensorboard --logdir=log_dir
# 브라우저로 localhost:6006 으로 접속해서 확인

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'  # 아래 경고 메시지 안 나오게하는 설정
# I tensorflow/core/platform/cpu_feature_guard.cc:137] Your CPU supports instructions that this TensorFlow binary was not compiled to use: SSE4.2 AVX AVX2 FMA

import tensorflow as tf

# 데이터 플로우 그래프 구축하기 --- (※1)
a = tf.constant(20, name="a")
b = tf.constant(30, name="b")
mul_op = a * b
# 세션 생성하기 --- (※2)
sess = tf.Session()
# TensorBoard 사용하기 --- (※3)
# tf.train.SummaryWriter is deprecated, instead use tf.summary.FileWriter
# tw = tf.train.SummaryWriter("log_dir", graph=sess.graph)
tw = tf.summary.FileWriter("log_dir", graph=sess.graph)

# 세션 실행하기 --- (※4)
print(sess.run(mul_op))  # 600
