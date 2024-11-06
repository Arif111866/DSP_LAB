import numpy as np
import matplotlib.pyplot as plt

def signla_plot_stem(x, y , index , str):
    plt.subplot(2,2, index)
    plt.stem(x, y)
    plt.title(str)
    plt.xlabel('time')
    plt.ylabel('value')
    plt.axhline(color = 'r')
    plt.axvline(color = 'r')
    plt.grid()

def convolution (x, h):
    y = np.zeros(len(x) + len(h) -1)
    for n in range(0 , len(y)):
        y[n] = 0 
        for k in range(0 , len(x)):
            if n-k >= 0 and n-k < len(h):
                y[n] += (x[k] * h[n-k]) ;
    return y

x = [1,2,3,4,5]
h = [2,3,4]
t_x = np.zeros(len(x))
t_h = np.zeros(len(h))
for i in range(0, len(t_x)):
    t_x[i] = i
for i in range(0, len(h)):
    t_h[i] = i

# plot x 
signla_plot_stem(t_x , x , 1 , 'x[n]')
# plot h 
signla_plot_stem(t_h , h , 2 , 'h[n]')
# plot convolution 
y = convolution(x , h) 
t_y = np.zeros(len(y)) 
for i in range(0 , len(y)):
    t_y[i] = i 
signla_plot_stem(t_y , y, 3 , 'x[x]*h[n-k]')


plt.show() ;
