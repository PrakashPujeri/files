import time
def linearsearch(arr,z):
    i=0
    while i<len(arr):
        if(arr[i]==z):
            return i
        i=i+1
    return-1

arr=[]
start=time.time()
arr= [20,20,55,99,45,14,55,4]
print(arr)
z=55
print(linearsearch(arr,z))
print(start)