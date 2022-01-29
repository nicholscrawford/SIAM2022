import matplotlib
import numpy as np
from scipy.ndimage import convolve
import util

'''features to add:
basic functionality
'''


#initialState: initial fire state matrix
#tempHigh: vector of high temperatures over the next 14 days
#tempLow: vector of low temperatures over the next 14 days
#precipVec: vector of precipitation values (decimal) over the next 14 days
#windVec: vector of wind speeds over the next 14 days (all northwesternly)
#humidVec: vector of humidity values over the next 14 days
#density: tree density
#r: side length of partitions in km
class firemodel: 
    
    def __init__(self, initialState, tempHigh, tempLow, precip, wind, humid, density=0.6, r=0.25):
        #make all basic parameter retrievable
        self.initialState = initialState
        self.tempHighs = tempHigh
        self.tempLows = tempLow
        self.precipVec = precip
        self.windVec = wind
        self.humidVec = humid
        self.density = density
        self.r = r
        
        #mutable state attributes
        self.t = 0
        self.state = initialState
        self.wind = wind[0]
        self.temp = tempLow[0]      #figure this out in more detail later
        self.humid = humid[0]
        self.precip = precip[0]
    def fireSpread(self):
        kernel = util.findKernel(self.state, self.wind, self.humid, self.precip)
        self.state = convolve(self.state, kernel, mode='constant')
        
        #iterate over all matrix entries, randomly determine spread according to temperature, density, humiditiy, wind
    
    
    def timeStep(self):
        #fireSpread and fireGrow; increment t
        pass