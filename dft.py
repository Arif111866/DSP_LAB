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
def signal_plot_stem(x, y, index , str):
    plt.subplot(3,2,index)
    plt.stem(x,y)
    plt.title(str)
    # plt.axhline(color = 'r')
    # plt.axvline(color = 'r')
    plt.xlabel('time')
    plt.ylabel('value')
    plt.grid(True)
def DFT(x):
    X = np.zeros(len(x),dtype=complex)
    for m in range(0 , len(x)):
        X[m] = 0 
        for n in range(0 , len(x)):
            X[m] += x[n]* np.exp(-1j*2*np.pi*n*m/len(x))
    return X ;
def calculate_phase(real, imag):
    # Initialize an empty list to store phase values
    phase = []
    
    # Calculate phase for each element
    for r, i in zip(real, imag):
        if r > 0:
            angle = np.arctan(i / r)
        elif r < 0 and i >= 0:
            angle = np.arctan(i / r) + np.pi
        elif r < 0 and i < 0:
            angle = np.arctan(i / r) - np.pi
        elif r == 0 and i > 0:
            angle = np.pi / 2
        elif r == 0 and i < 0:
            angle = -np.pi / 2
        else:
            angle = 0  # r == 0 and i == 0, undefined phase
        
        phase.append(angle)
    
    return np.array(phase)


N = 8
fs = 8000
n = np.arange(N)
T = 1/fs
x = np.sin(2*np.pi*1000*n*T) + 0.5*np.sin(2*np.pi*2000*n*T + (3*np.pi/4))
# print(x) ;
y = DFT(x)
# print(y)
signal_plot(n , x , 1 , 'original signal')
mag = np.abs(y)
signal_plot_stem(n , mag , 2 , 'magnitutde')
real = np.real(y)
signal_plot_stem(n , real , 4 , 'real')
img = np.imag(y)
signal_plot_stem(n , img , 5, "img")

phase = np.angle(y)*(180/np.pi)

signal_plot_stem(n , phase , 3 , 'phase')
plt.show()