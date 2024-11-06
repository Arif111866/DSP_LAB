import numpy as np
import matplotlib.pyplot as plt

def plot_funtion(x, y, amplitutde , phase , index):
    plt.subplot(3,2,index)
    plt.plot(x, y)
    plt.title("Sine Wave Amplitutde ={0} & phase = {1}".format(amplitutde , phase))
    plt.xlabel("angle")
    plt.ylabel('value')
    plt.axhline(color ='r')
    plt.axvline(color = 'r')
    plt.grid()

def signal(x, y , str , index):
    plt.subplot(3,2,index)
    plt.stem(x, y)
    plt.title(str)
    plt.xlabel('time')
    plt.ylabel('value')
    plt.axhline(color ='r')
    plt.axvline(color = 'r')
    plt.grid()

def unit_step(x):
    y = np.zeros(len(x))
    for i in range (0 , len(x)) :
        if x[i] >= 0:
            y[i] = 1
        else:
            y[i] = 0
    return y 

def ramp(x):
    y = np.zeros(len(x))
    for i in range(0, len(x)):
        if x[i] >= 0:
            y[i] = i
        else:
            y[i] = 0
    return y 
#  sine wave
sine_amplitutde = 2 
sine_phase = 0
sin_f = 5
x = np.linspace(-100 , 100 , 200) ;
y_sine = sine_amplitutde * np.sin(2 * np.pi * x * sin_f + (sine_phase *(np.pi/180)))
plot_funtion(x , y_sine , sine_amplitutde , sine_phase , 1)

# cosine wave
cos_amplitutde = 2 
cos_f = 5
cos_phase = 0 * (np.pi/180)
y_cos = cos_amplitutde * np.cos(2 * np.pi * x * cos_f + cos_phase)
plot_funtion(x , y_cos , cos_amplitutde , cos_phase , 2)

# Unite step
x_unit = np.linspace(-10 , 10 , 20)
y_unit = unit_step(x_unit) ;
str = 'Unit step signal'
signal(x_unit, y_unit , str , 3)

# Ramp 
y_ramp = ramp(x_unit)
str = 'Ramp signal'
signal(x_unit , y_ramp , str , 4)

# exponential signal 
y_expo = np.exp(x_unit) ;
str = "exponential signal"
signal(x_unit , y_expo , str , 5)

plt.show()