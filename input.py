# # # taking in0put from useres
# # from array import *
# # sturoll= array ('i',[])
# # n = int(input ("enter number of elements :"))
# # for i in range (n):
# #     sturoll.append(int(input("enter element in loop :")))
# # for i in range (len(sturoll)):
# #     print(sturoll[i])
# by while loop 
from array import *
sturoll = array('i',[])
i=0
n=int(input("enter the aaray elemnts:"))
while i<n:
    sturoll.append(int(input("enter the loop elemntes arry : ")))
    i+=1
a=0
while a<n:
    print(sturoll[a])
    a+=1