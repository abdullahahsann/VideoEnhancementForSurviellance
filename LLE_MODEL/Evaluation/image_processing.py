
import numpy as np
from PIL import Image
import cv2
import matplotlib.pyplot as plt
import seaborn as sns
import tensorflow as tf 



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