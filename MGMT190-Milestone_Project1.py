import random

def display_board (board):
    count = 0
    print("-------------")
    for i in board[1:]:
        if count % 3 == 0:
            print("|", end = "")
        print(" " + i + " |",end = "")
        count += 1
        if count % 3 == 0:
            print("\n-------------")

def player_input():
    p_i = ""
    while True:
        p_i = input("Please pick a marker 'X' or 'O': ")
        if p_i == 'X' or p_i == 'O':
            return p_i
        print("you put something wrong, please pick again")

def place_marker(board, marker, position):
    board[position] = marker
    return board

def win_check(board, mark):
    
    index = [(1,2,3), (4,5,6), (7,8,9), (1,4,7), (2,5,8), (3,6,9),(1,5,9), (3,5,7)] 
    
    ## check if mark wins
    for i, j, k in index:
        if board[i] == board[j] == board[k] == mark:
            return mark
    return False

def choose_first():
    return random.choice((-1, 1))

def space_check(space):
    return True if board[space] == " " else False

def full_board_check():
    for i in board:
        
        ## if there is still a space in the board
        if i == " ":
            return False
    
    ## if the space is full
    return True

def player_choice(board):
    space = ""
    l = [str(i) for i in range(1,10)]
    
    ## if space is in the range and space_check is true, the while-loop will break.
    while True:
        space = input("what is your next position: ")

        if space not in l: 
            print("you put something wrong! please input number from 1 to 9")
        elif not space_check(int(space)):
            print("the position you put is full, please choose other position")
        else: 
            return space

def replay():
    while True:
        answer = input(" if you want to play again? please type 'Y' or 'N': ")
        if answer.upper() == "Y":
            return True
        elif answer.upper() == "N":
            return False


# Put everything together

print ("Welcome to the best Tic-Tac-Toe game ever designed!")
user = {-1: "user 1", 1: "user 2"}
choose = 1
while True:
    #setup the game here
    board = ["#", " ", " ", " ", " ", " ", " ", " ", " ", " "]
    choose = choose_first()
    print(f'{user[choose]} will start first: \n')
    display_board(board)
    game_on = True
    print()
    while game_on:
        print(f"it is now {user[choose]}'s turn")
        mark = player_input()
        space = int(player_choice(board))
        place_marker(board, mark, space)
        display_board(board)
        
        if win_check(board, mark) != False:
            print(f"{user[choose]} wins")
            game_on = False
        
        if full_board_check():
            print("we have a tie here")
            game_on = False
        
        choose = - choose
        
    if not replay():
        break




