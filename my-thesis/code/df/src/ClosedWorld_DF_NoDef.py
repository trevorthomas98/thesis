#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This code is to implement deep fingerprinting model for website fingerprinting attacks
# ACM Reference Formant
# Payap Sirinam, Mohsen Imani, Marc Juarez, and Matthew Wright. 2018.
# Deep Fingerprinting: Undermining Website Fingerprinting Defenses with Deep Learning.
# In 2018 ACM SIGSAC Conference on Computer and Communications Security (CCS ’18),
# October 15–19, 2018, Toronto, ON, Canada. ACM, New York, NY, USA, 16 pages.
# https://doi.org/10.1145/3243734.3243768


#from keras import backend as K
#from utility import LoadDataNoDefCW
#from Model_NoDef import DFNet
#import random
#from keras.utils import np_utils
#from keras.optimizers import Adamax
#import numpy as np
#import os

#from tensorflow.python.keras import backend as K
from utility import LoadDataNoDefCW
from Model_NoDef import DFNet
import random
#from tensorflow.python.keras import utils
from tensorflow.python.keras.utils.np_utils import to_categorical
#from tensorflow.python.keras.optimizers import Adamax
import numpy as np
import os

random.seed(0)
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
os.environ['AUTOGRAPH_VERBOSITY'] = '1'

# Use only CPU
#os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"   # see issue #152
#os.environ["CUDA_VISIBLE_DEVICES"] = ""

description = "Training and evaluating DF model for closed-world scenario on non-defended dataset"

print (description)
# Training the DF model
NB_EPOCH = 120   # Number of training epoch
print ("Number of Epoch: ", NB_EPOCH)


##################################################################
# Batch Size Information
##################################################################
# Batch Gradient Descent. Batch Size = Size of Training Set
# Stochastic Gradient Descent. Batch Size = 1
# Mini-Batch Gradient Descent. 1 < Batch Size < Size of Training Set
# #########
# In the case of mini-batch gradient descent, popular batch sizes include 32, 64, and 128 samples. 
# You may see these values used in models in the literature and in tutorials.
##################################################################
BATCH_SIZE = 32 # Batch size / recommended no larger than 32

VERBOSE = 2 # Output display mode

#LENGTH = 5000 # Packet sequence length
#LENGTH = 23519 # Packet sequence length
LENGTH = 40000 # Packet sequence length

#OPTIMIZER = Adamax(lr=0.002, beta_1=0.9, beta_2=0.999, epsilon=1e-08, decay=0.0) # Optimizer

#NB_CLASSES = 95 # number of outputs = number of classes = video id = genres
NB_CLASSES = 6 # number of outputs = number of classes = video id = genres

INPUT_SHAPE = (LENGTH,1)


# Data: shuffled and split between train and test sets
print ("Loading and preparing data for training, and evaluating the model")
X_train, y_train, X_valid, y_valid, X_test, y_test = LoadDataNoDefCW()
# Please refer to the dataset format in readme
#K.set_image_dim_ordering("tf") # tf is tensorflow

# Convert data as float32 type
X_train = X_train.astype('float32')
X_valid = X_valid.astype('float32')
X_test = X_test.astype('float32')
y_train = y_train.astype('float32')
y_valid = y_valid.astype('float32')
y_test = y_test.astype('float32')

# we need a [Length x 1] x n shape as input to the DF CNN (Tensorflow)
X_train = X_train[:, :,np.newaxis]
X_valid = X_valid[:, :,np.newaxis]
X_test = X_test[:, :,np.newaxis]

print(X_train.shape[0], 'train samples')
print(X_valid.shape[0], 'validation samples')
print(X_test.shape[0], 'test samples')

# Convert class vectors to categorical classes matrices
y_train = to_categorical(y_train, NB_CLASSES)
y_valid = to_categorical(y_valid, NB_CLASSES)
y_test = to_categorical(y_test, NB_CLASSES)

# Building and training model
print ("Building and training DF model")

model = DFNet.build(input_shape=INPUT_SHAPE, classes=NB_CLASSES)

model.compile(loss="categorical_crossentropy", optimizer='adamax',
	metrics=["accuracy"])

print ("Model compiled")

# Start training
history = model.fit(X_train, y_train,
		batch_size=BATCH_SIZE, epochs=NB_EPOCH,
		verbose=VERBOSE, validation_data=(X_valid, y_valid))


# Start evaluating model with testing data
score_test = model.evaluate(X_test, y_test, verbose=VERBOSE)
print("Testing accuracy:", score_test[1])


