#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os 
import cv2
import numpy as np
from tqdm import tqdm

REBUILD_DATA=True

class Denoising():
    IMG_SIZE=256 
    label_dir='dataset/' #dataset directory
    training_data=[]
    
    def make_training_data(self):
        for f in tqdm(os.listdir(self.label_dir)):
            
            try:
                path=os.path.join(self.label_dir,f)
                img=cv2.resize(img,(self.IMG_SIZE,self.IMG_SIZE))
                self.training_data.append(np.array(img))

            except Exception as e:
                pass
            
        np.save('training_data.npy',self.training_data)
        
if (REBUILD_DATA):
    denoising=Denoising()
    denoising.make_training_data()

