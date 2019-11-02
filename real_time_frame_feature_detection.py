#this code compromises ORB algorithm to compute the features of the reference frame and real time frame simultaneously


import cv2
import numpy as np

# load image
img = cv2.imread('model/the-sun-is-also-a-star.jpg', 1)
# capture real time video
cap = cv2.VideoCapture(0)

# feature detection of model
orb = cv2.ORB_create()
kp_img, des_img = orb.detectAndCompute(img, None)  # argument none=no mask

# drawing features in model
img = cv2.drawKeypoints(img, kp_img, img)

while True:
    # read the camera
    _, frame = cap.read()

    # feature detection and drawing
    kp_frame, des_frame = orb.detectAndCompute(frame, None)
    frame = cv2.drawKeypoints(frame, kp_frame, frame)

    # showing image and camera in real time
    cv2.imshow('reference frame', img)
    cv2.imshow('real time frame', frame)

    # key event to get out of the loop
    key = cv2.waitKey(1)
    if key == 27:  # escapekey
        break

# release camera
cap.release()
cv2.destroyAllWindows()

