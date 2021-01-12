import matplotlib.pyplot as plt 

import numpy as np 

x= [0,30,60,0,60,0]
y = [0,500,0,300,300,0]
for z in range(20):
	x.append(z*3)
	y.append(300)
xpoint = np.array(x)
ypoint = np.array(y)
plt.plot(xpoint, ypoint,'o:r',ms = 20)
plt.show()