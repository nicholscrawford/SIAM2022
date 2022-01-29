import numpy as np
from scipy.ndimage import convolve

def findKernel(state,wind,humidity,precip): 
    kernel = np.zeros((3,3))
    kernel[0,0] = wind/15
    kernel[0,1] = 0.5
    kernel[1,0] = 0.5
    kernel[1,2] = 0.5
    kernel[2,1] = 0.5
    
    return kernel

def maskConvolve(state,kernel,mask):
    conv = convolve(state, kernel, mode='constant')
    return np.where(mask, conv, state)