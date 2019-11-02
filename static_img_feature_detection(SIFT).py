#this code implements SIFT Algorithm to detect features of static reference frame

import cv2
import numpy as np

img = cv2.imread('model/the-sun-is-also-a-star.jpg',1)
sift = cv2.xfeatures2d.SIFT_create()

kp, des = sift.detectAndCompute(img, None)

trained_image = cv2.drawKeypoints(img, kp, img, color=(0,255,0), flags=0)
cv2.imshow('reference_frame',trained_image)
cv2.waitKey(0)