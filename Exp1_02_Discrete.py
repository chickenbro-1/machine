import matplotlib.pyplot as plt
import numpy as np
fig = plt.figure()
n=np.arange(-5,5)
f= 2*(0.8)**n
plt.stem(n,f)
plt.show()