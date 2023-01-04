import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()

x_max = 9
x_min = -4
y_max = 4
n = 1

# set the axes
ax.set_xlim(x_min, x_max)
ax.set_ylim(-y_max-1, y_max+1)
# hide the extra 2 axes
ax.spines["right"].set_color("none")
ax.spines["top"].set_color("none")

# set the axes origion point
ax.spines["bottom"].set_position(("data", 0))
ax.spines["left"].set_position(("data", 0))

x_temp = np.linspace(x_max, x_max, 100)
y_temp = np.linspace(-y_max-1, y_max+1, 100)
plt.plot(x_temp, y_temp, 'k-',linewidth=3)


x1 = np.linspace(x_min, x_max, 500)
y1 = []
for i in range(len(x1)):
    if x1[i] < 0:
        y1.append(x1[i]-x_min)
    else:
        y1.append(y_max-(y_max/x_max)*x1[i])

y1 = np.array(y1)

#-- Function
def init():
    line.set_data(x1, y1)
    return line,

# Motion of Plucked String
def update(frame):
    x = np.linspace(x_min, x_max, 500)
    y = []
    for i in range(len(x)):
        a = 0
        for j in range(n):
            a += 2*y_max*((x_max-x_min)**2)*np.sin(-x_min*(j+1)*np.pi/(x_max-x_min))/(x_max*(-x_min)*((np.pi*(j+1))**2))
        tem = a*np.sin(n*np.pi*x[i]/(x_max-x_min))*np.cos(0.3*np.pi*n*frame/(x_max-x_min))
        y.append(tem)

    y = np.array(y)
    line.set_data(x, y)
    return line,

line, = ax.plot([], [], lw=2)

ani = FuncAnimation(fig, update, frames=2000, interval=100, init_func=init, blit=True)

plt.show()



