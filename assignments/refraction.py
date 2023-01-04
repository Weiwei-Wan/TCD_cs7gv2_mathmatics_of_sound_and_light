from pydoc import doc
from turtle import color
import numpy as np
import matplotlib.pyplot as plt

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
            
#-- Function
# income wave angle
alpha1 = np.pi/5
# refractive index
r1 = 1
r2 = 1.5
# calculate refraction wave angle
alpha2 = np.arcsin(np.sin(alpha1)*r1/r2)
# wave direction coef in our coordinate system
c1 = -np.tan(np.pi/2-alpha1)
c2 = -np.tan(np.pi/2-alpha2)
# wave front interval
inter1 = 2*np.sin(alpha1)
inter2 = 2*np.sin(alpha2)

# income wave 
x1 = np.linspace(-10,-5,100)
y1 = c1*x1+c1*5
x2 = np.linspace(-10,0,100)
y2 = c1*x2
x3 = np.linspace(-4,5,100)
y3 = c1*x3-c1*5
plt.plot(x1, y1, 'k-', linewidth=1.25, alpha=0.5)
plt.plot(x2, y2, 'k-', linewidth=1.25, alpha=0.5)
plt.plot(x3, y3, 'k-', linewidth=1.25, alpha=0.5)
# wave direction arrow
plt.arrow(-10, -10*c1, 5, 5*c1, color = "blue", width = 0.1, linestyle='--')
# wave front
for i in range(0, 5):
    x1 = np.linspace((-7-2*i-5*c1**2)/(1+c1**2), 5-2*(i+6)/(1+c1**2), 100)
    y1 = -x1/c1-(7+i*inter1/np.sin(alpha1))/c1
    plt.plot(x1, y1, 'b-', linewidth=1.25)
    x2 = np.linspace(3-2*i, 5-2*(i+1)/(1+c1**2), 100)
    y2 = -x2/c1+(3-i*inter1/np.sin(alpha1))/c1
    plt.plot(x2, y2, 'b-', linewidth=1.25)
    
# example interface point 
plt.plot([-5,-3,-1,1,3],[0,0,0,0,0],'y.', markersize=15)

# the wave propagation from interface
for i in range(1, 6):
    for j in range(1, 7-i):
        radius = j*inter2
        theta = np.linspace(np.pi, 2*np.pi, 200)
        a = 2*i-7-radius*np.cos(theta)
        b = radius*np.sin(theta)
        plt.plot(a, b, 'k-', linewidth=1.25, alpha=0.3)

# refraction wave 
x4 = np.linspace(-5, -1, 100)
y4 = c2*x4+c2*5
x5 = np.linspace(0, 4, 100)
y5 = c2*x5
x6 = np.linspace(5, 8, 100)
y6 = c2*x6-c2*5
plt.plot(x4, y4, 'k-', linewidth=1.25, alpha=0.5)
plt.plot(x5, y4, 'k-', linewidth=1.25, alpha=0.5)
plt.plot(x6, y6, 'k-', linewidth=1.25, alpha=0.5)
# wave direction arrow
plt.arrow(1, c2, 2, 2*c2, color = "green", width = 0.1)
# wave front
for i in range(0, 6):
    x = np.linspace((5+2*i-5*c2**2)/(1+c2**2), (5+2*i+5*c2**2)/(1+c2**2), 100)
    y = -(x-5-i*inter2/np.sin(alpha2))/c2
    plt.plot(x, y, 'g-', linewidth=1.25)

# save figure
plt.savefig("refraction.png", dpi=600, bbox_inches='tight')
plt.show()