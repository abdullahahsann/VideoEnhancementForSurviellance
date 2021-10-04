import random
import glob
from PIL import Image
import shutil
import os 
import matplotlib.pyplot as plt
import sys

# returns a list with path to all the training images
def populate_train_list(ll_path):
    train_list = glob.glob(ll_path + "*.JPG")
    random.shuffle(train_list)
    return train_list

#to prepare test data
def move_file(ori_path, des_path):
    dir_list = [x[0] for x in os.walk(ori_path)]
    for p in dir_list[1:]:
        for f in glob.glob(p + "/*.JPG"):
            name = f.split("/")[-2] + "_" + f.split("/")[-1]
            shutil.move(f, os.path.join(des_path, name))

#display images during training
def display_img(e_h, lle_img):    
    plt.figure(figsize = (15,15))
    display_list = [lle_img[0], e_h]
    title = ['lle Image', 'enhanced Image']
    
    for i in range(2):
        plt.subplot(1, 2, i+1)
        plt.title(title[i])
        plt.imshow(display_list[i])
        plt.axis('off')
        
    plt.show()

#show progess during training
def progress(epoch, trained_sample ,total_sample, bar_length=25, total_loss=0, message=""):
    percent = float(trained_sample) / total_sample
    hashes = '#' * int(round(percent * bar_length))
    spaces = ' ' * (bar_length - len(hashes))
    sys.stdout.write("\rEpoch {0}: [{1}] {2}%  ----- Loss: {3}".format(epoch, hashes + spaces, int(round(percent * 100)), float(total_loss)) + message)
    sys.stdout.flush()