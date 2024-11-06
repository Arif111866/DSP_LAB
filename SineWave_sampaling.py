import numpy as np
import matplotlib.pyplot as plt

def signal_plot(x, y, index , str):
    plt.subplot(2,2,index)
    plt.plot(x,y)
    plt.title(str)
    plt.axhline(color = 'r')
    plt.axvline(color = 'r')
    plt.xlabel('time')
    plt.ylabel('value')
    plt.grid(True)
def signal_plot_stem(x, y, index , str):
    plt.subplot(2,2,index)
    # plt.plot(x,y)
    plt.stem(x,y)
    plt.title(str)
    plt.axhline(color = 'r')
    plt.axvline(color = 'r')
    plt.xlabel('time')
    plt.ylabel('value')
    plt.grid(True)

# original signal 
st = 0
stp = 0.01
sine_amplitutde = 2 
sine_phase = 0
sin_f = 500
sample_count = 200 ;
x = np.linspace(st , stp , sample_count) ;
y_sine = sine_amplitutde * np.sin(2 * np.pi * x * sin_f + (sine_phase *(np.pi/180)))
signal_plot(x , y_sine , 1 , 'sin wave')

# Nyquest sampaling
fs = 2*sin_f
x = np.arange(st , stp , 1/fs)
y_sine = sine_amplitutde* np.sin(2 * np.pi * x * sin_f + (sine_phase *(np.pi/180)))
signal_plot_stem(x , y_sine , 2 , 'Nyquest rate')

# Up sampalint
fs = 6*sin_f
x = np.linspace(st , stp , int(fs*(stp - st)))
y_sine = sine_amplitutde* np.sin(2 * np.pi * x * sin_f + (sine_phase *(np.pi/180)))
signal_plot_stem(x , y_sine , 3 , 'Up sampaling')

# Down sampling
fs = sin_f
x = np.linspace(st , stp , int(fs*(stp - st)))
y_sine = sine_amplitutde* np.sin(2 * np.pi * x * sin_f + (sine_phase *(np.pi/180)))
signal_plot_stem(x , y_sine , 4 , 'Down sampaling')

plt.show()