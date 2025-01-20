from datetime import date
def task_printing(task_list):
    print(task_list)
    
def storing_tasks(task_list,task_info):
    task_list=task_info
    task_printing(task_list)
def feed_tasks(tasks,task_list): 
    for i in range(tasks):
        task_info=input("enter the details of the task : ")
        storing_tasks(task_list,task_info)
    
user_name=input("Enter Your Name : ")
tasks=int(input(f"{user_name} Enter Number Of Tasks You Want To Add for {date.today()} "))
task_list=[]

feed_tasks(tasks,task_list)
# print(task_list)