import uuid
import os
import time
import cv2
#import numpy as np
#import torch

image_path = os.path.join('data','image')
labels = ['awake','drowsy']
num_img = 20

cap = cv2.VideoCapture(0)
for label in labels :
    print("collecting img for {}".format(label))
    time.sleep(5)

    for img in range(num_img):
        print("collecting images for {} , img number{}".format(label,img))
        ret, frame = cap.read()
        
        img_name = os.path.join(image_path, label + "." + str(uuid.uuid1())+".jpg")
        cv2.imwrite(img_name,frame)
        cv2.imshow('img collection :',frame)
        time.sleep(2)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
cap.release()
cv2.destroyAllWindows()