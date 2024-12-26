# help to reverse the order lements presnet int he arrayb 
from array import * 
stu_rl=array('i', [123,124,324,431,213])
n = len(stu_rl)
i  = 0 
while i < n :
    print(stu_rl[i])
    i +=1
    
print("array afterrmeoving  : ")
stu_rl.reverse()
n = len(stu_rl)
i = 0 
while i < n : 
    print(stu_rl[i])
    i += 1 