import time
import sys
# from onvif import ONVIFCamera
from time import sleep
import os
import time
# from hikvisionapi import Client
import cv2
import getopt
import json

IP = "192.168.0.145"  # Camera IP address
PORT = 80  # Port
USER = "admin"  # onvif and RTSP Username
PASS = "Lums@12345"  # onvif Password
streamPass = "Lums@hik12345"

DIR = os.getcwd() + '/images/lab02/'

def click_event(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img_mat, str(x) + ',' +
                    str(y), (x,y), font,
                    1, (255, 0, 0), 2)
        coord.append([x,y])
        cv2.imshow(img, img_mat)

def get_coordinates(img):
    cv2.imshow(img, img_mat)
    cv2.setMouseCallback(img, click_event)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def get_images(dir):
    images = []
    for name in os.listdir(dir):
        if name.endswith('.jpg'):
            images.append(name)
    return images
    
# def get_json(image_name):
#     name = os.path.splitext(image_name)[0] +'.json'
#     return name

def save_coordinates(data):
    filename = DIR + 'coords.json'
    json_object = json.dumps(data, indent=4)
    with open(filename, 'w') as f:
        f.write(json_object)
    return

if __name__ == "__main__":
    images = get_images(DIR)
    data = {}
    for img in images:
        coord = []
        img_mat = cv2.imread(DIR + img)
        get_coordinates(img)
        data[img] = coord
    save_coordinates(data)