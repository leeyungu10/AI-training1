# 행렬
# 행렬이란? 다차원 배열

import numpy as np

arr1 = [[10, 20], [15, 25]]
arr2 = [[1,2], [2,3]]
print(arr1)
print(arr2)

arr11 = np.array(arr1)
arr22 = np.array(arr2)

print(arr11 + arr22)
print(arr11 * arr22)
print(np.dot(arr11, arr22))


