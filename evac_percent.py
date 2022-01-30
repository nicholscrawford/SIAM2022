import math
import numpy as np

e1 = [2109, 3136, 1623, 573, 1205, 1277, 408, 1689]
e2 = [22712, 34864, 17599, 6119, 13332, 13400, 4636, 17850]
e3 = [76165, 115761, 57483, 20105, 43531, 44517, 15493, 58874]

e1 = np.array(e1)
e1perc = e1/sum(e1)

newlist = np.zeros(e1perc.shape)
for i in range(len(e1perc)):
    newlist[i] = sum(e1perc[0:i+1])


print(e1perc)
print(newlist)

