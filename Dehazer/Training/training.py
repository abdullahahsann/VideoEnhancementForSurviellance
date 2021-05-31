import os
import numpy as np
import matplotlib.pyplot as plt
import glob
import random
from PIL import Image
import time
import datetime
import cv2
import tensorflow as tf
from tensorflow.keras.layers import *
from tensorflow.keras.models import Model
from tensorflow.keras.losses import mean_squared_error
from tensorflow.keras.optimizers import Adam
from tqdm import tqdm
from .helper import display_img, load_image

#--------------Initializing datapath for datasets---------------------

#For ResideOTS_archuive
def data_path_archive(orig_img_path, hazy_img_path):
    train_img = []
    val_img = []

    orig_img = glob.glob(orig_img_path + '/*.jpg')
    n = len(orig_img)
    random.shuffle(orig_img)
    train_keys = orig_img[:int(0.9*n)]        
    val_keys = orig_img[int(0.9*n):]

    split_dict = {}
    for key in train_keys:
        split_dict[key] = 'train'
    for key in val_keys:
        split_dict[key] = 'val'
        
    hazy_img = glob.glob(hazy_img_path + '/*.jpg')

    for img in hazy_img:
        img_name = img.split('/')[-1]
        orig_path = orig_img_path + '/' + img_name.split('_')[0] + '.jpg'
        if (split_dict[orig_path] == 'train'):
            train_img.append([img, orig_path])
        else:
            val_img.append([img, orig_path])
    return train_img, val_img


#For ONH Dataset
def data_path(orig_img_path, hazy_img_path):
    train_img = []
    val_img = []

    orig_img = glob.glob(orig_img_path + '/*')

    n = len(orig_img)
    random.shuffle(orig_img)
    train_keys = orig_img[:int(0.8*n)]        
    val_keys = orig_img[int(0.8*n):]

    split_dict = {}
    for key in train_keys:
        split_dict[key] = 'train'
    for key in val_keys:
        split_dict[key] = 'val'

    hazy_img = glob.glob(hazy_img_path + '/*')

    for img in hazy_img:
        img_name = img.split('/')[-1]
        if((img_name.split('.')[-1]) == 'png' ):
            orig_path = orig_img_path + '/' + img_name.split('_')[0] + '_GT.png'
        elif ((img_name.split('.')[-1]) == 'jpg' ):
            orig_path = orig_img_path + '/' + img_name.split('_')[0] + '_GT.jpg'
        if (split_dict[orig_path] == 'train'):
            train_img.append([img, orig_path])
        else:
            val_img.append([img, orig_path])

    return train_img, val_img

#For Moded Reside Archive Dataset
def check_image(img_name):
    img_value = img_name.split('_')[-1]
    img_value = img_value.split('.')[0] + '.' + img_value.split('.')[1]
    img_value = float(img_value)
    if img_value > 0.1 :
        return True
    else:
        return False

def data_path_mod_archive(orig_img_path, hazy_img_path):
    train_img = []
    val_img = []

    orig_img = glob.glob(orig_img_path + '/*.jpg')
    n = len(orig_img)
    random.shuffle(orig_img)
    train_keys = orig_img[:int(0.9*n)]        
    val_keys = orig_img[int(0.9*n):]

    split_dict = {}
    for key in train_keys:
        split_dict[key] = 'train'
    for key in val_keys:
        split_dict[key] = 'val'

    hazy_img = glob.glob(hazy_img_path + '/*.jpg')

    for img in hazy_img:
        img_name = img.split('/')[-1]
        check = check_image(img_name)
        if check == True:
            orig_path = orig_img_path + '/' + img_name.split('_')[0] + '.jpg'
            if (split_dict[orig_path] == 'train'):
                train_img.append([img, orig_path])
            else:
                val_img.append([img, orig_path])
    return train_img, val_img

#--------------------------------------------------------------

#-------------DataLoader------------------
def dataloader(train_data, val_data, batch_size):
    
    train_data_orig = tf.data.Dataset.from_tensor_slices([img[1] for img in train_data]).map(lambda x: load_image(x))
    train_data_haze = tf.data.Dataset.from_tensor_slices([img[0] for img in train_data]).map(lambda x: load_image(x))
    train = tf.data.Dataset.zip((train_data_haze, train_data_orig)).shuffle(buffer_size=100).batch(batch_size)
    
    val_data_orig = tf.data.Dataset.from_tensor_slices([img[1] for img in val_data]).map(lambda x: load_image(x))
    val_data_haze = tf.data.Dataset.from_tensor_slices([img[0] for img in val_data]).map(lambda x: load_image(x))
    val = tf.data.Dataset.zip((val_data_haze, val_data_orig)).shuffle(buffer_size=100).batch(batch_size)
    
    return train, val

#------------Function To start training model along with getting validation data result ---------------------
def train_model(epochs, train, val, net, train_loss_tracker, val_loss_tracker, optimizer):
    val_los = []
    train_los = []

    for epoch in range(epochs):
        print("\nStart of epoch %d" % (epoch,), end=' ')
        start_time_epoch = time.time()
        
        # training loop
        for step, (train_batch_haze, train_batch_orig) in enumerate(tqdm(train)):
            with tf.GradientTape() as tape:
                train_logits = net(train_batch_haze, training = True)
                loss = mean_squared_error(train_batch_orig, train_logits)
                
            grads = tape.gradient(loss, net.trainable_weights)
            optimizer.apply_gradients(zip(grads, net.trainable_weights))

            train_loss_tracker.update_state(train_batch_orig, train_logits)
           
        # validation loop
        for step, (val_batch_haze, val_batch_orig) in enumerate(val):
            val_logits = net(val_batch_haze, training = False)
            val_loss_tracker.update_state(val_batch_orig, val_logits)
            
            if step % 4 ==0:
                display_img(net, val_batch_haze, val_batch_orig)
        
        # validation result
        print("Time taken: %.2fs" % (time.time() - start_time_epoch))
        x = train_loss_tracker.result()
        y = val_loss_tracker.result()
        x = np.array(x)
        y = np.array(y)
        xx = round(float(x),4)
        yy = round(float(y),4)
        train_los.append(xx)
        val_los.append(yy)
        print(train_los)
        print(val_los)
        net.save('properaod/archive_mod/trained_model')          
        train_loss_tracker.reset_states()
        val_loss_tracker.reset_states()
    return train_los, val_los


#------------------------MODEL ARCHITECTURE------------------------
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

#--------To Check Models Architecture-----------
weight_decay = 1e-4
dh_check = dehazer_net()
dh_check.compile(optimizer='adam', loss=tf.keras.losses.mean_squared_error, metrics=['mse'])
dh_check.summary()
#---------------------------------------------

#--------Training Initialization---------------
#hyperparameters
epochs = 100
batch_size = 2
weight_decay = 1e-4

#Give Datasets Path
orig_img_path = './DATASETS/lesshazycomb/GT'
hazy_img_path = './DATASETS/lesshazycomb/hazy'

#Loading and initialzing datasets
train_data, val_data = data_path(orig_img_path, hazy_img_path)
train, val = dataloader(train_data, val_data, batch_size)

optimizer = Adam(learning_rate = 1e-3)
net = dehazer_net()

train_loss_tracker = tf.keras.metrics.MeanSquaredError(name = "train loss")
val_loss_tracker = tf.keras.metrics.MeanSquaredError(name = "val loss")

#Commencing Training
t_l, v_l = train_model(epochs, train, val, net, train_loss_tracker, val_loss_tracker, optimizer)
plt.plot(t_l, label = "training_loss")
plt.plot(v_l, label = "validation_loss")
plt.xlabel("epoch")
plt.ylabel("loss")
plt.legend()
plt.show()