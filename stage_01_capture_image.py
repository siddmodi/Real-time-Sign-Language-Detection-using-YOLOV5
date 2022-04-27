import os
import cv2
import time
import uuid

IMAGE_PATH='CollectedImages'

labels=['Hello','Yes','No','Thanks','IloveYou','Please']

number_of_images=2

for label in labels:
    print('collection of image stage start.............')
    img_path = os.path.join(IMAGE_PATH, label)
    print(img_path)
    os.makedirs(img_path)
    cap=cv2.VideoCapture(0,cv2.CAP_DSHOW)
    print('Collecting images for {}'.format(label))
    time.sleep(5)
    for imgnum in range(number_of_images):
        ret,frame=cap.read()
        imagename=os.path.join(IMAGE_PATH,label,label+'.'+'{}.jpg'.format(str(uuid.uuid1())))
        cv2.imwrite(imagename,frame)
        cv2.imshow('frame',frame)
        time.sleep(5)
    
        if cv2.waitKey(1) & 0xFF==ord('q'):
            break
    cap.release()
    print('Collection of images done succesfully')


    # To run :--->  python stage_01_capture_image.py