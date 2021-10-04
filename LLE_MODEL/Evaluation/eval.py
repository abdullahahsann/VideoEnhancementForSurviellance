import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import tensorflow as tf 
import keras
import keras.backend as K
from tensorflow.keras.layers import Conv2D, AveragePooling2D, Activation, Concatenate
from tensorflow.keras import Sequential, Input, Model
from model import lle_model
from image_processing import *


#---------------Image Evaluation---------------------
test_img = "s3.jpg"
frame = Image.open(test_img)
frame = np.asarray(frame)

def single_image_eval(test_img):
    load_model = lle_model()
    load_model.load_weights("../Model/ep_23_it_1000.h5")
    #first go
    original_img, img_lowlight, original_size = ip_i_pre(test_img)
    A = load_model.predict(img_lowlight)
    enhance_image, for_loss = applying_curve_maps(A, original_img, btw_arr)
    enhance_image = op_pre(enhance_image, original_size)

    #second go
    again_image = enhance_image
    original_img2 = Image.fromarray((again_image))
    original_size2 = (np.array(original_img2).shape[1], np.array(original_img2).shape[0])
    original_img2 = original_img2.resize((512,512), Image.ANTIALIAS) 
    original_img2 = (np.asarray(original_img2)/255.0)

    img_lowlight2 = Image.fromarray(again_image)   
    img_lowlight2 = img_lowlight2.resize((512,512), Image.ANTIALIAS)
    img_lowlight2 = (np.asarray(img_lowlight2)/255.0) 
    img_lowlight2 = np.expand_dims(img_lowlight2, 0)

    A = load_model.predict(img_lowlight2)
    enhance_image2, for_loss, r1 = applying_curve_maps(A, original_img2, btw_arr)
    enhance_image2 = op_pre(enhance_image2, original_size2)
    plt.imshow(frame)
    plt.show()
    plt.imshow(enhance_image2)
    plt.show()


#---------------Video Evaluation---------------------
def testvideo(video_input, video_output_name):
    load_model = lle_model()
    load_model.load_weights("../Model/ep_23_it_1000.h5")

    ### load image ###
    cap = cv2.VideoCapture(video_input)
    prev_frame_time = 0
    new_frame_time = 0

    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))
    frameSize = (frame_width, frame_height)
    out = cv2.VideoWriter(video_output_name, cv2.VideoWriter_fourcc('M','P','4','V'), 25, frameSize)
    length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    print( 'Total Frames: ', length )

    if (cap.isOpened() == False):
        print("Unable to read camera feed")
    counter = 1

    while(True):
        print("Frames Processed: ", counter, "/", length)
        ret, frame = cap.read()
        if ret == True:    
            o_i = Image.fromarray((frame))
            original_size = (np.array(o_i).shape[1], np.array(o_i).shape[0])
            original_img = o_i.resize((512,512), Image.ANTIALIAS) 
            original_img = (np.asarray(original_img)/255.0)
    
            img_given = np.array(o_i)
        
            img_lowlight = o_i.resize((512,512), Image.ANTIALIAS)
            img_lowlight = (np.asarray(img_lowlight)/255.0) 
            img_lowlight = np.expand_dims(img_lowlight, 0)

            ### process image ###
            A = model.predict(img_lowlight)
            r1, r2, r3, r4, r5, r6, r7, r8 = A[:,:,:,:3], A[:,:,:,3:6], A[:,:,:,6:9], A[:,:,:,9:12], A[:,:,:,12:15], A[:,:,:,15:18], A[:,:,:,18:21], A[:,:,:,21:24]
            x = img_ll + (r1 * (tf.pow(img_ll,2) - img_ll))
            x = x + (r2 * (tf.pow(x,2) - x))
            x = x + (r3 * (tf.pow(x,2) - x))
            x = x + (r4 * (tf.pow(x,2) - x))
            x = x + (r5 * (tf.pow(x,2) - x))
            x = x + (r6 * (tf.pow(x,2) - x))
            x = x + (r7 * (tf.pow(x,2) - x))
            enhance_image = x + (r8 * (tf.pow(x,2) - x))

            enhance_image = tf.cast((enhance_image[0,:,:,:] * 255), dtype=np.uint8)
            enhance_image = Image.fromarray(enhance_image.numpy())
            enhance_image = enhance_image.resize(original_size, Image.ANTIALIAS)
            enhance_image = np.array(enhance_image)

            again_image = enhance_image

            original_img2 = Image.fromarray((again_image))
            original_size2 = (np.array(original_img2).shape[1], np.array(original_img2).shape[0])
            original_img2 = original_img2.resize((512,512), Image.ANTIALIAS) 
            original_img2 = (np.asarray(original_img2)/255.0)

            img_lowlight2 = Image.fromarray(again_image)   
            img_lowlight2 = img_lowlight2.resize((512,512), Image.ANTIALIAS)
            img_lowlight2 = (np.asarray(img_lowlight2)/255.0) 
            img_lowlight2 = np.expand_dims(img_lowlight2, 0)

            A2 = model.predict(img_lowlight2)
            r1, r2, r3, r4, r5, r6, r7, r8 = A2[:,:,:,:3], A2[:,:,:,3:6], A2[:,:,:,6:9], A2[:,:,:,9:12], A2[:,:,:,12:15], A2[:,:,:,15:18], A2[:,:,:,18:21], A2[:,:,:,21:24]
            x = img_ll + (r1 * (tf.pow(img_ll,2) - img_ll))
            x = x + (r2 * (tf.pow(x,2) - x))
            x = x + (r3 * (tf.pow(x,2) - x))
            x = x + (r4 * (tf.pow(x,2) - x))
            x = x + (r5 * (tf.pow(x,2) - x))
            x = x + (r6 * (tf.pow(x,2) - x))
            x = x + (r7 * (tf.pow(x,2) - x))
            enhance_image2 = x + (r8 * (tf.pow(x,2) - x))
            enhance_image2 = tf.cast((enhance_image2[0,:,:,:] * 255), dtype=np.uint8)
            enhance_image2 = Image.fromarray(enhance_image2.numpy())
            enhance_image2 = enhance_image2.resize(original_size2, Image.ANTIALIAS)
            enhance_image2 = np.array(enhance_image2)
            
            cv2.startWindowThread()
            cv2.namedWindow("preview")
            cv2.putText(enhance_image2, fps, (7, 70), font, 3, (100, 255, 0), 3, cv2.LINE_AA)
            cv2.imshow("original", img_given)
            cv2.imshow("enhanced", enhance_image2)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break        
            counter += 1
        else:
            break
    cap.release()
    out.release()
    cv2.destroyAllWindows()


#---------------Live Evaluation---------------------
def testLive(video_output_name):
    load_model = lle_model()
    load_model.load_weights("../Model/ep_23_it_1000.h5")

    ### load image ###
    cap = cv2.VideoCapture(0)
    prev_frame_time = 0
    new_frame_time = 0

    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))
    frameSize = (frame_width, frame_height)
    out = cv2.VideoWriter(video_output_name, cv2.VideoWriter_fourcc('M','P','4','V'), 25, frameSize)
    length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    print( 'Total Frames: ', length )

    if (cap.isOpened() == False):
        print("Unable to read camera feed")
    counter = 1

    while(True):
        print("Frames Processed: ", counter, "/", length)
        ret, frame = cap.read()
        if ret == True:    
            o_i = Image.fromarray((frame))
            original_size = (np.array(o_i).shape[1], np.array(o_i).shape[0])
            original_img = o_i.resize((512,512), Image.ANTIALIAS) 
            original_img = (np.asarray(original_img)/255.0)
    
            img_given = np.array(o_i)
        
            img_lowlight = o_i.resize((512,512), Image.ANTIALIAS)
            img_lowlight = (np.asarray(img_lowlight)/255.0) 
            img_lowlight = np.expand_dims(img_lowlight, 0)

            ### process image ###
            A = model.predict(img_lowlight)
            r1, r2, r3, r4, r5, r6, r7, r8 = A[:,:,:,:3], A[:,:,:,3:6], A[:,:,:,6:9], A[:,:,:,9:12], A[:,:,:,12:15], A[:,:,:,15:18], A[:,:,:,18:21], A[:,:,:,21:24]
            x = img_ll + (r1 * (tf.pow(img_ll,2) - img_ll))
            x = x + (r2 * (tf.pow(x,2) - x))
            x = x + (r3 * (tf.pow(x,2) - x))
            x = x + (r4 * (tf.pow(x,2) - x))
            x = x + (r5 * (tf.pow(x,2) - x))
            x = x + (r6 * (tf.pow(x,2) - x))
            x = x + (r7 * (tf.pow(x,2) - x))
            enhance_image = x + (r8 * (tf.pow(x,2) - x))

            enhance_image = tf.cast((enhance_image[0,:,:,:] * 255), dtype=np.uint8)
            enhance_image = Image.fromarray(enhance_image.numpy())
            enhance_image = enhance_image.resize(original_size, Image.ANTIALIAS)
            enhance_image = np.array(enhance_image)

            again_image = enhance_image

            original_img2 = Image.fromarray((again_image))
            original_size2 = (np.array(original_img2).shape[1], np.array(original_img2).shape[0])
            original_img2 = original_img2.resize((512,512), Image.ANTIALIAS) 
            original_img2 = (np.asarray(original_img2)/255.0)

            img_lowlight2 = Image.fromarray(again_image)   
            img_lowlight2 = img_lowlight2.resize((512,512), Image.ANTIALIAS)
            img_lowlight2 = (np.asarray(img_lowlight2)/255.0) 
            img_lowlight2 = np.expand_dims(img_lowlight2, 0)

            A2 = model.predict(img_lowlight2)
            r1, r2, r3, r4, r5, r6, r7, r8 = A2[:,:,:,:3], A2[:,:,:,3:6], A2[:,:,:,6:9], A2[:,:,:,9:12], A2[:,:,:,12:15], A2[:,:,:,15:18], A2[:,:,:,18:21], A2[:,:,:,21:24]
            x = img_ll + (r1 * (tf.pow(img_ll,2) - img_ll))
            x = x + (r2 * (tf.pow(x,2) - x))
            x = x + (r3 * (tf.pow(x,2) - x))
            x = x + (r4 * (tf.pow(x,2) - x))
            x = x + (r5 * (tf.pow(x,2) - x))
            x = x + (r6 * (tf.pow(x,2) - x))
            x = x + (r7 * (tf.pow(x,2) - x))
            enhance_image2 = x + (r8 * (tf.pow(x,2) - x))
            enhance_image2 = tf.cast((enhance_image2[0,:,:,:] * 255), dtype=np.uint8)
            enhance_image2 = Image.fromarray(enhance_image2.numpy())
            enhance_image2 = enhance_image2.resize(original_size2, Image.ANTIALIAS)
            enhance_image2 = np.array(enhance_image2)
            
            cv2.startWindowThread()
            cv2.namedWindow("preview")
            cv2.putText(enhance_image2, fps, (7, 70), font, 3, (100, 255, 0), 3, cv2.LINE_AA)
            cv2.imshow("original", img_given)
            cv2.imshow("enhanced", enhance_image2)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break        
            counter += 1
        else:
            break
    cap.release()
    out.release()
    cv2.destroyAllWindows()


#--------Evaluation----------
v_i = 'test2.mp4'
v_o = 'LiveTest.mp4'
testLive(v_o)




