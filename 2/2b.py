import matplotlib.pyplot as plt
import numpy as np
n=np.arange(1,10)
a=n
b=n**2
plt.plot(n,a)
plt.plot(n,b)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()