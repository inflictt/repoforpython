# Create a rock-paper-scissors game: Allow the user to play rock-paper-scissors against the computer. Use random number generation to determine the computer's choice.
from enum import Enum

class Name(Enum):
    USER = input("enter your name:")          
    COMPUTER = "Computer" 
    DRAW = "Draw"  
    
def making_moves_input(round,round_winner_list):
    for index, i in enumerate(round,start = 1) :

        comp_move=computer_move()
        user_move= your_move()   
        print(f"{index}) computer played : {comp_move} \t {index}) {Name.USER.value} played :  {user_move}")
        final_score= round_winner(comp_move,user_move)
        round_winner_list.append(final_score)
        print(f"Round {index} won by :  {round_winner_list[i]}")     

  
def showcasing_round_winner(round,round_winner_list,user_score,comp_score):
    for index,i in enumerate(round,start=1) :    
        if round_winner_list[i]==Name.USER:
            user_score=user_score+1
        elif round_winner_list[i]==Name.COMPUTER:
            comp_score=comp_score+1
    return user_score, comp_score


def final_scoring_results(comp_score,user_score):
    print(f"computer score is {comp_score} \t {Name.USER.value} score is {user_score}")
    if user_score>comp_score:
        print(f"{Name.USER.value} won the game ")
    elif user_score<comp_score:
        print("computer won the game ")
    else:
        print("game tied") 
        
def checking_move_if_integer(user_message):
        while True : 
            move= input(user_message)
            try:
                move=int(move)
                return move
            except:
                print(f"You entered {move} which is incorret retry again . ")
        

def round_winner(comp_move,user_move):

    if comp_move==user_move:
        return Name.DRAW
    if user_move==2:
        if comp_move==1:
            return Name.USER
        else :
            return Name.COMPUTER 
    if user_move== 3 :
        if comp_move==2:
            return Name.USER
        else :
            return  Name.COMPUTER 
    if user_move==1:
        if comp_move==2:
            return  Name.COMPUTER 
        else :
            return Name.USER
    
    
def computer_move():
    computer = random.randint(1,3)
    return computer

def your_move():
    while True : 
        move= checking_move_if_integer(f"Please {Name.USER.value} enter: ")
        if move >0 and move<4:
            return move 
        else:
            print("user move incorrect input")
        
            
import random 
print("Rock Paper and Scissors ")
print("Enter 1 for Rock \nEnter 2 for Paper \nEnter 3 for Scissors")
rounds = int (input("enter number of round you want to play : "))
round= range(rounds)
comp_score= 0 
user_score = 0
round_winner_list = []
making_moves_input(round,round_winner_list)
user_score , comp_score = showcasing_round_winner(round, round_winner_list, user_score, comp_score)
final_scoring_results(comp_score,user_score)


    
assert round_winner(1,1)==Name.DRAW
assert round_winner(2,2)==Name.DRAW
assert round_winner(3,3)==Name.DRAW
assert round_winner(1,2)==Name.USER
assert round_winner(1,3)==Name.COMPUTER 
assert round_winner(2,1)==Name.COMPUTER 
assert round_winner(2,3)==Name.USER
assert round_winner(3,1)==Name.USER
assert round_winner(3,2)==Name.COMPUTER 