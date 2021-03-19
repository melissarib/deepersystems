# Overview

The purpose of this task is to test your knowledge and capabilities using neural networks and basic computer vision to solve problems. 

# Speed & Functionality

This test is about getting 1. **a functional solution** and 2. **as fast as possible**. 

This is **not** about code quality. The neural network should get a highly accurate result, but we'll be far more impressed if it takes you 1 hour to code minimal data processing and net training scripts rather than 5 hours of a perfectly modular, 'future-proof' solution with full docstrings etc. 

The clock is already ticking! Create a github repository and make an empty initial commit **right now**. As soon as you are done coding (**before** fully training the net), commit the code to the repository. We'll look at the timings of the commits as part of the evaluation. 

If you wait until your net is fully trained to submit your code **you will be disadvantaged** compared to the other applicants as we will have to consider your total time spent (including waiting for nets to train) as part of your coding time.

# The Task

Oh no! Our facial recognition data-set got all jumbled up. We have thousands of images, but some of them have been 
rotated left, rotated right, and turned upside-down! 

The upright images are like this:

![upright](https://imgur.com/WY6x3RG.jpg)

And some have been jumbled up like this:

![rotated_left](https://imgur.com/JWdJl0B.jpg)
![rotated_right](https://imgur.com/73Obelm.jpg)
![upside_down](https://imgur.com/mFUm3E8.jpg)

The task is to create a neural network which takes an image of a face as input and returns its orientation - `upright`, 
`rotated_left`, `rotated_right`, or `upside_down` - and use this neural network to correct the images in the test set.

**Use Keras's [CIFAR10-CNN model example](https://github.com/keras-team/keras/blob/88ca804d94a0f978d0522d82a2e2bda26362076a/examples/cifar10_cnn.py) as a starting point.** You must include a result that used this model. 

If you want to make your own model or make improvements from there, include your results both for the CIFAR10 model and for your (better-performing) model... but you will want to first submit your results with the CIFAR10 model so we can take that timing into account.

## Data Format

### Inputs

The input is a folder full of images.

### Ground Truth

The ground truth is a CSV with the image file-name and the label for it, for example:

```
fn,label
0-10049200_1891-09-16_1958.jpg,rotated_left
0-10110600_1985-09-17_2012.jpg,rotated_left
0-10126400_1964-07-07_2010.jpg,rotated_left
0-1013900_1917-10-15_1960.jpg,upside_down
0-10166400_1960-03-12_2008.jpg,upright
0-102100_1970-10-09_2008.jpg,rotated_left
0-1024100_1982-06-07_2011.jpg,rotated_right
```

## Training Data

The training data is a set of images and the ground truth for them.

[**Download Link**](https://www.dropbox.com/s/lbobq9xt3nchq5q/train.rotfaces.zip?dl=0)

## Test Data

The test data is a set of images without the ground truth.

[**Download Link**](https://www.dropbox.com/s/ustfubunhfe47mj/test.rotfaces.zip?dl=0)

## Evaluation

You will be evaluated based on how many images were correctly classified. **You must submit a test.preds.csv which we can
use the attached `eval.py` to run with** - the preds file format is the same as the ground truth:

    python eval.py test.truth.csv test.preds.csv

You should be able to get 90%+ on your training set, and we'll expect a similar result when we evaluate your submission
on the test set.

### Zip Output

Additionally you need to submit a zip file of the truth images with the corrected orientations, as best as you can given 
how well your neural net performs.  For example, this test set image:
  
![broken](https://i.imgur.com/BL3LsDq.jpg)
  
Would be corrected to:
  
![fixed](https://i.imgur.com/YS5I71c.jpg)
  
Note they don't have to be 100% correct, you just have to use your neural net's predictions to rotate the faces.

### Numpy Output

As a last step, you should save all of the **corrected orientation** faces into one numpy array file. This is a standard format that is used as input to further neural networks we might want to train on the data.

For clarity, the numpy array file should have shape (5361, 64, 64, 3).

# Submission

When you are done, submit the following, in a GitHub repository:

* Your prediction csv file on the test data in the correct format , using the CIFAR10 model.
* [optional] Any prediction csv files on the test data from model you made or improved yourself.
* A zip file of the test set images, **as PNGs**, with the corrected orientations.  
* All the code needed to train and run your network to produce that prediction from
  scratch, along with instructions on how to run the code
* A short description, in English, of the approach you took and how you arrived at the solution 
  you did
* A few notes on the next steps you would take to improve the model even further

Good luck!
