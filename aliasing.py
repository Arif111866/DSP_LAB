import numpy as np
import matplotlib.pyplot as plt

def signal_plot(x, y, index , str):
    plt.subplot(4,1,index)
    plt.plot(x,y)
    plt.title(str)
    # plt.axhline(color = 'r')
    # plt.axvline(color = 'r')
    # plt.xlabel('time')
    # plt.ylabel('value')
    plt.grid(True)
def signal_plot_stem(x, y, index , str):
    plt.subplot(4,1,index)
    plt.stem(x,y)
    plt.title(str)
    # plt.axhline(color = 'r')
    # plt.axvline(color = 'r')
    # plt.xlabel('time')
    # plt.ylabel('value')
    plt.grid(True)

t = np.linspace(0 , 1 , 1000)
x1 = np.sin(2 * np.pi * 10 * t)
x2 = np.sin(2 * np.pi * 50 * t)

signal_plot(t , x1 , 1 , 'signal x1')
signal_plot(t , x2 , 2 , 'signal x2')


fs = 40
t_sampled = np.arange(0 , 1 , 1/fs)
x1_sampled = np.sin(2 * np.pi * 10 * t_sampled)
x2_sampled = np.sin(2 * np.pi * 50 * t_sampled)

signal_plot_stem(t_sampled , x1_sampled , 3 , 'sampled signal x1')
signal_plot_stem(t_sampled , x2_sampled , 4 , 'sampled signal x2')

plt.show()
