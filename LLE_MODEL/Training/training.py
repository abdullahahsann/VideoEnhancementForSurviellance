import numpy as np
import random
import glob
import sys
from PIL import Image

import shutil
import os 
import cv2
import matplotlib.pyplot as plt
import seaborn as sns
import time
import tensorflow as tf 
import keras
import keras.backend as K
from tensorflow.keras.layers import Conv2D, Concatenate
from tensorflow.keras import Input, Model

from .helper import *
from .loss import *

#--------------------------------Preparing Dataset----------------------------#
ori_path = '..//Dataset'
des_path = '../Dataset_Part1/All/'

#move_file(ori_path, des_path)

#--------------------------------Data Generator----------------------------#
class DataGenerator(keras.utils.Sequence):
    def __init__(self, ll_path, batch_size):
        self.train_list = populate_train_list(ll_path)
        self.batch_size = batch_size
        self.n_channels = 3
        self.data_list = self.train_list
        self.size = 512
        print("Total training examples: ", len(self.train_list))
        print("Batches per epoch:", int(np.floor(len(self.train_list) / self.batch_size)))

    def __len__(self):
        return int(np.floor(len(self.train_list) / self.batch_size))
    
    def __getitem__(self, index):
        #generate indexes of the batch
        indexes = self.data_list[index * self.batch_size:(index + 1)*self.batch_size]

        #generate data
        X = self.__data_generation(indexes)
        return X

    def on_epoch_end(self):
        self.indexes = np.arange(len(self.list_IDs))
        if self.shuffle == True:
            np.random.shuffle(self.indexes)

    def __data_generation(self, indexes):
        #initialization
        X = np.empty((self.batch_size, self.size, self.size, self.n_channels))

        #generate data
        for i, ID in enumerate(indexes):
            data_ll_path = ID
            data_ll = Image.open(data_ll_path)
            data_ll = data_ll.resize((self.size, self.size), Image.ANTIALIAS)
            data_ll = np.asarray(data_ll)/255.0
            X[i,] = data_ll
        
        return K.variable(X)

#--------------------------------Model Architecture----------------------------#
def lle_model():
    #defining layers
    input_image = Input(shape=(512,512,3))
    conv1 = Conv2D(32, (3,3), strides=(1,1), activation='relu', padding="same")
    conv2 = Conv2D(32, (3,3), strides=(1,1), activation='relu', padding= "same")
    conv3 = Conv2D(32, (3,3), strides=(1,1), activation='relu', padding='same')
    conv4 = Conv2D(32, (3,3), strides=(1,1), activation='relu', padding='same')
    conv5 = Conv2D(32, (3,3), strides=(1,1), activation='relu', padding='same')
    conv6 = Conv2D(32, (3,3), strides=(1,1), activation='relu', padding="same")
    conv7 = Conv2D(24, (3,3), strides=(1,1), activation='tanh', padding="same")

    #concatenation
    conv_1 = conv1(input_image)
    conv_2 = conv2(conv_1)
    conv_3 = conv3(conv_2)
    conv_4 = conv4(conv_3)
    conc_1 = Concatenate(axis=-1)([conv_4, conv_3])
    conv_5 = conv5(conc_1)
    conc_2 = Concatenate(axis=-1)([conv_5, conv_2])
    conv_6 = conv6(conc_2)
    conc_3 = Concatenate(axis=-1)([conv_6, conv_1])
    f_c = conv7(conc_3)

    model = Model(inputs = input_image, outputs = f_c)
    return model    

#initiazlizing the model
low_light_model = lle_model()

#--------------------------------Image Processing Functions----------------------------#
#Preprocessing the input image
def ip_i_pre(frame):
    original_img = Image.open(frame)
    original_size = (np.array(original_img).shape[1], np.array(original_img).shape[0])
    original_img = original_img.resize((512,512), Image.ANTIALIAS) 
    original_img = (np.asarray(original_img)/255.0)

    img_lowlight = Image.open(frame)
    img_given = np.array(img_lowlight)
    img_lowlight = img_lowlight.resize((512,512), Image.ANTIALIAS)
    img_lowlight = (np.asarray(img_lowlight)/255.0) 
    img_lowlight = np.expand_dims(img_lowlight, 0)

    return original_img, img_lowlight, original_size

#applying image curves
def applying_curve_maps(A, img_ll):
    global btw_arr
    r1, r2, r3, r4, r5, r6, r7, r8 = A[:,:,:,:3], A[:,:,:,3:6], A[:,:,:,6:9], A[:,:,:,9:12], A[:,:,:,12:15], A[:,:,:,15:18], A[:,:,:,18:21], A[:,:,:,21:24]
    #applying pixel wise curve mapping recursively
    x = img_ll + (r1 * (tf.pow(img_ll,2) - img_ll))
    x = x + (r2 * (tf.pow(x,2) - x))
    x = x + (r3 * (tf.pow(x,2) - x))
    x = x + (r4 * (tf.pow(x,2) - x))
    x = x + (r5 * (tf.pow(x,2) - x))
    x = x + (r6 * (tf.pow(x,2) - x))
    x = x + (r7 * (tf.pow(x,2) - x))
    enhanced_image = x + (r8 * (tf.pow(x,2) - x))
    for_loss = enhanced_image
    return enhanced_image, for_loss, r1

#output preprocessing
def op_pre(enhance_image, original_size):
    enhance_image = tf.cast((enhance_image[0,:,:,:] * 255), dtype=np.uint8)
    enhance_image = Image.fromarray(enhance_image.numpy())
    enhance_image = enhance_image.resize(original_size, Image.ANTIALIAS)
    enhance_image = np.array(enhance_image)
    
    return enhance_image

#Fucntion to show heatmaps if needs be
def hm(rmap, cval, original_size):
    r1_image =  rmap[0,:,:,:]
    op_cv_img = cv2.resize(r1_image, (original_size), interpolation=cv2.INTER_AREA)

    print("B Channel")
    r_c = op_cv_img[:,:,0]
    ax = sns.heatmap(r_c, cmap = cval)
    plt.show()

    print("G Channel")
    r_c = op_cv_img[:,:,1]
    ax = sns.heatmap(r_c, cmap= cval)
    plt.show()

    print("R Channel")
    r_c = op_cv_img[:,:,2]
    ax = sns.heatmap(r_c, cmap= cval)
    plt.show()

#--------------------------------Training----------------------------#
loss = []
t_loss = []

def train(gpu , ll_path, batch_size, lr, epochs, cp_iter, cp_folder):
    global loss, t_loss
    os.environ['CUDA_VISIBLE_DEVICES'] = str(gpu)

    train_dataset = DataGenerator(ll_path, batch_size)
    optimizer = tf.keras.optimizers.Adam(learning_rate=lr)

    model = lle_model()
    min_loss = 10000.0
    print("Training Started...")

    for epoch in range(epochs):
        print("\nStart of epoch %d" % (epoch,), end=' ')
        start_time_epoch = time.time()
        for iteration, img_ll in enumerate(train_dataset):
            with tf.GradientTape() as tape:
                A = model(img_ll)
                #getting image parameter maps
                r1, r2, r3, r4, r5, r6, r7, r8 = A[:,:,:,:3], A[:,:,:,3:6], A[:,:,:,6:9], A[:,:,:,9:12], A[:,:,:,12:15], A[:,:,:,15:18], A[:,:,:,18:21], A[:,:,:,21:24]

                #applying pixel wise curve mapping recursively
                x = img_ll + (r1 * (tf.pow(img_ll,2) - img_ll))
                x = x + (r2 * (tf.pow(x,2) - x))
                x = x + (r3 * (tf.pow(x,2) - x))
                x = x + (r4 * (tf.pow(x,2) - x))
                x = x + (r5 * (tf.pow(x,2) - x))
                x = x + (r6 * (tf.pow(x,2) - x))
                x = x + (r7 * (tf.pow(x,2) - x))
                enhanced_image = x + (r8 * (tf.pow(x,2) - x))

                #calculating losses
                loss_TV = 200*L_TV(A)
                loss_spa = tf.reduce_mean(L_spa(enhanced_image, img_ll))
                loss_col = 5*tf.reduce_mean(L_color(enhanced_image))
                loss_exp = 10*tf.reduce_mean(L_exp(enhanced_image, mean_val=0.6))

                total_loss = loss_TV + loss_spa + loss_col + loss_exp
                xx = np.array(total_loss)
                xx = round(float(xx), 4)

            grads = tape.gradient(total_loss, model.trainable_weights)
            optimizer.apply_gradients(zip(grads, model.trainable_weights))

            progress(epoch+1, (iteration+1), len(train_dataset), total_loss=total_loss)

            if (iteration+1) % cp_iter == 0 and total_loss < min_loss:
                min_loss = total_loss
                progress(epoch+1, (iteration+1), len(train_dataset), total_loss=total_loss, message=' ----- saved weight for epoch ' + str(epoch+1) + ' iter ' + str(iteration+1))
                model.save_weights(os.path.join(cp_folder, "ep_"+str(epoch+1)+"_it_"+str(iteration+1)+".h5"))
                loss.append(total_loss)

                #showing
                enhanced_image = tf.cast((enhanced_image[0,:,:,:] * 255), dtype=np.uint8)
                enhanced_image = Image.fromarray(enhanced_image.numpy())
                enhanced_image = enhanced_image.resize((512,512), Image.ANTIALIAS)
                enhanced_image = np.array(enhanced_image)
                display_img(enhanced_image, img_ll)
        t_loss.append(xx)
        print("Time taken: %.2fs" % (time.time() - start_time_epoch))
    model.save("saved_model/model")    


train_data_path = "../Dataset_Part1/All/"
weight_save_path = "../Weights_saved"
train(0, train_data_path, 2, 0.0001, 50, 500, weight_save_path)

#--------------------------------Plotting Loss----------------------------#

plt.plot(t_loss, label = "training_loss")
plt.xlabel("epoch")
plt.ylabel("loss")
plt.legend()
plt.show()