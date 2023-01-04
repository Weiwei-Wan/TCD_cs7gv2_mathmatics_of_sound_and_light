import numpy as np
import matplotlib
import matplotlib.pyplot as plt

# set axes scale [x_left, x_right, y_down, y_up]
plt.axis([-4*np.pi, 4*np.pi, -2, 2])

# Get current axis
ax = plt.gca()

# hide the extra 2 axes
ax.spines["right"].set_color("none")
ax.spines["top"].set_color("none")

# hide the ticks
ax.xaxis.set_ticks([])
ax.yaxis.set_ticks([])

# set the axes origion point
ax.spines["bottom"].set_position(("data", 0))
ax.spines["left"].set_position(("data", 0))

# Set the aspect of the axis scaling
ax.set_aspect(3.5)

# 2 axes arrow
# xytext: The position (x, y) to place the text // "$x$" : LaTex
arrowproperty = dict(facecolor='black', arrowstyle = "<|-")
ax.annotate('$x$', xy=(1, 0), xycoords=('axes fraction', 'data'), 
            xytext=(20, 0), textcoords='offset points',
            ha='left', va='center',arrowprops=arrowproperty)

ax.annotate('$A$', xy=(0, 1), xycoords=('data', 'axes fraction'), 
            xytext=(0, 20), textcoords='offset points',
            ha='center', va='bottom', arrowprops=arrowproperty)

# Function
# numpy.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None, axis=0)
x_right = np.linspace(0, 4*np.pi, 396)
y_right = np.sin(x_right+5/6*np.pi)
plt.plot(x_right, y_right, 'k--',linewidth=1)

x_left = np.linspace(-4*np.pi, 0, 396)
y_left = np.sin(x_left+1/6*np.pi)
plt.plot(x_left, y_left, 'k--',linewidth=1)

x_right_de = np.linspace(-1/3*np.pi, 4*np.pi, (396+33))
y_right_de = np.sin(x_right_de+0.5*np.pi)
plt.plot(x_right_de, y_right_de, 'k:',markersize=1)

x_left_de = np.linspace(-4*np.pi, -1/3*np.pi, (396-33))
y_left_de = np.sin(x_left_de+7/6*np.pi)
plt.plot(x_left_de, y_left_de, 'k:',markersize=1)

# save figure
plt.savefig("/Users/wanjiang/Documents/TCD/cs7gv2_mathmatics_of_sound_and_light/assignment_1/q1_decrease.png", dpi=1200, bbox_inches='tight')

# show figure
plt.show()

