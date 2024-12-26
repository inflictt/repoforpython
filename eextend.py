# to aaddd aone more iterable object to one present one 
from array import array 

stu_rl=array('i', [123,124,324,431,213])
arrray=array('i', [231,34,452,45,465])

n = len(stu_rl)
i  = 0 
while i < n :
    print(stu_rl[i])
    i +=1
    
print("array after extending   : ")
stu_rl.extend(arrray)
n = len(stu_rl)
i = 0 
while i < n : 
    print(stu_rl[i])
    i += 1 