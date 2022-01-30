import numpy as np
import matplotlib.pyplot as plt

grid = np.zeros((100,200))
grid[49,57] = 0.8
grid[46:54,125:142] = 0.2


plt.imshow(grid,cmap=plt.get_cmap('gnuplot2'))