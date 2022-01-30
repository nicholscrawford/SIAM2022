import math
import numpy as np

e1 = [2109, 3136, 1623, 573, 1205, 1277, 408, 1689]
e2 = [22712, 34864, 17599, 6119, 13332, 13400, 4636, 17850]
e3 = [76165, 115761, 57483, 20105, 43531, 44517, 15493, 58874]

e4 = [76165, 57880.5, 57880.5, 38794, 38794, 22012, 22012, 22012, 22012, 15493, 58874]

e4 = np.array(e4)
e4perc = e4/sum(e4)

newlist = np.zeros(e4perc.shape)
for i in range(len(e4perc)):
    newlist[i] = sum(e4perc[0:i+1])


print(e4perc)
print(newlist)

