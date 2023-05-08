import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


data= pd.read_csv(r'C:\Users\X_xx\Desktop\广州站1#数据（振动+工艺参数）.csv')

#print(data.dtypes)
# print(data_set)
# print(data.loc[:, ['datetime', 'A72']])


# data = data.loc[:, ['datetime', 'A71', 'A72']]  # 读取主电机驱动端振动数据
(x, _) = data.shape
#print(x)



plt.figure(num='主电机驱动端振动数据-----1')
plt.subplot(2, 1, 1)

h = plt.scatter(np.arange(x),
            data.loc[:, 'A72'],s=1)


plt.legend(handles=(h, ), labels=['A72', ], loc='best')

plt.ylim(0, 0.5)
plt.xlabel(r'time')
plt.ylabel(r'vibration_data')
plt.title(r'disperse')

plt.subplot(2, 1, 2)
h = plt.plot(np.arange(x), data.loc[:, 'A72'])

plt.legend(handles=(h, ), labels=['A72', ], loc='best')

plt.xlabel(r'time')
plt.ylabel(r'vibration_data')
plt.title(r'continuous')


plt.figure(num='主电机驱动端振动数据-----2')
plt.subplot(2, 1, 1)

h = plt.scatter(np.arange(x),
            data.loc[:, 'A73'], s=1)


plt.legend(handles=(h,), labels=['A73', ], loc='best')

plt.ylim(0, 80)
plt.xlabel(r'time')
plt.ylabel(r'vibration_data')
plt.title(r'disperse')

plt.subplot(2, 1, 2)
h = plt.plot(np.arange(x), data.loc[:, 'A72'])

plt.legend(handles=(h, ), labels=['A73', ], loc='best')
#plt.ylim(0, 60)
plt.xlabel(r'time')
plt.ylabel(r'vibration_data')
plt.title(r'continuous')


plt.figure(num='主电机非驱动端振动数据-----1')
plt.subplot(2, 1, 1)

h = plt.scatter(np.arange(x),
            data.loc[:, 'A70'], s=1)


plt.legend(handles=(h,), labels=['A70', ], loc='best')

#plt.ylim(0, 80)
plt.xlabel(r'time')
plt.ylabel(r'vibration_data')
plt.title(r'disperse')

plt.subplot(2, 1, 2)
h = plt.plot(np.arange(x), data.loc[:, 'A70'])

plt.legend(handles=(h, ), labels=['A70', ], loc='best')
#plt.ylim(0, 60)
plt.xlabel(r'time')
plt.ylabel(r'vibration_data')
plt.title(r'continuous')


plt.figure(num='主电机非驱动端振动数据-----2')
plt.subplot(2, 1, 1)

h = plt.scatter(np.arange(x),
            data.loc[:, 'A71'], s=1)


plt.legend(handles=(h,), labels=['A71', ], loc='best')

#plt.ylim(0, 80)
plt.xlabel(r'time')
plt.ylabel(r'vibration_data')
plt.title(r'disperse')

plt.subplot(2, 1, 2)
h = plt.plot(np.arange(x), data.loc[:, 'A71'])

plt.legend(handles=(h, ), labels=['A71', ], loc='best')
#plt.ylim(0, 60)
plt.xlabel(r'time')
plt.ylabel(r'vibration_data')
plt.title(r'continuous')
plt.show()

