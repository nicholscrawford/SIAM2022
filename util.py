import numpy as np
from scipy.ndimage import convolve

def findKernel(state,wind,humidity,precip):
    kernel = np.zeros((3,3))
    kernel[0,0] = wind/20
    kernel[0,1] = wind/40
    kernel[1,0] = wind/40
    kernel[1,2] = 0.1
    kernel[2,1] = 0.1
    kernel[1,1] = 1
    kernel[2,2] = 0.1
    kernel *= humidity
    kernel *= (1-precip)
    return kernel

def maskConvolve(state,kernel,mask):
    conv = convolve(state, kernel, mode='constant')
    return np.where(mask, conv, state)