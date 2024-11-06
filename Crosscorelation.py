import numpy as np
import matplotlib.pyplot as plt

x = [1,3,5,7]
h = [4,3,2,1]

y = []
size = len(x) + len(h) -1 ;
def crosscorelation():
    for l in range(-1*len(h)+1 , len(x)):
        value = 0
        for k in range(0 , len(x)):
            if k-l >= 0 and k-l < len(h) :
                value += x[k] * h[k-l] 
        print(value )
        y.append(value)
crosscorelation()
t = range(-1*len(h)+1 , len(x))
print(y,t)
plt.plot(t,y)
plt.stem(t,y)
plt.title('crosscorelation')
plt.axhline(color = 'r')
plt.axvline(color = 'r')
plt.xlabel('time')
plt.ylabel('value')
plt.grid(True) 
plt.show()