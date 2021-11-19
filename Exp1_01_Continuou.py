import matplotlib.pyplot as plt
import numpy as np
fig = plt.figure()
t = np.arange(0.0, 5.0, 0.0001)
x = 5*(np.exp((-0.8)*t))*(np.sin(np.pi*t))
fig, ax = plt.subplots()
ax.plot(t, x, label='Exp1_01_Continuou')
plt.show()
