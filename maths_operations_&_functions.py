import numpy as np

arr1= np.array([[10,20,22],[30,50,98]])
arr2= np.array([[55,55,66],[58,55,88]])
print(arr1+arr2)
print(np.add(arr1,arr2))
print(arr1-arr2)
print(np.subtract(arr1,arr2))

a=np.array([1,2,3,4,5])
b=np.array([3])
c=np.array([1,4,9,16,25])
print(np.power(a,b))
print(np.sqrt(c))