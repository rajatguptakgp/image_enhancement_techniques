# Image Restoration Techniques

***
## Overview
This work is about removing noise/haze from noisy/hazy images to obtain clearer images using stacked autoencoders.

## Results

This work is a result of participation in (New Trends in Image Restoration and Enhancement workshop) **NTIRE 2020 Real Image Denoising Challenge - Track2 – sRGB**, in conjunction with (Conference on Computer Vision and Pattern Recognition) **CVPR 2020, Seattle, US**.

Participation in NTIRE 2020 Denoising Challenge led my team secure **16th** position among **250+** registrants. [Publication Link](https://arxiv.org/abs/2005.04117)

This work also discusses implementation on **Image Dehazing** as an extension to the original work on Image Denoising. Lastly, it compares the approach with State of the art approaches on Image Translation tasks - CycleGAN and Pix2Pix. 

| Technique | Model  | Epochs | Mean PSNR | Mean SSIM |
| :---:   | :-: | :-: | :-: | :-: |
| Denoising | Stacked Autoencoder | 1000 | 26.95 | 0.78 |
| Dehazing | Stacked Autoencoder | 500 | 10.24 | 0.54 |
| Dehazing | CycleGAN | 1000 | 13.44 | 0.54 |
| Dehazing | Pix2Pix | 1000 | 15.96 | 0.60 |

From the results, we can conclude that our basic PyTorch implementation has been able to perform quite well compared to state-of-the-art approaches - CycleGAN and Pix2Pix.

## Dependencies
 - PyTorch
 - OpenCV
 
 ## Installation
 - To install PyTorch, see installation instructions on the PyTorch website.
 - To install OpenCV: `pip install opencv-python`
 
## Dataset

Image Denoising
- This work makes use of the Smartphone Image Denoising Dataset+ [SIDD+](https://arxiv.org/abs/1710.03957). The data was made available on the Codalab website where the competition was hosted.

Image Dehazing
- This work makes use of [Dense-Haze](https://arxiv.org/abs/1904.02904) dataset. 

## Data Preprocessing
The data in original forms are extremely high resolution images. Due to lack of computing resources, the images have been down-sized to 256 pixels.

### For Image Denoising
- Use the `make_data_vseq2seq.py` script to process the data splits (train, validation and test) into a CSV file.

### For HRED
- Use the `make_data_hred.py` script to process the data splits (train, validation and test) into a CSV file. Additional samples for each dialog have been created since they have generic responses and also because the number of dialogs is less, which may not be enough to train the model effectively. 

## Reference
* [PyTorch Seq2Seq](https://github.com/bentrevett/pytorch-seq2seq)
 
