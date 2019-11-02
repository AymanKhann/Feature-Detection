#this code implements ORB Algorithm to detect features of static reference frame

import cv2
import numpy as np

#reads the model image (reference frame)
img = cv2.imread('model/the-sun-is-also-a-star.jpg',1)

orb = cv2.ORB_create()
# find the keypoints
kp = orb.detect(img, None)
# compute the descriptors
kp, des = orb.compute(img, kp)

# draw only keypoints location,not size and orientation
trained_image = cv2.drawKeypoints(img, kp, img, color=(0,255,0), flags=0)
cv2.imshow('reference frame',trained_image)
cv2.waitKey(0)