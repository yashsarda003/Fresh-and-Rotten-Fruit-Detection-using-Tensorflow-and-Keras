from importlib import import_module
from importlib.resources import path
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing import image


# new_model = tf.keras.models.load_model('h5_model/model.h5')

new_model = tf.keras.models.load_model('h5_model/classification_model.h5')

def reset_list(data_list):
    data_list.clear()



def detection(file_list):
    img_data = []  
    tot_val = 0.0
    check_val = 0

    for images in file_list:
        img = image.load_img(images,target_size = (200,200))

        x = image.img_to_array(img)
        x = np.expand_dims(x,axis = 0)
        images = np.vstack([x])

        val = new_model.predict(x)  
        print("Value is ===========> ",val[0][0])

        tot_val = val[0][0]+tot_val
        print("Total value is =============>  ",tot_val)

        check_val = tot_val/4

        print("Check value is =======>   ",check_val)


    if 0 == check_val or check_val <= 0.3:
        return 0
    else:
        return 1 



