import numpy as np
#
# l1 = [[20,30,40],[60,70]]
# # l2 = 5
# # print(l1*l2)
# print(l1)

# a = np.array([20,30,40.0])
# print(a)

a = np.array([[20,30,40],[50,60,70],[80,90,10]])
print(a[2,0:3])
print("The size of the array is:",np.size(a))
print("The shape of the array is:",np.shape(a))
print("The number of dimensions is",np.ndim(a))
print(a.astype(str))










# print()
# b = np.array([50,60,70])
# # [50,60,70],[80,90,10]
# print(a)
# print(b)
# # print(a*b)
#
# print(type(a))