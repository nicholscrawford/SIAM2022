import math
import numpy as np
import matplotlib.pyplot as plt
import model

initialState = np.zeros((10,10))
initialState[5,5] = 0.1

tempHigh = np.array([94,87,86,97,98,89,92,96,98,99,103,103,97,91])
tempLow = np.array([60,56,55,59,61,61,57,58,59,64,65,64,62,57])
precip = np.zeros((14)) * 0.01
wind = np.array([15,16,12,9,13,17,12,15,10,12,10,9,14,13]) * 1.609 #convert to km/hr
humid = np.array([49.2,57.1,55.2,41.5,40.0,44.1,45.1,42.5,45.3,38.1,34.3,35.3,50.0,56.9])*0.01

testModel = model.firemodel(initialState, tempHigh, tempLow, precip, wind, humid)

states = np.zeros((10,10,9))
states[:,:,0] = testModel.visualize()
testModel.timeStep()
for i in range(8):
    testModel.timeStep()
    states[:,:,i+1] = testModel.visualize()
    '''if testModel.t % 50 == 0:
        states[:,:,math.floor(testModel.t/50)] = testModel.visualize()'''
      
fig, ax = plt.subplots(3,3)

ax[0][0].imshow(states[:,:,0],cmap=plt.get_cmap('inferno'))
ax[0][1].imshow(states[:,:,1],cmap=plt.get_cmap('inferno'))
ax[0][2].imshow(states[:,:,2],cmap=plt.get_cmap('inferno'))
im = ax[1][0].imshow(states[:,:,3],cmap=plt.get_cmap('inferno'))
ax[1][1].imshow(states[:,:,4],cmap=plt.get_cmap('inferno'))
ax[1][2].imshow(states[:,:,5],cmap=plt.get_cmap('inferno'))
ax[2][0].imshow(states[:,:,6],cmap=plt.get_cmap('inferno'))
ax[2][1].imshow(states[:,:,7],cmap=plt.get_cmap('inferno'))
ax[2][2].imshow(states[:,:,8],cmap=plt.get_cmap('inferno'))

fig.colorbar(im)
plt.show()
        
#plt.imshow(testModel.visualize(), cmap=plt.get_cmap('inferno'))
#plt.show