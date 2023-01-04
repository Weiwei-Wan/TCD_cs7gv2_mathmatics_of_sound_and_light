from mpl_toolkits.mplot3d import Axes3D 
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation


def move_arrow(pos, dir, trunk_plt, head_plt, length=1, arrow_length_ratio=0.3, normalize=False, arrow_angle=15):
    pos = np.asarray(pos)
    dir = np.asarray(dir)
    dir_norm = dir / np.linalg.norm(dir)
    if normalize:
        dir = dir_norm
    shift = dir * length
    end = pos + shift
    # Make rotation matrix for arrow direction
    head_x = -dir_norm
    head_y = np.cross(head_x, np.arange(3) == head_x.argmin())
    head_z = np.cross(head_x, head_y)
    rot_ref = np.stack([head_x, head_y, head_z], axis=1)
    # Make rotation matrix for head tips
    arrow_rad = np.deg2rad(arrow_angle)
    s, c = np.sin(arrow_rad), np.cos(arrow_rad)
    rot_arrow = np.array([[c, 0, s], [0, 1, 0], [-s, 0, c]])
    # Compute head tips
    head_length = np.linalg.norm(shift) * arrow_length_ratio
    head_1 = end + rot_ref @ rot_arrow @ [head_length, 0, 0]
    head_2 = end + rot_ref @ rot_arrow.T @ [head_length, 0, 0]
    # Set line data
    trunk_plt.set_data([pos[0], end[0]], [pos[1], end[1]])
    trunk_plt.set_3d_properties([pos[2], end[2]])
    head_plt.set_data([head_1[0], end[0], head_2[0]], [head_1[1], end[1], head_2[1]])
    head_plt.set_3d_properties([head_1[2], end[2], head_2[2]])

fig = plt.figure()
ax = plt.subplot(111, projection='3d')  
pos = [.2, .4, .1]
dir = [.5, .0, .3]
trunk_plt = ax.plot3D([], [], [], c='b')[0]
head_plt = ax.plot3D([], [], [], c='b')[0]
move_arrow(pos, dir, trunk_plt, head_plt)
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_zlim(0, 1)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

def anim_frame(i):
    dir_shift = 0.1 * np.array([np.sin(0.01 * i + 1), np.sin(0.02 * i + 2), np.sin(0.03 * i + 3)])
    move_arrow(pos, dir + dir_shift, trunk_plt, head_plt)
    return [trunk_plt, head_plt]

anim = FuncAnimation(fig, anim_frame, range(1000), interval=1/30, repeat=False, blit=True)