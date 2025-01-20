# # used for multidimension array as multi dimension array is not pssible without numpy
# two ways importing numpy 
# 1>import numpy - imports entire module 
# 2>from numpy import*- only class obj var etc /
# one dimenioal array  means single row and sinle column
# ways creating 1d array - array, linspace , logspace , arange , zeros, ones all these r funciton to create 1d array 
# by arry fun
import numpy 
one_darray= numpy.array([231,43,132,543,213,456],dtype=int)
for i in range(6):
    print(one_darray[i])
    