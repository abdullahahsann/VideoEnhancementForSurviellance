import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

def load_image(img_path):
    img = tf.io.read_file(img_path)
    img = tf.io.decode_jpeg(img, channels = 3)
    img = tf.image.resize(img, size = (480, 640), antialias = True)
    img = img / 255.0
    return img


def display_img(model, hazy_img, orig_img):
    dehazed_img = model(hazy_img, training = True)
    plt.figure(figsize = (15,15))
    display_list = [hazy_img[0], orig_img[0], dehazed_img[0]]
    title = ['Hazy Image', 'Ground Truth', 'Dehazed Image']
    
    for i in range(3):
        plt.subplot(1, 3, i+1)
        plt.title(title[i])
        plt.imshow(display_list[i])
        plt.axis('off')
        
    plt.show()