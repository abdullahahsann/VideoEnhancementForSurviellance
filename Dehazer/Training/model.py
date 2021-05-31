import tensorflow as tf
from tensorflow.keras.layers import *
from tensorflow.keras.models import Model

weight_decay = 1e-4

def dehazer_net():
    inputs = tf.keras.Input(shape = [480, 640, 3])     
    
    # Defining Layers
    conv1 = Conv2D(64,3,1,padding="SAME",activation="relu",use_bias=True,kernel_initializer=tf.initializers.random_normal(),
                kernel_regularizer=tf.keras.regularizers.l2(weight_decay))
    
    conv2 = Conv2D(64,3,1,padding="SAME",activation="relu",use_bias=True,kernel_initializer=tf.initializers.random_normal(),
                  kernel_regularizer=tf.keras.regularizers.l2(weight_decay))
    
    conv3 = Conv2D(64,5,1,padding="SAME",activation="relu",use_bias=True,kernel_initializer=tf.initializers.random_normal(),
                  kernel_regularizer=tf.keras.regularizers.l2(weight_decay))
    
    conv4 = Conv2D(64,7,1,padding="SAME",activation="relu",use_bias=True,kernel_initializer=tf.initializers.random_normal(),
                  kernel_regularizer=tf.keras.regularizers.l2(weight_decay))
    
    conv6 = Conv2D(128,3,1,padding="SAME",activation="relu",use_bias=True,kernel_initializer=tf.initializers.random_normal(),
                  kernel_regularizer=tf.keras.regularizers.l2(weight_decay))
    
    conv5 = Conv2D(3,3,1,padding="SAME",activation="relu",use_bias=True,kernel_initializer=tf.initializers.random_normal(),
                  kernel_regularizer=tf.keras.regularizers.l2(weight_decay))
    
    relu = ReLU(max_value = 1.0)

    #concatenation
    conv_1 = conv1(inputs)
    conv_2 = conv2(conv_1)
    conc_1 = tf.concat([conv_1 + conv_2], axis = -1)
    conv_3 = conv3(conc_1)
    conc_2 = tf.concat([conv_2 + conv_3], axis = -1)
    conv_6 = conv6(conc_2)
    conv_4 = conv4(conv_6)
    conc_3 = tf.concat([conv_1 + conv_2 + conv_3 + conv_4], axis = -1)
    #Calculating transmission matrix and global atmospheric light
    k = conv5(conc_3)

    #Calculating dehazed image
    j = tf.math.multiply(k, inputs) - k + 1.0
    output = relu(j)
    return Model(inputs = inputs, outputs = output)