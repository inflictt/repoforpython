from datetime import date
from sympy import oo

def creating_a_list(num_tasks,tasks_list):
    for i in range(1, num_tasks + 1):
        task_details = input(f"Enter the details for Task {i}: ")
        tasks_list.append(task_details)

                
def number_of_tasks():
    while True:
        num_tasks=input("Enter the number of tasks you want to deal with : ")
        try:
            num_tasks=int(num_tasks)
            if num_tasks>0:
                return num_tasks
            else:
                print("Wrong range inputed for number of tasks . ")
        except:
            print("Please enter a correct input . ")
        
        
def checking_results_for_choice(choice,tasks_list,user_name,completed_tasks_list):
        if choice==1: #means users want to create a list 
            print(f"Creating A list For {user_name}")
            num_tasks=number_of_tasks()
            creating_a_list(num_tasks,tasks_list)
        
        elif choice == 2 :#updation or edition depening on usereneed
            print("relpacing the list please hold up a bit ...")
            to_edit=int(input("Enter the index of value you want to replace with : "))
            tasks_list[to_edit]=input("Enter the new value you want to update to : ")
            print("List after getting replaced is : ", tasks_list)
        
        elif choice == 3: #delteing by value from the user need 
            print("deletion in progress please hold up a bit ...")
            print("list before deleteing a value", tasks_list)
            to_delete=input("enter the value you want to delete from the list : ")
            tasks_list.remove(to_delete)
            print("list after deleting a value ",tasks_list)
        
        elif choice==4 : #to view the list 
            print("Viewving list here = ", tasks_list)
        
        elif choice == 5: #for completed task list
            comp_task=int(input("enter the index of the task you want to update as completed : "))
            x=tasks_list.pop(comp_task)
            completed_tasks_list.append(x)          
            print("Completed task list is ", completed_tasks_list)     
            
            
            
def checking_user_input_for_integer():
    while True:
        choice = input(
            "Enter 1 to create a list\n"
            "Enter 2 to replace the list\n"
            "Enter 3 to delete tasks\n"
            "Enter 4 to view the list\n"
            "Enter 5 to update task in completed task list\n  "
            "Enter 6 to exit\n"
            "Please enter your choice here: "
        )
        try:
            choice = int(choice)
            if 1 <= choice <= 6:
                return choice
            else:
                print("Please enter a number between 1 and 5.")
        except:
                print("Invalid input. Please enter a number.")
            
def task_manager():
    user_name = input("Enter Your Name: ")
    print(f"Welcome {user_name} to the task manager application.")
    tasks_list = []
    completed_tasks_list=[]

    while True:
        choice = checking_user_input_for_integer()
        if choice == 6:
            print("Exiting the application...")
            break
        else:
            checking_results_for_choice(choice, tasks_list, user_name,completed_tasks_list)

task_manager()