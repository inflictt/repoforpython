# Create a rock-paper-scissors game: Allow the user to play rock-paper-scissors against the computer. Use random number generation to determine the computer's choice.
def checking_move_if_integer(user_message):
        while True : 
            move= input(user_message)
            try:
                move=int(move)
                return move
            except:
                print(f"You entered {move} which is incorret retry again . ")
        

def score_checking(comp_move,user_move,comp_score,user_score):
    if comp_move==user_move:
        print("no points awarded")
    elif comp_move>user_move:
        comp_score+=1
        print("1 point awarded to computer ")
    else:
        user_score+=1
        print("1 point awarded to user ")
    print("computer score = ", comp_score, "user score = ", user_score)
    return comp_score,user_score

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
for i in round :
    comp_score= 0 
    user_score = 0
    comp_move=computer_move()
    user_move= your_move()        
    print("computer played : " , comp_move)
    print("user played : " , user_move)
    final_score= score_checking(comp_move,user_move,comp_score,user_score)
    
    