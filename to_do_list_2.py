from datetime import date
from sympy import oo

def number_of_tasks():
    while True:
        num_tasks=input("Enter the number of tasks you want to deal with : ")
        try:
            num_tasks=int(num_tasks)
            if num_tasks>0 and num_tasks<oo:
                return num_tasks
            else:
                print("Wrong range inputed for number of tasks . ")
        except:
            print("Please enter a correct input . ")
        
        
def checking_results_for_choice(choice,tasks_list,num_tasks):
        if choice==1: #means users want to create a list 
            print(f"Creating A list For {user_name}")
            for i in range(1,num_tasks+1):
                task_details=input(f"Enters the details for Task{i} = ")
                i = i+1
                tasks_list.append(task_details)
        
            
def checking_user_input_for_integer():
    while True :
        choice = input("Enter 1 to create a list\nEnter 2 to edit/update the list\nEnter 3 to delete the list\nEnter 4 to view the list\nEnter 5 to exit the list\nPlease enter your choice here : ")
        try :
            choice= int(choice)
            if (choice>0 and choice<6):
                return choice 
            else:
                print("wrong range inputed . ")
        except:
            print("Entered value is not a correct input for the choice . ")
            
            
user_name=input("Enter Your Name  : ")
print(f"Welcome {user_name} to the task manager application . ")
choice = checking_user_input_for_integer()
tasks_list=[]
if choice==5:
        print("Exitng the application....")
else:            
    num_tasks=number_of_tasks()
    checking_results_for_choice(choice,tasks_list,num_tasks)
print(tasks_list)