# remove help to remove the first occurence of the array 
from array import * 
stu_rl=array('i', [123,124,324,431,213])
n = len(stu_rl)
i  = 0 
while i < n :
    print(stu_rl[i])
    i +=1
    
print("array afterrmeoving  : ")
stu_rl.remove(124)
n = len(stu_rl)
i = 0 
while i < n : 
    print(stu_rl[i])
    i += 1 