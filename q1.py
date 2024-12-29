# Develop a number guessing game: The computer generates a random number, and the player has to guess it within a certain number of tries. Provide feedback to the player (e.g., "Too high!", "Too low!").

# tasks to do
# 1. make check logic a function
# 2. write test cases for that function, eg: assert 3 == 3, assert 3 == 5 , assert 3 == somefunction(12)
# 3. Handle string as value, handle blank as value, handle out of range values
# 4. input range from user
# 5. input attempts from user, where attempts should be less than equal to number of total values in the range
# 6. Create a feedback loop via the logic function which returns high, low or correct
def check_if_num_intger(user_message):
    num1 = input(user_message)
    try:
        num1= int(num1)
        # return lower_bound
    except:
        print("num1 entered incorrectly ")
    return num1
    



def range_input():
    user_message = "enter value for Lower bound : "
    lower_bound= check_if_num_intger(user_message)
    user_message = "enter value for Upper bound : "
    upper_bound= check_if_num_intger(user_message)
    while lower_bound>upper_bound:
        print(f"you have entered upper bound which = {upper_bound} less than lower bound = {lower_bound} ")
        upper_bound=int(input("Enter the upper value :  "))
    return lower_bound,upper_bound


def guess_input(lower_bound,upper_bound):
    guess=input(f"Enter your guess from {lower_bound} to {upper_bound}  : ")
    try :
        guess = int(guess)
        if guess>=lower_bound and guess<=upper_bound:
            return guess 
        else: 
            print (f"entered input is {guess} which is out of {lower_bound} to {upper_bound} ")
    except ValueError:
        print(f"the input is {guess} which entered is wrong as expected values are supposed to be integers  ")

    
def check_value(num,guess):
    if(num==guess ):
        return True

    else:
        return False
    
import random
limit = range_input()
print(limit)
lower_bound=limit[0]
upper_bound=limit[1]
num = random.randint(lower_bound,upper_bound)
tries=5
print(num)

for i in range(tries) :
    # guess=input("Enter your guess from 1 to 11  : ")
    guess= guess_input(lower_bound,upper_bound)
    value = check_value(num , guess )
    left = tries-1-i
    print("number of tries left are : ",left)

    if (value==True) :
        print("right answer bro ")
        break
    elif(left==0):
        print ("oh no zero tries left now and the number was : ", num )
# assert check_value(2,3) == False 
# assert check_value(11,11) == True 