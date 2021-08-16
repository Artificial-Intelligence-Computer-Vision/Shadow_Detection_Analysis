import cv2
import numpy as np
from glob import glob
import os
from os.path import basename

image_path = "images_data/"
images = [count for count in glob(image_path +'*') if 'jpg' in count]

def save_image(img, file_name, image_to_save):
    image_path = "images_data/"
    image_number = [count for count in glob(image_path+'*') if 'jpg' in count]

    if image_to_save == "black_shadow":
        image_output = "black_shadow_cubes"
        
    for i in range(len(image_number)):
        cv2.imwrite(os.path.join(image_output, str(file_name)), img)
        cv2.waitKey(0)
        

def show_light_reflection(img):
    
    # Change the image to have shadow
    threshold_y = 1
    threshold_x = 1
    threshold2_x = 1
    threshold2_y = 1
    
    img = cv2.cvtColor(img,cv2.COLOR_RGB2HLS)
    shadow_mask = 0*img[:,:,1]
    
    # Get the grid of the image for both axis
    grid_x = np.mgrid[0:img.shape[0], 0:img.shape[1]][0]
    grid_y = np.mgrid[0:img.shape[0], 0:img.shape[1]][1]
    
    shadow_mask[((grid_x - threshold_x)*(threshold2_y - threshold_y) - (threshold2_x - threshold_x)*(grid_y-threshold_y) >=0)]=0
    
    brightness = 1
    bits_equal_1 = shadow_mask == 1
    bits_equal_0 = shadow_mask == 0
                
    img[:,:,1][bits_equal_1] = img[:,:,0][bits_equal_1] * brightness
    img[:,:,1][bits_equal_0] = img[:,:,0][bits_equal_0] * brightness

    return img
    
count = 0
for image in images:
    count +=1
    print(count)
    img = cv2.imread(image, -1)
    file_name = basename(image)
    
    light_reflection = show_light_reflection(img)
    
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    black_shadow = cv2.cvtColor(img, gray, cv2.COLOR_HSV2BGR)
    #black_shadow = cv2.applyColorMap(light_reflection[:,:,0], cv2.COLORMAP_HSV)
    #black_shadow = cv2.cvtColor(black_shadow, cv2.COLOR_HSV2RGB)
    
    save_image(black_shadow, file_name, image_to_save = "black_shadow")

    
    
