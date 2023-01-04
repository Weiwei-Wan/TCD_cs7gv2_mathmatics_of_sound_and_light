# https://blog.csdn.net/jk_101/article/details/124804014
import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.fftpack import fft2

img = np.zeros((200,200))

# if (i-100)**2 + (j-100)**2 <= 50:
# if i>95 and i<105 and j>95 and j<i:
# if i>95 and i<105 and j>(i+95)/2 and j<(305-i)/2:
for i in range(len(img)):
    for j in range(len(img[0])):
        if (i-100)**2 + (j-100)**2 <= 50:
            img[i][j]=255

for i in range(len(img)):
    for j in range(len(img[0])):
        img[i][j] = img[i][j]*math.pow(-1,i+j)

img = fft2(img)
plt.imshow(np.abs(img), cmap='gray')
plt.show()