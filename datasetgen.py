import cv2
import time
import random
import numpy as np
import matplotlib.pyplot as plt

def generate_images(n):
  for i in range(n):
    s = "image"+str(i)+".png"
    imarray = np.random.rand(100,100,3) * 255
    im = Image.fromarray(imarray.astype('uint8')).convert('RGBA')
    im.save(s)
