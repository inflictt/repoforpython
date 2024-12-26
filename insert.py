# # insert helps to insert elemneta at a particular position an array 
# synax: arraayname.insert(position , element ) \
from array import *
sturoll = array ('i',[132,412,422,123,354])
n = len(sturoll)
i = 0 
while i<n:
    print(sturoll[i])
    i+=1
print ("after inserting the array ")
sturoll.insert(2,0)
n = len(sturoll)
i = 0 
while i < n:
    print(sturoll[i])
    i += 1