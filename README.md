# Feature-Detection
## using numpy and opencv

> **USAGE**

* add the reference surface to be detected in real-time-frame in `model` folder
* change the name of the image in the codes i.e `img = cv2.imread('model\abc.jpg',1)` *1 in argument represents the scale image i.e BGR that can be altered as opted*


### feature extraction:
* looking in both the reference and target images for features that stand out.
* find the object when a certain number of positive feature matches are found between the target and reference images. 

For a region or point of an image to be labeled as feature it should fulfill two important properties:
1.  some uniqueness i.e : corners or edges
2. invariant against scale, rotation or brightness changes.

 ### feature description:
* finding suitable representation of the information the identified features provide. 
> A descriptor provides a representation of the information given by a feature and its surroundings. Which is abstracted to a feature vector *a vector that contains the descriptors of the keypoints found in the image with the reference object.*

There are many algorithms that extract image features and compute its descriptors **(SIFT, SURF, Harris and ORB)**
The given code pratices **SIFT** algorithm *(which is patent)* and **ORB** as an *efficient alternative*
 ORB embraces features of FAST and BRIEF algorithms, which in real time AR applications help process data (key points) and computes descriptors fast.
