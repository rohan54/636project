# DroNet: Collision Detection

Project inspired from DroNet: Learning to fly by driving (https://github.com/uzh-rpg/rpg_public_dronet)

# Dataset:
Collision dataset collected by Go-Pro camera mounted on bike running on roads
for training, validation and testing. Pixels: 960*720*3

## Link: https://drive.google.com/open?id=1ZarSED1EyZhqZq_dctexsEdDmzJiFGHg

Train images : 5062
Validation images : 534
Testing images : 1212

# Architecture:
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
conv2d_1 (Conv2D)            (None, 94, 70, 32)        896       
_________________________________________________________________
max_pooling2d_1 (MaxPooling2 (None, 47, 35, 32)        0         
_________________________________________________________________
dropout_1 (Dropout)          (None, 47, 35, 32)        0         
_________________________________________________________________
conv2d_2 (Conv2D)            (None, 45, 33, 64)        18496     
_________________________________________________________________
max_pooling2d_2 (MaxPooling2 (None, 22, 16, 64)        0         
_________________________________________________________________
flatten_1 (Flatten)          (None, 22528)             0         
_________________________________________________________________
dense_1 (Dense)              (None, 512)               11534848  
_________________________________________________________________
dense_2 (Dense)              (None, 1)                 513       
=================================================================
Total params: 11,554,753
Trainable params: 11,554,753
Non-trainable params: 0
_________________________________________________________________

Hyperparameters:
1. epoch
2. batch size

Optimizer:
1. SGD
2.Adam

Loss:
Binary Cross-Entropy

# Procedure

1. How to run your code for training and testing?
Download the colab notebook that you want to run. Upload it in google colab.
Mount the drive and 
