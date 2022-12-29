import numpy as np
data_from_text=np.genfromtxt('numpy_advance.txt',delimiter=',')
print(data_from_text)
data_from_text=data_from_text.astype('int32')
print(data_from_text)
print(data_from_text>10)
#advanceindexing
print(data_from_text[data_from_text>0])
print(data_from_text[data_from_text<0])
#fillvalues
fill_values=np.genfromtxt('numpy_advance.txt',delimiter=',',dtype=np.int32)
print(fill_values)
fill_values=np.genfromtxt('numpy_advance.txt',delimiter=',',dtype=np.int32,filling_values=100)
print(fill_values)

import numpy as np
def numpy_function(x,y):
    return 10 * x + y
b=np.fromfunction(numpy_function,(2,3),dtype=int)
print(b)
