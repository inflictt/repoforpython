# Develop a number guessing game: The computer generates a random number, and the player has to guess it within a certain number of tries. Provide feedback to the player (e.g., "Too high!", "Too low!").
import random
num = random.randint(1,11)
print(num)
for i in range(11) :
    guess=int(input("ENTER THE NUMBER YOU GUESSED  : "))
    if(num==guess ):
        print("yay! right guess ")
        print("and! the number was :", num)
        print("you took thiss much tries:",)
        print("and this much tries were left : ",)
        break
    else:
        print("oops wrong number now you have this much guess left : ",range)
print("number generated by the system was : ", num)
