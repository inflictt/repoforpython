# Develop a number guessing game: The computer generates a random number, and the player has to guess it within a certain number of tries. Provide feedback to the player (e.g., "Too high!", "Too low!").

# tasks to do
# 1. make check logic a function
# 2. write test cases for that function, eg: assert 3 == 3, assert 3 == 5 , assert 3 == somefunction(12)
# 3. Handle string as value, handle blank as value, handle out of range values
# 4. input range from user
# 5. input attempts from user, where attempts should be less than equal to number of total values in the range
# 6. Create a feedback loop via the logic function which returns high, low or correct

def check_value():
    if(num==guess ):
        print("right answer bro ")
        return True

    else:
        print("oops wrong number now you have this much guess left : ",tries-i) 
        return False
import random
num = random.randint(1,11)
tries=5
print(num)
for i in range(tries) :
    guess=int(input("ENTER THE NUMBER YOU GUESSED  : "))
    value = check_value()
    if (value==True) :
        break
    # print("number of tries left are : ", tries)

# assert num == guess
