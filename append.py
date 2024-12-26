# its a method used to add a element at the end of an existing array 
# syntax array_name.append(newelement)
from array import *
sturoll=array('i',[101,32,23,34])
n = len(sturoll)
i = 0
while i<n:
    print(sturoll[i])
    i+=1
    
print("array after i append is ")
sturoll.append(234)
a=0
n = len(sturoll)

while a<n:
    print(sturoll[a])
    a+=1
