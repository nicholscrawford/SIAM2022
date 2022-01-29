import numpy as np
from scipy.ndimage import convolve

def findKernel(state,wind,humidity,precip): 
    kernel = np.ones((3,3))
    return kernel

def maskConvolve(state,kernel,mask):
    conv = convolve(state, kernel, mode='constant')
    return np.where(mask, conv, state)