# one d array consits of single row but multi columns 
# type: ignore # you have to import array module if u want to use array 
# 2 way to impor 1) import array 2) from array import*
# import array 
# stu_roll= array.array('i',[101,102,103,104,105])
# print(stu_roll[0])
# print(stu_roll[1])
# print(stu_roll[2])
# print(stu_roll[3])
# print(stu_roll[4])
from array import array
stu_roll= array('i',[101,102,99 ,104,105])
# print(stu_roll[0])
# print(stu_roll[1])
# print(stu_roll[2])
# print(stu_roll[3])
# print(stu_roll[4])
for element in stu_roll:
    print(element)
