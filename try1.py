# Develop a number guessing game: The computer generates a random number, and the player has to guess it within a certain number of tries. Provide feedback to the player (e.g., "Too high!", "Too low!").

# tasks to do
# 1. make check logic a function
# 2. write test cases for that function, eg: assert 3 == 3, assert 3 == 5 , assert 3 == somefunction(12)
# 3. Handle string as value, handle blank as value, handle out of range values
# 4. input range from user
# 5. input attempts from user, where attempts should be less than equal to number of total values in the range
# 6. Create a feedback loop via the logic function which returns high, low or correct
def incorrect_input(num , guess ):
    print("THE INPUT YOU DID IS INCORRECT OR OUT OF RANGE ")
    
def check_value(num,guess):
    if(num==guess ):
        return True

    else:
        return False
    
import random
num = random.randint(1,11)
tries=5
print(num)

for i in range(tries) :
    guess=input("Enter your guess from 1 to 11  : ")
    
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