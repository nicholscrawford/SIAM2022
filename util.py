import numpy as np
from scipy.ndimage import convolve
import math

def dayTime(time):
    day = math.floor(time/24)
    hour = time % 24
    return (day, hour)

def findKernel(state,wind,humidity,precip,temp):
    kernel = np.zeros((3,3))
    precipRand = np.random.rand()
    if precipRand < precip:
        kernel[1,1] = 1
        return kernel
    if temp <= 51.61: #dew point
        kernel[1,1] = 1
        return kernel
    kernel[0,0] = wind/(math.sqrt(2)*0.25) #NEED WIND IN km/hr
    
    kernel[0,1] = 0.075
    kernel[1,0] = 0.075
    kernel[1,2] = 0.075
    kernel[2,1] = 0.075
    
    kernel[2,0] = 0.05
    kernel[0,2] = 0.05
    
    kernel[1,1] = 1
    kernel[2,2] = 0.1
    kernel *= humidity
    return kernel

def maskConvolve(state,kernel,mask):
    conv = convolve(state, kernel, mode='constant')
    return np.where(mask, conv, state)


#more physical motivation: wind
#match the question doc: kernel 'numbers'