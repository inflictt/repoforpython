from datetime import date

def storing_tasks(task_list,task_info):
    task_list.append(task_info)
    
def feed_tasks(task_list): 
        task_info=input(f"{i}). Enter the details of the task {i}: ")
        storing_tasks(task_list,task_info)
        
def checking_tasks_as_integer_input():
    while True:
            tasks=(input(f"{user_name} Enter Number Of Tasks You Want To Add for {date.today()} = "))
            try:
                tasks=int(tasks)
                return tasks
            except:
                print(f"You entered {tasks} incorretly retry again . ")
    
user_name=input("Enter Your Name : ")
task_list=[]
tasks=checking_tasks_as_integer_input()
for i in range(1,tasks+1):
    feed_tasks(task_list)
print("Final List Of Tasks Is : ",task_list)