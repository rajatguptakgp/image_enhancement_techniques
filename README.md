# Image Restoration Techniques

***
## Overview
This work is about removing noise/haze from noisy/hazy images to obtain clearer images using stacked autoencoders.

## Results

The work is a result of participation in (New Trends in Image Restoration and Enhancement workshop) **NTIRE 2020 Real Image Denoising Challenge - Track2 – sRGB**, in conjunction with (Conference on Computer Vision and Pattern Recognition) **CVPR 2020, Seattle, US**.

Participation in NTIRE 2020 Denoising Challenge led my team secure **16th** position among **250+** registrants. [Publication Link](https://arxiv.org/abs/2005.04117)

Further work was done on the same post that. This work also discusses implementation on **Image Dehazing** as an extension to the original work on Image Denoising. Lastly, it compares our approach with two state of the art approaches on Image Translation tasks - CycleGAN and Pix2Pix. 

| Technique | Model  | Epochs | Mean PSNR | Mean SSIM |
| :---:   | :-: | :-: | :-: | :-: |
| Denoising | Stacked Autoencoder | 1000 | 26.95 | 0.78 |
| Dehazing | Stacked Autoencoder | 500 | 10.24 | 0.54 |
| Dehazing | CycleGAN | 1000 | 13.44 | 0.54 |
| Dehazing | Pix2Pix | 1000 | 15.96 | 0.60 |

From the results, we can conclude that our basic PyTorch implementation has been able to perform quite well compared to two state-of-the-art approaches for Image Translation tasks - CycleGAN and Pix2Pix.

## Dependencies
 - PyTorch
 - OpenCV
 
 ## Installation
 - To install PyTorch, see installation instructions on the PyTorch website.
 - To install OpenCV: `pip install opencv-python`
 
## Dataset

### Image Denoising
- This work makes use of the Smartphone Image Denoising Dataset [SIDD](https://www.eecs.yorku.ca/~kamel/sidd/). The data was made available on the Codalab website where the competition was hosted.

### Image Dehazing
- This work makes use of [Dense-Haze](https://arxiv.org/abs/1904.02904) dataset for the purpose of Image Dehazing. 

## Data Preprocessing
The data in original forms are extremely high resolution images. Due to lack of computing resources, for training purposes, the images have been down-sized to 256 pixels.

### For Image Denoising
- Use the `denoising_make_data.py` script to process images and convert them to a numPy array (.npy) file.

### For Image Dehazing
- Use the `dehazing_make_data.py` script to process images and convert them to a numPy array (.npy) file. 

## References
* [Denoising Autoencoder](https://github.com/GunhoChoi/Kind-PyTorch-Tutorial/blob/master/07_Denoising_Autoencoder/Denoising_Autoencoder.ipynb)
* [CycleGAN & Pix2Pix (Official)](https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix)

 
