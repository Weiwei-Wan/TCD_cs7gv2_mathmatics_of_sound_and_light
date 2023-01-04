# https://www.acs.psu.edu/drussell/Demos/waves/wavemotion.html
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

xy = np.random.uniform(-20, 20, (5000,2))
# set up parameters
wave_length = 5
w = 1/20
R = 0.8
k = 2*np.pi/wave_length

# def animate(frame):
#     xy2 = np.copy(xy)   
#     for i in range(len(xy2)):
#         x = xy2[i][0]
#         #update patical position use R cos(kx − ωt) + (1 − R) cos(kx + ωt)
#         p = R*np.sin(k*x-w*frame)
#         xy2[i][1] += p
#     sc.set_offsets(np.c_[xy2[:,0], xy2[:,1]])

# xy2 = np.copy(xy)       
# fig,ax = plt.subplots()
# sc = ax.scatter(xy2[:,0], xy2[:,1], s=10, c="k")
# plt.ylim(-5, 5)

# ani = FuncAnimation(fig, animate, frames=5000, interval=50)
# #ani.save('transverse_wave.gif',writer='imagemagick')
# plt.show()

#%%
def longitudinal_wave(frame):
    xy2 = np.copy(xy)   
    for i in range(len(xy2)):
        x = xy2[i][0]
        #update patical position use R cos(kx − ωt) + (1 − R) cos(kx + ωt)
        p = R*np.cos(k*x - w*frame) + (1 - R)*np.cos(k*x + w*frame)
        #p = R*np.sin(k*x-w*frame)
        xy2[i][0] += p
    sc.set_offsets(np.c_[xy2[:,0], xy2[:,1]])

xy2 = np.copy(xy)       
fig,ax = plt.subplots()
sc = ax.scatter(xy2[:,1], xy2[:,0], s=10, c="k")
plt.ylim(-20, 20)

ani = FuncAnimation(fig, longitudinal_wave, frames=2000, interval=20)
#ani.save('longitudinal_wave.gif',writer='imagemagick')
plt.show()