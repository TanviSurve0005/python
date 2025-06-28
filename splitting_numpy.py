import numpy as np

# a=[20,40,50]
# b=[2,3,4]
# print(a+b)

# a=np.array([1,2,3,4,5])
# b=np.array([1,4,9,16,25])
# print(np.concatenate([a,b]))

# a=np.array([[1,2,3],[4,5,5]])
# b=np.array([[1,4,9],[16,2,5]])
# print(np.concatenate([a,b],axis=0))
# print(np.hstack([a,b])) #horizontal Concatenation
# print(np.vstack([a,b]))#Vertical Concatenation

arr = np.array([[20,40,40],[50,57,20],[50,22,66]])
# arr1 = np.array_split(arr,2)
# print(arr1)
# print(np.append(arr,90))
# print(np.append(arr,[90,100]))
# print(np.insert(arr,1,10))
# print(type(arr))
# print(np.insert(arr,[1],[10,80],axis=1)) #array,index,value

print(arr)
print(np.delete(arr,1))#only 1st element remove
print(np.delete(arr,1, axis=0))#1 row complete remove