# Createan enviornment and install all dependencies and required library
command --> python -m venv env 
command --> cd yolov5 && pip install -r requirements.txt

# Stage 1 
command --> python stage_01_capture_image.py
--> To capture image with webcam and save all images in their respective class folder in a parent folder 

# Stage 2
command --> python stage_02_train_test_data.py
--> Create a data directory with train and test directory with 2 directories inside ie. images and labels ,
    collect all images in train and test dir 
# Use Labelimg (Annotation Tool) for labeling the image class and bounding box and save it in label folder

# Stage 3 
--> Here we train YOLO-V5 for our custom dataset
--> Create data.yaml file for our custom data 
--> We save our trained model weights as pt file (I saved as best.pt) 

# To run (Real time sign language detection)
command -->  cd yolov5
command -->  python detect.py --weights best.pt --img 416 --conf 0.5 --source 0


========================== **Explaination** =================================

This'll detect the sign language and create bounding box around them using YOLO V5

We create 3 stages for this project

1) This stage open webcam capture images and label them with their respective sign language and save that image as jpg in their respective sign language direcory

2) Create a data directory with train and test directory with 2 directories inside ie. images and labels, collect all images in train and test dir.
	We do custom labeling for each image using Annotation Tool - labelImg

3) Here we train YOLO-V5 for our custom dataset
   Create data.yaml file for our custom data 
   We save our trained model weights as pt file (I saved as best.pt)
