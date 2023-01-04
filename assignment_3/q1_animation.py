# %%
from email.base64mime import header_length
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation
from matplotlib import cm, rcParams

# 
y = np.linspace(0, 4*np.pi, 200)
x_1 = 200*[0]
z_1 = np.sin(y)

# build a 3d system
ax = plt.subplot(111, projection='3d')  

# set the axes
ax.set_xlim(-2, 2)
ax.set_ylim(0, 13)
ax.set_zlim(-2, 2)

# plot the direction of electromatic radiation
plt.plot(x_1, y, x_1, "k-")
arrow = ax.quiver(0, 0, 0, 0, 4*np.pi+1, 0, fc='k', ec='k', length=1)
plt.plot(x_1, y, z_1, 'b-')
plt.plot(z_1, y, x_1, 'r-')

# we simply plot an empty line: we'll add data to the line later
'''
line, = ax.plot([], [], [], lw=2)

def init():
    line.set_data([], [], [])
    return line,

def animate(i):
    z_1 = np.sin(y+i*0.01)
    line.set_data(x_1, y, z_1)
    return line,
anim = FuncAnimation(fig, animate, init_func=init,frames=200, interval=20, blit=True)
'''

# draw the arrows
for i in range(0, 4):
    for j in range(1, 5):
        arrow = ax.quiver(0, np.pi*(i+j/5), 0, 0, 0, np.sin(np.pi*(i+j/5)), fc='b', ec='b')
        arrow = ax.quiver(0, np.pi*(i+j/5), 0, np.sin(np.pi*(i+j/5)), 0, 0, fc='r', ec='r')
        
# set the axes label
ax.set_zlabel('z')  # 坐标轴
ax.set_ylabel('y')
ax.set_xlabel('x')

# hide the ticks
ax.xaxis.set_ticks([])
ax.yaxis.set_ticks([])
ax.zaxis.set_ticks([])

# rotate the 3d view direction
elev, azim = 45, 30
ax.view_init(elev, azim) 

# remove the grid
ax.grid(False)

plt.show()

