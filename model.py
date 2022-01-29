import matplotlib
import numpy as np

#initialState: initial fire state matrix
#tempHigh: vector of high temperatures over the next 14 days
#tempLow: vector of low temperatures over the next 14 days
#precip: vector of precipitation values (decimal) over the next 14 days
#wind: vector of wind speeds over the next 14 days (all northwesternly)
#humid: vector of humidity values over the next 14 days
#density: tree density
#r: side length of partitions in km
class firemodel: 
    
    def __init__(self, initialState, tempHigh, tempLow, precip, wind, humid, density=0.6, r=0.25):
        #make all basic parameter retrievable
        self.initialState = initialState
        self.tempHigh = tempHigh
        self.tempLow = tempLow
        self.precip = precip
        self.wind = wind
        self.humid = humid
        
        #mutable state attribute
        self.state = initialState
    
    def fireSpread(self):
        #iterate over all matrix entries, randomly determine spread according to temperature, density, humiditiy, wind
        pass
    
    def fireGrow(self):
        #iterate over all matrix entries, increase fire levels according to temperature, density, humidity; check for burnout
        pass
    
    def timeStep(self):
        #fireSpread and fireGrow
        pass