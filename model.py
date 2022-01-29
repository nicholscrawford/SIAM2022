import matplotlib
import numpy as np
import util

'''features to add:
stochastic elements
-wind speed/direciton
-temperature
-precipitation
-humidity
'''
#initialState: initial fire state matrix
#tempHigh: vector of high temperatures over the next 14 days
#tempLow: vector of low temperatures over the next 14 days
#precipVec: vector of precipitation values (decimal) over the next 14 days
#windVec: vector of wind speeds over the next 14 days (all southeasternly)
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
        self.mask = np.ones(initialState.shape)
    def fireSpread(self):
        kernel = util.findKernel(self.state, self.wind, self.humid, self.precip, self.temp) #calculate kernel for convolution
        self.state = util.maskConvolve(self.state, kernel, self.mask) #convolve but skipping burnt out cells
        self.burnout() #check if any regions are over 100% burned
    
    def burnout(self):
        for i in range(self.state.shape[0]):
            for j in range(self.state.shape[1]):
                if self.state[i,j] >= 1:
                    self.state[i,j] = 0
                    self.mask[i,j] = 0
                    
    def updateTemp(self):
        day, hour = util.dayTime(self.t)
        highT = self.tempHighs[day]
        lowT = self.tempLows[day]
        lowT_new = self.tempLows[day+1]
        if hour < 8:
            self.temp = lowT + hour * (highT - lowT)/8
        else:
            self.temp = highT + (hour - 8) * (lowT_new - highT)/16
    
    def timeStep(self):
        self.fireSpread()
        self.t += 1
        
    def visualize(self):
        return self.state + (1-self.mask)