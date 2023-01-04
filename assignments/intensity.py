# https://www.jianshu.com/p/c793a709c93c
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import expon, poisson

# exponential
xy = expon.rvs(scale=1.0,size=[120, 160])
#print(np.mean(xy), np.std(xy), np.sum(xy[xy>4.0]), np.amax(xy))
plt.hist(xy, bins=60, fc='k', ec='k')
plt.savefig("intensity_expon.png", dpi=600, bbox_inches='tight')
plt.show()

# poisson
xy_poisson = poisson.rvs(mu=3, size=20000)
print(xy_poisson)
plt.hist(xy_poisson, bins=60, fc='k', ec='k')
plt.savefig("intensity_poisson.png", dpi=600, bbox_inches='tight')
plt.show()