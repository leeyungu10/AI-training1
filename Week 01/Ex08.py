# matplotlib는 그래프 그려주는 친구랍니다.
import matplotlib.pyplot as mp
import numpy as np

x = []
y = []
y1 = []
for i in range(-100, 100):
    x.append(i)
    y.append(i*i*-3+2*i-5)
    y1.append(i+1)

arr_x = np.array(x)
arr_y = np.array(y)
arr_y1 = np.array(y1)
mp.plot(arr_x, arr_y)
mp.plot(arr_x, arr_y1)
mp.show()
