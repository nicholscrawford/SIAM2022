import numpy as np
import matplotlib.pyplot as plt
import model
from evacsim import evaczone
from evacsim import path
from evacsim import neighborhood


initialState = np.zeros((100,200))
initialState[49,57] = 0.1
#city is at initialState[46:54,125:142]
burnTimes = np.zeros((8,17))

tempHigh = np.array([94,87,86,97,98,89,92,96,98,99,103,103,97,91])
tempLow = np.array([60,56,55,59,61,61,57,58,59,64,65,64,62,57])
precip = np.zeros((14)) * 0.01
wind = np.array([15,16,12,9,13,17,12,15,10,12,10,9,14,13]) * 1.609 #convert to km/hr
humid = np.array([49.2,57.1,55.2,41.5,40.0,44.1,45.1,42.5,45.3,38.1,34.3,35.3,50.0,56.9])*0.01

testModel = model.firemodel(initialState, tempHigh, tempLow, precip, wind, humid)

for i in range(336):
    testModel.timeStep()
    for j in range(8):
        for k in range(17):
            if testModel.state[j+46,k+125] != 0:
                burnTimes[j,k] = i + 1

fig, ax = plt.subplots()
im = plt.imshow(burnTimes,cmap=plt.get_cmap('RdBu'))
fig.colorbar(im)
plt.show()
#fig, ax1 = plt.imshow(burnTimes,cmap=plt.get_cmap('inferno'))

#Run simulation
totalpeople = 1000

#Create paths and neighborhoods
end = evaczone()

paths = {}

paths["a"] = path(0.354, 35, end)
paths["b"] = path(0.172, 35, paths["a"])
paths["c"] = path(0.072, 35, paths["b"])
paths["d"] = path(0.175, 25, paths["c"])
paths["e"] = path(0.197, 25, paths["c"])
paths["f"] = path(0.091, 25, paths["e"])
paths["g"] = path(0.175, 25, paths["f"])

neighborhoods = {}
neighborhoods["17,1"] = neighborhood(30, paths["b"])
neighborhoods["16,1"] = neighborhood(30, paths["e"])
neighborhoods["16,2"] = neighborhood(30, paths["g"])
neighborhoods["17,2"] = neighborhood(30, paths["d"])

#Evaccomplete > 0 means not all are evacuated.
evaccomplete = 1
#Run timesteps, check if everyone is evacuated.
while evaccomplete > 0:
    for n in neighborhoods:
        neighborhoods[n].timestep()
    for p in paths:
        paths[p].timestep()
    
    evaccomplete = 0
    
    for n in neighborhoods:
        evaccomplete += not neighborhoods[n].isempty()
    for p in paths:
        evaccomplete += not paths[p].isempty()
