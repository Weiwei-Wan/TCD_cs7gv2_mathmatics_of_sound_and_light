from pickle import TRUE
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation

#-- Function
# k constant value of spring
k = 100
# mass of the object
m = 10
# max distance
x = 5 
# damper value
c = 2

# give a random range of x
interval = 1000
t = np.linspace(0, 10, interval)

delta_t = 10/interval

y = np.zeros(interval) 

for i in range(0, interval):
    if i == 0:
        y[i] = x
    elif i == 1:
        y[i] = x - k*x*delta_t*delta_t/(2*m)
    else:
        y[i] = (-y[i-1]*k*delta_t*delta_t + c*delta_t*y[i-2]/2+m*(2*y[i-1]-y[i-2]))/(m+c*delta_t/2)

def data_gen():
    for i in range(0, interval):
        yield t[i], y[i]

def init():
    del xdata[:]
    del ydata[:]
    ax.set_ylim(-6, 6)
    ax.set_xlim(0, 12)
    ax.spines["right"].set_color("none")
    ax.spines["top"].set_color("none")
    ax.spines["bottom"].set_position(("data", 0))
    return line

def run(data):
    # update the data
    t, y = data
    xdata.append(t)
    ydata.append(y)
    xmin, xmax = ax.get_xlim()
    if t >= xmax:
        ax.set_xlim(xmin, 2*xmax)
        ax.figure.canvas.draw()
    line.set_data(xdata, ydata)
    return line

fig, ax = plt.subplots()
plt.axis([0, 12, -6, 6])
ax.spines["right"].set_color("none")
ax.spines["top"].set_color("none")
ax.spines["bottom"].set_position(("data", 0))

line, = ax.plot([], [], lw=2)

xdata, ydata = [], []

ani =  animation.FuncAnimation(fig, run, data_gen, blit=False, interval=2, repeat=False, init_func=init,save_count=500)

plt.show()
