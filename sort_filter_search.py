import numpy as np

# a = np.array([[7,3,5,6,2],[8,4,5,3,5]])
# print(np.sort(a))

# a = np.array([3,4,1,7,8])
# ss= np.searchsorted(a, 4)# s = np.where(a%2==0)
# print(ss)

# a = np.array([20, 35, 40, 50])
# fa = a>=35
# f1 = a%2==0
# new = a[f1]
# print(new)


# Aggregation Functions


# a = np.array([20, 35, 40, 50])
# print(np.sum(a))
# print(np.min(a))
# print(np.max(a))
# print(np.size(a))
# print(np.mean(a))
# print(np.cumsum(a))
# print(np.cumprod(a))

a = [100,150,199,200,250,130]
b=[10,50,30,40,30,10]

price = np.array(a)
quantity = np.array(b)

print(price,"\n",quantity)
c = (np.cumprod([price,quantity], axis=0))
print(c[1].sum())
