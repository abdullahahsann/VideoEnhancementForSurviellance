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


#---------------Image Evaluation---------------------
def evaluate_images(net, test_img_path):
    test_img = glob.glob(test_img_path + '/*')
    random.shuffle(test_img)

    for img in test_img:
        img = tf.io.read_file(img)
        img = tf.io.decode_jpeg(img, channels = 3)
        
        temp_zero = img.shape[0]
        temp_one = img.shape[1]

        img = tf.image.resize(img, size = (480, 640), antialias = True)
        img = img / 255.0
        img = tf.expand_dims(img, axis = 0)     
        
        dehaze = net(img, training = False)
        
        img = tf.image.resize(img, size = (temp_zero, temp_one), antialias = True)
        dehaze = tf.image.resize(dehaze, size = (temp_zero, temp_one), antialias = True)

        plt.figure(figsize = (80, 80))
        display_list = [img[0], dehaze[0]]      
        title = ['Hazy Image', 'Dehazed Image']
        for i in range(2):
            plt.subplot(1, 2, i+1)
            plt.title(title[i], fontsize = 65, y = 1.045)
            plt.imshow(display_list[i])
            plt.axis('off')
        
        plt.show()

#---------------Video Evaluation---------------------
def evaluate_video(net, video_input, video_output_name):
    '''
    net: Model on which to evaluate
    video_input: video to be evaluated path
    video_output name: processed video save
    '''
    cap = cv2.VideoCapture(video_input)
    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))
    frameSize = (frame_width, frame_height)
    out = cv2.VideoWriter(video_output_name, cv2.VideoWriter_fourcc('M','P','4','V'), 30, frameSize)
    length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    print( 'Total Frames: ', length )

    if (cap.isOpened() == False):
        print("Unable to read camera feed")
    counter = 1

    while(True):
        print("Frames Processed: ", counter)
        ret, frame = cap.read()
        if ret == True:
        
            img= tf.convert_to_tensor(frame)
            
            temp_zero = img.shape[0]
            temp_one = img.shape[1]

            img = tf.image.resize(img, size = (480, 640), antialias = True)

            img = img / 255.0
            img = tf.expand_dims(img, axis = 0)      #transform input image from 3D to 4D###
            dehaze = net(img, training = False)
            
            img = tf.image.resize(img, size = (temp_zero, temp_one), antialias = True)
            dehaze = tf.image.resize(dehaze, size = (temp_zero, temp_one), antialias = True)
            
            img = img[0].numpy()
            img *= 255/img.max() 
            # cast to 8bit
            img = np.array(img, np.uint8)
            
            d_op = dehaze[0].numpy()
            d_op *= 255/d_op.max() 
            # cast to 8bit
            d_op = np.array(d_op, np.uint8)
            
            out.write(d_op)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break        
            counter += 1

        else:
            break
    cap.release()
    out.release()

    cv2.destroyAllWindows()

def evaluate_live(net, video_output_name):
    cap = cv2.VideoCapture(0)
    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))
    frameSize = (frame_width, frame_height)
    out = cv2.VideoWriter(video_output_name, cv2.VideoWriter_fourcc('M','P','4','V'), 30, frameSize)
    length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
  
    if (cap.isOpened() == False):
        print("Unable to read camera feed")
    counter = 1

    while(True):
        ret, frame = cap.read()
        if ret == True:
           
            img= tf.convert_to_tensor(frame)
            
            temp_zero = img.shape[0]
            temp_one = img.shape[1]

            img = tf.image.resize(img, size = (480, 640), antialias = True)
            img = img / 255.0
            img = tf.expand_dims(img, axis = 0)   

            dehaze = net(img, training = False)
            
            img = tf.image.resize(img, size = (temp_zero, temp_one), antialias = True)
            dehaze = tf.image.resize(dehaze, size = (temp_zero, temp_one), antialias = True)
            
            img = img[0].numpy()
            img *= 255/img.max() 
            img = np.array(img, np.uint8)
            
            d_op = dehaze[0].numpy()
            d_op *= 255/d_op.max() 
            d_op = np.array(d_op, np.uint8)
           
            cv2.startWindowThread()
            cv2.namedWindow("preview")
            cv2.imshow("preview", d_op)
            cv2.imshow("orig", img)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break        
            counter += 1
        else:
            break
    cap.release()
    out.release()

    cv2.destroyAllWindows()


#--------Evaluation----------
model_path = './Model/trained_model'
video_input = './Testvideos2/mega2.mp4' 
video_output_name = 'pleasemegae2.mp4'

test_net = tf.keras.models.load_model(model_path, compile = False)
evaluate_live(test_net, video_output_name )