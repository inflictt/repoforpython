# Develop a number guessing game: The computer generates a random number, and the player has to guess it within a certain number of tries. Provide feedback to the player (e.g., "Too high!", "Too low!").

# tasks to do
# 1. make check logic a function
# 2. write test cases for that function, eg: assert 3 == 3, assert 3 == 5 , assert 3 == somefunction(12)
# 3. Handle string as value, handle blank as value, handle out of range values
# 4. input range from user
# 5. input attempts from user, where attempts should be less than equal to number of total values in the range
# 6. Create a feedback loop via the logic function which returns high, low or correct
def check_if_num_intger(user_message):
    while True:
        num1 = input(user_message)
        try:
            num1= int(num1)
            return num1

        except:
            print("number entered incorrectly ")

def range_input():
    user_message = "enter value for Lower bound : "
    lower_bound= check_if_num_intger(user_message)
    user_message = "enter value for Upper bound : "
    upper_bound= check_if_num_intger(user_message)
    while lower_bound>=upper_bound:
        print(f"you have entered upper bound which = {upper_bound} less than or equal lower bound = {lower_bound} ")
        upper_bound=check_if_num_intger(user_message)
    return lower_bound,upper_bound


def guess_input(lower_bound,upper_bound):
    while True:
        guess=check_if_num_intger(f"Enter your guess from {lower_bound} to {upper_bound}  : ")
        if guess>=lower_bound and guess<=upper_bound:
            return guess 
        else: 
            print (f"you guessed {guess} which is out of {lower_bound} to {upper_bound} renter it ")
            
def check_value(num,guess):
    if(num==guess ):
        return True
    elif num<guess:
        print("the guessed number is greater than correct number")
    else:
        print("the guessed number is lesser than correct number")
    return False
def main():   
    import random
    limit = range_input()
    lower_bound=limit[0]
    upper_bound=limit[1]
    num = random.randint(lower_bound,upper_bound)
    tries=upper_bound-lower_bound+1

    for left in range(tries,0,-1) :
        guess= guess_input(lower_bound,upper_bound)
        value = check_value(num , guess )
        print("number of tries left are : ",left-1)

        if (value==True) :
            print("right answer bro ")
            break
        elif(left==0):
            print ("oh no zero tries left now and the number was : ", num )
    assert check_value(2,3) == False 
# assert check_value(11,11) == True 
main()