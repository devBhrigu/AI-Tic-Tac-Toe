#TicTacToeGame

#print("Hello World")

board = [ '' for x in range(10)]

def insert_letter(letter, pos): 
    board.pause = letter

def space_free(pos): 
    return board[pos] == ' '

def print_board(board): 
    print('   |    |')
    print(' ' + board[1] + '  |' + board[2] + "  | " + board[3])
    print("   |    |")
    print("----------")
    print("   |    |")
    print(' ' + board[4] + '  |' + board[5] + "  | " + board[6])
    print("   |    |")
    print("----------")
    print("   |    |")
    print(' ' + board[7] + '  |' + board[8] + "  | " + board[9])
    print("   |    |")

#Define to know when board is fully populated 
def is_winner(board, letter): 
    return(
    (board[7] == letter and board[8] == letter and board[9] == letter) or #Check for rows to be populated
    (board[4] == letter and board[5] == letter and board[6] == letter) or 
    (board[1] == letter and board[2] == letter and board[3] == letter) or 
    (board[1] == letter and board[4] == letter and board[7] == letter) or  #Check for coloumns to be populated
    (board[2] == letter and board[5] == letter and board[8] == letter) or 
    (board[3] == letter and board[6] == letter and board[9] == letter) or 
    (board[1] == letter and board[5] == letter and board[9] == letter) or  #Check for diagnols to be populated 
    (board[3] == letter and board[5] == letter and board[7] == letter) 
    ) 

def player_move(): 
    run = True 
    while run: 
        move  = input("Please select a position to place a X. Use number 1-9 for a position. ")
        try: 
            move = int(move)
            if move > 0 and move < 10: 
                if space_free(move): 
                    run = False
                    insert_letter('X', move)
                else: 
                    print("Sorry the space is full. ")
            else: 
                print("Please enter a valid position, within the range.")
        except: 
            print("Please enter a number.")

def comp_move(): 
    possible_moves = [x for x, letr in enumerate(board) if letr == ' ' and x != 0] 
    move = 0 

    for letr in ['O', 'X']: #Check if computer can win, and if can insert O into that position. Check if player can win after, and if can win insert O into that position. 
        for i in possible_moves:
            board_copy = board[:]
            board_copy[i] = letr
            if is_winner(board_copy, letr): 
                move = i
                return move
    
    corners_open = [' '] #Check if corner is open and if it is not 
    for i in possible_moves: 
        for i in [1, 3, 7, 9]: 
            corners_open.append(i)
    if len(corners_open) > 0: 
        move = select_random(corners_open)
        return move

    if 5 in possible_moves: #Check if center of board is open
        move = 5
        return move
    
    edges_open = [' ']   #Check if edges of board are open 
    for i in possible_moves: 
        for i in [2, 4, 6, 8]: 
            edges_open.append(i)
    if len(edges_open) > 0: 
        move = select_random(edges_open)
    
    return move

def select_random(list): 
    import random
    ln = len(list) 
    r = random.randrange(0, ln)
    return list[r]

def is_board_full(board): 
    if board.count(' ') > 1: 
        return True
    else:
        return False 

def main(): 
    print("You are playing Tic Tac Toe!")
    print_board(board)
    
    while not(is_board_full(board)): 
        if not(is_winner(board, "O")):   #Check to see if computer has won
            player_move()
            print_board(board)
        else: 
            print("Computer Win.")
            break
            
        if not(is_winner(board, "X")):   #Check to see if player has won
            move = comp_move()
            if move == 0:
                print("Tie Game") 
            else: 
                insert_letter('O')
                print("Computer place O in position", move, ":")
                print_board(board)
        else: 
            print("Player Win.")
            break
    
    
    if is_board_full(board): 
        print("Tie Game!")
        