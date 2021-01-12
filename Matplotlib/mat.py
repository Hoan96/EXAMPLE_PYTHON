import matplotlib.pyplot as plt 

import numpy as np 


xpoint = np.array([0,30,60,0,60,0])
ypoint = np.array([0,500,0,300,300,0])
plt.plot(xpoint, ypoint,'*:r',ms = 20)
plt.show()