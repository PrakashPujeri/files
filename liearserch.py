import time
import numpy as np 
import matplotlib.pyplot as plt 
def linearsearach(arr,x):
    i=0
    while i<len(arr):
        if arr[i]==x:
            return i
        i=i+1
    return-1
times=list()
arr=list()
numtimes=list()
for i in range(1,8):
    start=time.time()
    n=int(input("enter the no of elements:"))
    numtimes.append(n)
    for x in range(n):
        number=np.random.randint(10,99)
        arr.append(number)
    print("list before searching",x+1,"elements")
    print(arr)
    linearsearach(arr,x)
    end=time.time()
    times.append(end-start)
    print("list after linearsearching for",n,"elements is",end-start)
print(numtimes)
print(times)
plt.plot(numtimes,time,label="linearsearach")
plt.grid()
plt.legend()
plt.show()

    