# Udacity Machine Learning Nanodegree

This is my  final capstone project.


Software requirements:

- Capstone Project: Anaconda python 2.7, Python Pillow, Tensorflow r.012


# Better Model for SVHN
After finishing my Udacity ML nanodegree I played around with the SVHN model and do more data augmentation. At the end I increased the size of the first Conv layer from 16 to 32 and train the model with large data augmentation one million steps  on a Titan X Pascal (about a week!). Finally I achieved test accuracy character level: 98.55%!! and Test accuracy for the whole number: 96.00%!! Notebooks:
- svhn_cnn_32x32_FINAL.ipynb: this notebook do trhe data augmentation and train the model. You need a machine with 64GB RAM and a very fast GPU (Titan X Pascal, K80 and so on)
- svhn_cnn_32x32_bestl_model.ipynb loads the best model and shows some results.  You will see in some cases the ground true label is wrong and the model is right!
- added U-Net segmentation to find the location of a house number on an image. Preprocessing the data is in svhn_load_preprocess_for_regression.ipynb, U-Net training and application on the test data is in svhn-unet.ipynb. This notebook finally saves cropped images of the detected house numbers to an h5 file, which is loaded and applied in the Notebook svhn_cnn_32x32_bestl_model.ipynb. Since the detection if the house number location has only 79% accuracy we can't expect that the CNN network will achieve 96% accurray, but we get 76,67% accuracy. So we finally have the pieces of a processing pipeline to detect and to classify a house number on an image. Because the U-Net can detect more than one house number on an image it would work for this too.  The U-Net house number detection is quite fast: about 13000 images in about 7 seconds!
