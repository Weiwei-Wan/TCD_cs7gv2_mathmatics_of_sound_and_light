from pydoc import doc
from turtle import color
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# axes setting 
# set axes scale [x_left, x_right, y_down, y_up]
plt.axis([-16, 16, -12, 12])
# Get current axis
ax = plt.gca()
# hide the extra 2 axes
ax.spines["right"].set_color("none")
ax.spines["left"].set_color("none")
ax.spines["top"].set_color("none")
# hide the ticks
ax.xaxis.set_ticks([])
ax.yaxis.set_ticks([])
# set the axes origion point
ax.spines["bottom"].set_position(("data", 0))
# Set the aspect of the axis scaling
ax.set_aspect(1)

# (x,y), width, height
ax.add_patch(patches.Rectangle(xy=(-16, 0), width=10, height=0.7, color="#666666"))
ax.add_patch(patches.Rectangle(xy=(6, 0), width=10, height=0.7, color="#666666"))

#-- Function
# income wave 
x = np.linspace(-10,10,100)
y1 = np.linspace(1,1,100)
y2 = np.linspace(2,2,100)
y3 = np.linspace(3,3,100)
plt.plot(x, y1, color="#2e2d88", linewidth=2, alpha=1)
plt.plot(x, y2, color="#2e2d88", linewidth=2, alpha=1)
plt.plot(x, y3, color="#2e2d88", linewidth=2, alpha=1)
#wave arrow
plt.arrow(0, 10, 0, -8, color="#2e2d88", width = 0.1, linestyle='--')

# the wave propagation from aperture
for i in range(0, 6):
    for j in range (1, 8):
        a = np.linspace(5-2*i-2/3*j,5-2*i+2/3*j,100)
        f = lambda a:(4/9*j*j-(a-5+2*i)**2)**0.5
        b = f(a)
        plt.plot(a, -b, color="#83888e", linewidth=2, alpha=0.5)

# example interface point 
plt.plot([-5,-3,-1,1,3,5],[0,0,0,0,0,0],'y.', markersize=15)

# save figure
plt.savefig("difraction.png", dpi=1200, bbox_inches='tight')
plt.show()

