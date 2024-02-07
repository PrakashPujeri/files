import time
import random
def linearsearch(arr,x):
    i=0
    while i<len(arr):
        if(arr[i]==x):
            return i
        i=i+1
    return-1
arr=list()
start=time.time()
n=int(input("eneter the number of you want:"))
while n > 0:
    z=int(input("enter the num:"))
    arr.append(z)
    n = n- 1
print(arr)
x=int(input("enter the number to be searched:"))
print(linearsearch(arr,x))
r= linearsearch(arr,x)
print("the element found of",r)
