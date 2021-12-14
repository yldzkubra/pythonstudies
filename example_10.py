import matplotlib.pyplot as plt
import numpy as np

boyList=range(145,218,8)
kiloList=range(35,126,10)

xpoints = np.array(boyList)
ypoints = np.array(kiloList)

font = {'family':'serif','color':'green','size':10}

plt.xlabel("boy değerleri",fontdict = font)
plt.ylabel("kilo değerleri",fontdict = font)

plt.grid()

plt.plot(xpoints, ypoints ,color = 'b',marker='o')
plt.show()

