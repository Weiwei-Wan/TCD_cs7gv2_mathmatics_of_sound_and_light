import numpy as np
import matplotlib
import matplotlib.pyplot as plt

# set axes scale [x_left, x_right, y_down, y_up]
plt.axis([0, 12, -6, 6])

# Get current axis
ax = plt.gca()

# hide the extra 2 axes
ax.spines["right"].set_color("none")
ax.spines["top"].set_color("none")

# set the axes origion point
ax.spines["bottom"].set_position(("data", 0))

# Set the aspect of the axis scaling
#ax.set_aspect(1)
            
#-- Function
# k constant value of spring
k = 100
# mass of the object
m = 10
# max distance
x = 5 
# damper value
c = 3

# give a random range of x
interval = 1000
t = np.linspace(0, 10, interval)

delta_t = 10/interval

y = np.zeros(interval) 
y[0] = x
y[1] = x - k*x*delta_t*delta_t/(2*m)

# k*x + m*a - c*v = 0
# k*y[n-1] + m*((y[n-2]-y[n-1]) - (y[n-1]-y[n]))/(delta_t**2) - c*(y[n-2]-y[n])/2*delta_t = 0
for i in range(2, interval):
    y[i] = (-y[i-1]*k*delta_t*delta_t + c*delta_t*y[i-2]/2+m*(2*y[i-1]-y[i-2]))/(m+c*delta_t/2)

plt.plot(t, y, 'k-', linewidth=1.25)


# save figure
# plt.savefig("/Users/wanjiang/Documents/TCD/cs7gv2_mathmatics_of_sound_and_light/assignment_2/q1_damped_spring.png", dpi=1200, bbox_inches='tight')

plt.show()