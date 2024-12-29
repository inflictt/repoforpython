# Create a rock-paper-scissors game: Allow the user to play rock-paper-scissors against the computer. Use random number generation to determine the computer's choice.
USER="user"
DRAW="draw"
COMPUTER="computer" 

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
        return DRAW
    if user_move==2:
        if comp_move==1:
            return USER
        else :
            return COMPUTER 
    if user_move== 3 :
        if comp_move==2:
            return USER
        else :
            return  COMPUTER 
    if user_move==1:
        if comp_move==2:
            return  COMPUTER 
        else :
            return USER
    
    
def computer_move():
    computer = random.randint(1,3)
    return computer

def your_move():
    while True : 
        move= checking_move_if_integer("Please user enter: ")
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
for i in round :

    comp_move=computer_move()
    user_move= your_move()        
    print("computer played : " , comp_move)
    print("user played : " , user_move)
    final_score= round_winner(comp_move,user_move)
    round_winner_list.append(final_score)
  
for i in round :    
    if round_winner_list[i]==USER:
        user_score=user_score+1
    elif round_winner_list[i]==COMPUTER:
        comp_score=comp_score+1
    
print(f"computer score is {comp_score} \n user score is {user_score}")
if user_score>comp_score:
    print("user won the game ")
elif user_score<comp_score:
    print("computer won the game ")
else:
    print("game tied") 
    
    
assert round_winner(1,1)==DRAW
assert round_winner(2,2)==DRAW
assert round_winner(3,3)==DRAW
assert round_winner(1,2)==USER
assert round_winner(1,3)== COMPUTER 
assert round_winner(2,1)== COMPUTER 
assert round_winner(2,3)==USER
assert round_winner(3,1)==USER
assert round_winner(3,2)== COMPUTER 