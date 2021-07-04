import numpy as np

arr=np.array(10)
print(arr)
print('dimention',arr.ndim)
arr1=np.array([1,2,3,4,5])
print(arr1)
print('dimention',arr1.ndim)

arr2=np.array([[1,2,3,4],[4,3,2,1]])
print(arr2)
print('dimention',arr2.ndim)
arr3=np.array([[[1,2],[3,4],[5,6]]])
print(arr3)
print('dimention',arr3.ndim)

print(arr2[0,3])
print(arr2[1,2])