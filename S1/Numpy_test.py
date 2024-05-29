import numpy as np
import random as rd
##################################################
# A = np.array([[2,7],[5,6], [4,3]])
# print(A)
# print(A.mean(axis=1))
# exit(-2)
# ##################################################
# x = np.arange(10)
# print(x[::2])
# exit(-2)
#
# ##################################################
# mat_1 = np.loadtxt("mat_1.txt")
# print(type(mat_1))
# print((mat_1[0,:]))
# exit(-2)
# ##################################################
a = np.reshape(range(1, 10), (3, 3))
np.savetxt("out.dat", a)

##################################################
Values = [1,2,3,4,5]
#K = np.full((10,10), rd.choices(Values, k=10), int)
K = np.random.randint(10,90,(10,10))
print(np.linalg.eig(K))
#K = np.random.randn(10,10)

print(K)