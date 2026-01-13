import numpy as np
arr=np.array([[10,20,30],[40,50,60]])
mean=np.mean(arr)
median=np.median(arr)
std_dev=np.std(arr)
variance=np.var(arr)
transpose=np.transpose(arr)
copied_matrix=np.copy(arr)
copied_matrix[0]=100
print("original matrix=",arr)
print("mean=",mean)
print("median=",median)
print("standard deviation=",std_dev)
print("variance=",variance)
