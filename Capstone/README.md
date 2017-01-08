# Street View House Numbers
## Udacity Capstone by Thomas Tilli
## Files

- svhn_load_preprocess.ipynb : Downloads and preprocesses files used for training of  the Convolutional Nerural Networks (CNN) Classifier for house number recognition
- svhn_load_preprocess_for_regression.ipynb:  Downloads and preprocesses files used for training of  the Convolutional Nerural Networks (CNN) Regression model for house number localization. 
- svhn_cnn54x54.ipynb: code for several CNN models for 54x54 images.
- svhn_cnn32x32.ipynb: code for several CNN models for 54x54 images. Here you can find also the code and parameter settings for the best model.
- svhn_regression_cnn.ipynb: code for several CNN models for locatization of house numbers.
- svhn_cnn_32x32_final_model.ipynb: code for loading the best trained model and to apply it to some test data sets. 
- Street View House Numbers Recognition.pdf: Dokumentation of the project.

## Important Notes
- Due to some memory management issues of Tensorflow I was forced to use the same function name for  all functions for CNN models within one IPython notebook with 
- The best model is to large to be uploaded to GitHub (>200MB). You must created that by traing.

## Software Requirements
Anaconda python 2.7, Python Pillow, Tensorflow r.012
## Hardware Requirements
A fast machines with at least 64GB RAM! And a fast GPU with a least 8 GB RAM, eg. GTX 1080, GTX Titan X, K80 or similar. Not even try to run this models on a CPU it will takes weeks at best
 
