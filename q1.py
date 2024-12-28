# Develop a number guessing game: The computer generates a random number, and the player has to guess it within a certain number of tries. Provide feedback to the player (e.g., "Too high!", "Too low!").
import random
num = random.randint(1,11)
# print(num)
guess1=int(input("ENTER THE NUMBER YOU GUESSED FIRST : "))
guess2=int(input("ENTER THE NUMBER YOU GUESSED SECOND : "))
guess3=int(input("ENTER THE NUMBER YOU GUESSED THIRD : "))
if(num==guess1 or num==guess2 or num ==guess3):
    print("yayyyyyy!!!! right guess ")
    print("and the number was :", num)
else:
    print("aee vediyaaa !!!! galat jawab")
    print("correct number was :",num)