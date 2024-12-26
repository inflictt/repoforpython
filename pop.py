# use to remove ht elast elemnet from the array 
# synx : arrayname.pop()
from array import * 
stu_rl=array('i', [123,124,324,431,213])
n = len(stu_rl)
i  = 0 
while i < n :
    print(stu_rl[i])
    i +=1
    
print("array after getitng popped : ")
stu_rl.pop(3)
n = len(stu_rl)
i = 0 
while i < n : 
    print(stu_rl[i])
    i += 1 