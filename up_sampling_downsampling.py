import numpy as np
import matplotlib.pyplot as plt

def signal_plot(x, y, index , str):
    plt.subplot(3,2,index)
    plt.plot(x,y)
    plt.title(str)
    # plt.axhline(color = 'r')
    # plt.axvline(color = 'r')
    plt.xlabel('time')
    plt.ylabel('value')
    plt.grid(True)
def signal_plot_stem(y, index , str):
    plt.subplot(3,2,index)
    plt.stem(y)
    plt.title(str)
    # plt.axhline(color = 'r')
    # plt.axvline(color = 'r')
    plt.xlabel('time')
    plt.ylabel('value')
    plt.grid(True)

t = np.arange(0 , 0.008, 0.00001)
x = 5 * np.sin(2 * np.pi * 500 * t + np.radians(90))
signal_plot(t,x , 1 , 'original signal')

# upsampling rate by 2 
fs = 3750
T = 1/fs 
t_sample = np.arange(0 , 0.008 , T) 
x_sanpled = 5 * np.sin(2 * np.pi * 500 * t_sample + np.radians(90))
signal_plot_stem( x_sanpled , 2 , "sampled signal")

x_sample_2 = np.zeros(len(t_sample)*2)
x_sample_2[::2] = x_sanpled 
signal_plot_stem(x_sample_2 , 3 , 'upsacling factor 2')

# Smooting of upsacling 
for i in range(1 , len(x_sample_2)):
    if i%2 == 1:
        if i == len(x_sample_2)-1:
            x_sample_2[i] = (x_sample_2[i-1] + x_sample_2[i])/2
        else:
            x_sample_2[i] = (x_sample_2[i+1] + x_sample_2[i-1])/2

signal_plot_stem(x_sample_2 , 4 , 'smooting signal')


# downsampling rate by 2 
x_Down_sample = x_sanpled[::2]
signal_plot_stem(x_Down_sample , 5 , 'down sampled')
plt.show()