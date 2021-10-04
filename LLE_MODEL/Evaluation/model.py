import tensorflow as tf 
import keras
import keras.backend as K
from tensorflow.keras.layers import Conv2D, Concatenate
from tensorflow.keras import Sequential, Input, Model


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