import numpy as np
import tensorflow as tf

np_arr = np.array([[1,2], [3,4] ,[5,6]])

# mean operation using numpy
print "numpy_mean"
print "rowise_mean : ", np.mean(np_arr, 1)
print "columwise_mean : ", np.mean(np_arr, 0)
print "total_mean : ", np.mean(np_arr)

# mean operation using tensorflow
mean1 = tf.reduce_mean(np_arr, 1)
mean2 = tf.reduce_mean(np_arr, 0)
mean3 = tf.reduce_mean(np_arr)

with tf.Session() as sess:
    print "tf.reduce_mean...."
    print "rowise_mean : ", sess.run(mean1)
    print "colimumnise_mean : ", sess.run(mean2)
    print "total_mean : ", sess.run(mean3)
    
c = np.array([[1.,2], [3.,4] ,[5.,6]])
# mean operation using tensorflow
mean1 = tf.reduce_mean(c, 1)
mean2 = tf.reduce_mean(c, 0)
mean3 = tf.reduce_mean(c)
with tf.Session() as sess:
    print "tf.reduce_mean...."
    print "rowise_mean : ", sess.run(mean1)
    print "colimumnise_mean : ", sess.run(mean2)
    print "total_mean : ", sess.run(mean3)
    
d = [[1.,2], [3.,4] ,[5.,6]]
# mean operation using tensorflow
mean1 = tf.reduce_mean(d, 1)
mean2 = tf.reduce_mean(d, 0)
mean3 = tf.reduce_mean(d)
with tf.Session() as sess:
    print "tf.reduce_mean...."
    print "rowise_mean : ", sess.run(mean1)
    print "colimumnise_mean : ", sess.run(mean2)
    print "total_mean : ", sess.run(mean3)
    