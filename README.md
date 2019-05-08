# DroNet: Collision Detection

Project inspired from DroNet: Learning to fly by driving (https://github.com/uzh-rpg/rpg_public_dronet)

# Dataset:
Collision dataset collected by Go-Pro camera mounted on bike running on roads\
for training, validation and testing. Pixels: 960 X 720 X 3

## Link: https://drive.google.com/open?id=1ZarSED1EyZhqZq_dctexsEdDmzJiFGHg

Train images :      5062\
Validation images : 534\
Testing images :    1212

# Architecture:

|Layer (type)|Output Shape|Param|
|------------|------------|-----|
|vgg16 (Model)|(None, 3, 2, 512)|14714688|
|conv2d_1 (Conv2D)|(None, 3, 2, 32)|147488|
|max_pooling2d_2 (MaxPooling2|(None, 2, 1, 32)|0|
|dropout_1 (Dropout)|(None, 2, 1, 32)|0|         
|conv2d_2 (Conv2D)|(None, 2, 1, 64)|18496|
|max_pooling2d_3 (MaxPooling2|(None, 1, 1, 64)|0|    
|flatten_1 (Flatten)|(None, 64)|0|
|dense_1 (Dense)|(None, 512)|33280|
|dense_2 (Dense)|(None, 1)|513|   


Total params: 14,914,465\
Trainable params: 14,914,465\
Non-trainable params: 0
_________________________________________________________________

Hyperparameters:
1. learning rate of 0.01
2. epoch
3. batch size

Optimizer :
1. SGD

Loss:\
&nbsp;&nbsp;&nbsp;Binary Cross-Entropy

# Procedure

1. How to run your code for training and testing?

A. Using google collab:

    Download the colab notebook that you want to run. Upload it in google colab.
    Do "Add to my drive" on the shared folder.
    Run all code snippets in notebook.
    
B. Using local Environment:

    B.1 Install Dependencies
    Dependencies:
    • TensorFlow 1.13.1
    • Keras 2.2.4 (Make sure that the Keras version is correct!)
    • NumPy 1.16.3
    • scikit-learn 0.20.3
    • Python gflags
    
    Upload google colab notebook in google collab or jupyter. Download as python file in menu options.
    Adjust paths as per downloaded datset
    Run your code: "python train.py" or "python test.py"

2. How to use GUI?

    GUI is designed to run evaluate performance of different saved models.\
    Pick your model using select model button.\
    Run evaluate.\
    Check results in space of GUI below.\
    Demo video: 

3. Conclusion:
   
   The given model achieves an accuracy of xx.xx % as compared to random regression accuracy of yy.yy %
