import numpy as np
import matplotlib.pyplot as plt

def signal_plot(x, y, index , str):
    plt.subplot(4,1,index)
    plt.plot(x,y)
    plt.title(str)
    # plt.axhline(color = 'r')
    # plt.axvline(color = 'r')
    plt.xlabel('time')
    plt.ylabel('value')
    plt.grid(True)
def signal_plot_stem(x, y, index , str):
    plt.subplot(4,1,index)
    plt.stem(x,y)
    plt.title(str)
    # plt.axhline(color = 'r')
    # plt.axvline(color = 'r')
    plt.xlabel('time')
    plt.ylabel('value')
    plt.grid(True)

f = 500
t = np.linspace(0 , 0.02 , 1000)
x = 5 * np.sin(2 * np.pi * f * t + np.pi/2)
signal_plot(t , x , 1 , 'original signal')
# nyquest rate 
fs = 1000
t_sampled = np.arange(0 , 0.02 , 1/fs)
x_sampled = 5 * np.sin(2 * np.pi * f * t_sampled + np.pi/2)
signal_plot_stem(t_sampled , x_sampled , 2 , 'nyquest rate')

# oversampled 
fs = 8000
t_sampled = np.arange(0 , 0.02 , 1/fs)
x_sampled = 5 * np.sin(2 * np.pi * f * t_sampled + np.pi/2)
signal_plot_stem(t_sampled , x_sampled , 3 , 'nyquest rate')

# UnderSampled
fs = 400
t_sampled = np.arange(0 , 0.02 , 1/fs)
x_sampled = 5 * np.sin(2 * np.pi * f * t_sampled + np.pi/2)
signal_plot_stem(t_sampled , x_sampled , 4 , 'nyquest rate')

plt.show()