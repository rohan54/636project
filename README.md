# DroNet: Collision Detection

Project inspired from DroNet: Learning to fly by driving (https://github.com/uzh-rpg/rpg_public_dronet)

# Dataset:
Collision dataset collected by Go-Pro camera mounted on bike running on roads
for training, validation and testing. Pixels: 960 X 720 X 3

## Link: https://drive.google.com/open?id=1ZarSED1EyZhqZq_dctexsEdDmzJiFGHg

Train images :      5062
Validation images : 534
Testing images :    1212

# Architecture:

|Layer (type)|Output Shape|Param|
|------------|------------|-----|
|conv2d_1 (Conv2D)|(None, 94, 70, 32)|896|
|max_pooling2d_1 (MaxPooling2|(None, 47, 35, 32)|0|   
|dropout_1 (Dropout)|(None, 47, 35, 32)|0|    
|conv2d_2 (Conv2D)|(None, 45, 33, 64)|18496|
|max_pooling2d_2 (MaxPooling2|(None, 22, 16, 64)|0| 
|flatten_1 (Flatten)|(None, 22528)|0|
|dense_1 (Dense)|(None, 512)|11534848|
|dense_2 (Dense)|(None, 1)|513       


Total params: 11,554,753
Trainable params: 11,554,753
Non-trainable params: 0
_________________________________________________________________

Hyperparameters:
1. starting learning rate of 0.001
2. exponential per-step decay equal to 10−5
3. epoch
4. batch size

Optimizer:
1. SGD
2.Adam

Loss:
Binary Cross-Entropy

# Procedure

1. How to run your code for training and testing?

A. Using google collab:

    Download the colab notebook that you want to run. Upload it in google colab.
    Do "Add to my drive" on the shared folder.
    Run all.
    
B. Using local Environment:
    B.1 Install Dependencies
    Dependencies:
    • TensorFlow 1.5.0
    • Keras 2.1.4 (Make sure that the Keras version is correct!)
    • NumPy 1.12.1
    • OpenCV 3.1.0
    • scikit-learn 0.18.1
    • Python gflags
    
    Upload google colab notebook. Download as python file in menu options.
    Adjust paths as per downloaded datset
    Run your code: "python train.py" or "python test.py"

2. How to use GUI?
  GUI is designed to run evaluate performance of different saved models.
  Pick your model using select model button.
  Run evaluate.
  Check results in space of GUI below.
  Demo video: 

3. Conclusion:
   The given model achieves an accuracy of xx.xx % as compared to random regression accuracy of yy.yy %
