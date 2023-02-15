"""
Adam Strotman
Tic Tac Toe
"""
import itertools

def win(current_game):
    def all_same(l):
        if l.count(l[0])== len(l) and l[0] != 0:
            return True
        else:
            return False
    #horizontial
    for row in game:
        print (row)
        if all_same(row):
            print("Winner")
    #vertical
    for column in range(len(game)):
        check=[]
        for row in game:
            check.append(row[column])  
        if all_same(check):
            print("Winner")
    #diagonal 
    diags =[]       
    col = reversed(range(len(game)))
    row = range(len(game))
    
    for col, row, in zip(col, row):
        print(col, row)
        diags.append(game[row][col])
        if all_same(diags):
            print("Winner")
    
    diags = []
    for i in range(len(game)):
        diags.append(game[i][i])
        if all_same(diags):
            print("Winner")
    return False


def game_board(game_map, player= 0, row= 0, column= 0, just_display= False):
    try:
        if game_map[row][column] != 0:
            print("Someone has played in this position. Choose another.")
            return game_map, False
        print("   0  1  2")
        if not just_display:
            game_map[row][column] = player
        for count, row in enumerate (game_map):
            print (count,row)
        return True
    except IndexError as e:
        print("Error: make sure you input row/column as 0, 1, 2", e)
        return game_map, False
    except Exception as e:
        print ("Something went wrong", e)
        return game_map, False

play = True
players=[1,2]
while play:
    game = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],]
    game_won = False
    game= game_board(game, just_display= True)
    player_choice= itertools.cycle([1,2])
    while not game_won:
        current_player= next(player_choice)
        print(f"Current Player: " , current_player)
        played = False
        while not played:
            column_choice = int(input("Pick a column: "))
            row_choice = int(input("Pick a row: "))
            game, played = game_board(game, current_player, row_choice, column_choice)
        
        if win(game):
            game_won = True
            play_again = input("Would you like to play again? y/n ")
            if play_again.lower() == "y":
                play = True
            else:
                print("Goodbye")
                play = False

            

