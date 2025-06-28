import numpy as np
import statistics as stats

# baked_food = [200,150,150,130,200,220,170,188]
# a = np.array([baked_food])
# print(np.mean(a)) #sum of all values
# print(np.median(a)) #Central value after sorting
# print(stats.mode(baked_food))
# print(np.std(baked_food))
# print(np.var(baked_food))

#-1 represent inversely proportional relationship
# 1 represent inversely relationship
# 0 represent no relationship
tobacco_consumption = [30,50,10,30,50,40]
deaths = [100,120,70,100,120,112]
print(np.corrcoef([tobacco_consumption,deaths]))

price = [300,100,350,150,200]
sale = [10,20,7,17,3]
print(np.corrcoef([price,sale]))
