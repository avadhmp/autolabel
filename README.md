# autolabel
cpfile goes through a folder and collects all the image with jpeg extension and creates a corresponding xml file with the same prefix 
using the "template" empty xml 
test file uses color detection to detect object and created bounding box based on predefined area of bounding box size to create x,y min and max location and user chosen class label all imported into xml format for easier adatability for object detection algorithms trianign and class creation. I used this code roboflow for yolov5 for labeling and class creation rather than repetivie creating label and boxing object of interest.
