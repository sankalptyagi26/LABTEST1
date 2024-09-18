import numpy as np
import matplotlib.pyplot as plt

def calavgtemp(temp):
    m = len(temp)
    n = len(temp[0])
    res = []
    for j in range(0 , n):
        s = 0
        for i in range(0 , m):
            s = s + temp[i,j]
        
        res.append(float(s/m))
    return res

temp = np.array([[30, 32, 31, 29, 28, 27, 26] , [35, 34, 36, 33, 32, 31, 30] , [25, 26, 27, 28, 29, 30, 31] , [22, 23, 24, 25, 26, 27, 28]])
for i in range(0,4):
    print("Average temperature of city " , i , " : " , temp[i].mean())
    print("Maximum Temperature of city " , i , " : " , temp[i].max())
    print("Minimum Temperature of city " , i , " : " , temp[i].min())
    print()
print("Average temperature of each day : " , calavgtemp(temp))
print()
maxm = temp.max()
minm = temp.min()
x = np.linspace(1 , 7 , 7)

plt.plot(x , temp[0] , label = "A")
plt.plot(x , temp[1] , label = "B")
plt.plot(x , temp[2] , label = "C")
plt.plot(x , temp[3] , label = "D")
    
plt.title("Line plot for temperatures of various cities")
plt.xlabel("Day")
plt.ylabel("Temperature")
plt.legend()
plt.show()

temprange = []
for i in range(0 , 4):
    temprange.append(temp[i].max() - temp[i].min())
print()
for i in range(0 , 4):
    print("Temperature range of city " , i , " : " , temprange[i])
    
cities = ["A" , "B" , "C" , "D"]
plt.bar(cities , temprange)
plt.xlabel("Cities")
plt.ylabel("Temperature range")
plt.title("Bar graph showing temperature ranges : ")
plt.show()
