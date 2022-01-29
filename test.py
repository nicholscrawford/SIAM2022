import numpy as np
import matplotlib.pyplot as plt
import model
import time

initialState = np.zeros((36,88))
initialState[18,44] = 0.1

tempHigh = np.array([94,87,86,97,98,89,92,96,98,99,103,103,97,91])
tempLow = np.array([60,56,55,59,61,61,57,58,59,64,65,64,62,57])
precip = np.zeros((14))
wind = np.array([15,16,12,9,13,17,12,15,10,12,10,9,14,13])
humid = np.array([49.2,57.1,55.2,41.5,40.0,44.1,45.1,42.5,45.3,38.1,34.3,35.3,50.0,56.9])

testModel = model.firemodel(initialState, tempHigh, tempLow, precip, wind, humid)

plt.figure(1)
plt.imshow(testModel.state, cmap=plt.get_cmap('inferno'))
plt.show
for i in range(7):
    testModel.timeStep()
    #print(testModel.state)
    
    plt.figure(i+2)
    plt.imshow(testModel.state, cmap=plt.get_cmap('inferno'))
    plt.show