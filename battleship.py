from random import randint

board = []
ship_locs = []

for x in range(0, 5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print " ".join(row)



def random_row(board):
    return randint(1, len(board))

def random_col(board):
    return randint(1, len(board[0]))

def ship_maker(board):
    for i in range(len(board)):
        ship_row = random_row(board)
        ship_col = random_col(board)
        while [ship_row, ship_col] in ship_locs:
            ship_row = random_row(board)
            ship_col = random_col(board)
        ship_locs.append([ship_row, ship_col])

ship_maker(board)



def play_game(board):
    p1_score = 0
    p2_score = 0
    for turn in range(5):
        player = 0
        while player < 2:
            player += 1
            print_board(board)
            print "Turn", turn + 1
            print "Player 1 Score:", p1_score
            print "Player 2 Score:", p2_score
            print "Player", str(player) + ":", "your move!"
            guess_row = int(raw_input("Guess Row:"))
            guess_col = int(raw_input("Guess Col:"))
            
            if [guess_row, guess_col] in ship_locs:
                print "Congratulations! You sank my battleship!"
                board[guess_row - 1][guess_col - 1] = "B"
                if player == 1:
                    p1_score += 1
                else:
                    p2_score += 1
            else:
                if guess_row not in range(1, len(board)+1) or \
                   guess_col not in range(1, len(board[0])+1):
                       print "Oops, that's not even in the ocean."
                elif board[guess_row - 1][guess_col - 1] == "X" or \
                     board[guess_row - 1][guess_col - 1] == "B":
                    print "You guessed that one already."
                else:
                    print "You missed my battleship!"
                    board[guess_row - 1][guess_col - 1] = "X"
            if turn == 4:
                print " "
                print "Game Over"
                if p1_score > p2_score:
                    print "Winner: Player 1"
                elif p1_score == p2_score:
                    print "Tie game!"
                else:
                    print "Winner: Player 2"
                    
        
        
play_game(board)