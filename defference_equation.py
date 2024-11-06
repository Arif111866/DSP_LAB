import numpy as np
import matplotlib.pyplot as plt

def convolution(x,h):
    size = len(x)+len(h)-1
    Y = np.zeros(size)
    for n in range(0 , size):
        Y[n] = 0
        for k in range(0 , len(x)):
            if n-k >= 0 and n-k < len(h):
                Y[n] += x[k]*h[n-k]
    return Y

# y(n) = 0.3x(n) + 0.4x(n-1) + 0.3x(n-2)
x = np.array([1, 2, 3, 4, 5])
h = np.array([0.3, 0.4, 0.3])
y = convolution(x,h)
print('y[n] =' , y)

