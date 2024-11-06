import numpy as np
import matplotlib.pyplot as plt

def signal_plot(x, y, index , str):
    plt.subplot(2,1,index)
    plt.plot(x,y)
    plt.title(str)
    plt.axhline(color = 'r')
    plt.axvline(color = 'r')
    plt.xlabel('time')
    plt.ylabel('value')
    plt.grid(True)

n = 8000
w = np.linspace(-1*np.pi , np.pi , n)
H = np.zeros(n,dtype=complex)
for i in range(0 , n):
    z = np.exp(1j*w[i])
    H[i] = (0.1*(z ** 0) +  0.2*(z ** -1) + 0.3*(z ** -2))*1j/(1*(z ** 0) - 0.5*(z ** -1) + 0.25*(z ** -2))

magnitude = np.abs(H)
phase = np.angle(H)*(180/np.pi)
signal_plot(w , magnitude , 1 , 'Mangnitutde')
signal_plot(w , phase , 2 , 'phase')
plt.show()