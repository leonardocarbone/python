# SUPER SIMPLE, VERY SIMPLE TIC TAC TOE GAME (TWO PLAYERS)

import os
import random
import re

game_state =  None

def print_board():
    os.system("clear")
    board = game_state["board"]
        
    print "{:^50}".format("TIC TAC TOE SUPER GAME")
    print ""

    print "X - Wins: {0}       O - Wins: {1}".format(game_state["X"], game_state["O"])
    print ""

    print " Game Positions"  
    print "    1|2|3         {0}|{1}|{2}".format(board[0], board[1], board[2])
    print "    -----         -----"
    print "    4|5|6         {0}|{1}|{2}".format(board[3], board[4], board[5])
    print "    -----         -----"
    print "    7|8|9         {0}|{1}|{2}".format(board[6], board[7], board[8])
    
    print ""
    
    if(game_state["error"]):
        print game_state["error"]

    if(game_state["winner"]):
        print "THE WINNER IS {0}".format(game_state["marker"])

    if(game_state["tied"]):
        print "GAME TIED!"
    
def check_full_board():
    board = "".join(game_state["board"]).replace(" ","")
    if(len(board) == 9):
        game_state["winner"] = False
        game_state["tied"] = True    

def check_winner():
    match_patterns = ['100100100',
                      '010010010',
                      '001001001',
                      '111000000',
                      '000111000',
                      '000000111',
                      '100010001',
                      '001010100']
                      
                     
    board = "".join(game_state["board"]).replace(game_state["marker"],"1")
    board = re.sub("[^1]","0",board)
        
    if(board in match_patterns):    
        game_state["winner"] = True
        game_state[game_state["marker"]]+=1
    
def next_marker():
    if(game_state["marker"] == "X"):
        game_state["marker"] = "O"
    else:
        game_state["marker"] = "X"


def new_game_state():
    global game_state

    score_X = 0
    score_O = 0

    if(game_state != None):
        score_X = game_state["X"]
        score_O = game_state["O"]


    game_state = { "X" : score_X,
                   "O" : score_O,
                   "marker" : random.choice(["X","O"]),
                   "winner" : None,
                   "tied"   : False,
                   "error"  : "",
                   "board" : [" ", " ", " ", " ", " ", " ", " ", " ", " "]
                }

def game():
    
    another_game = "Y"    
    while another_game.upper() != "N":
        new_game_state()
        print_board()

        while game_state["winner"] == None:           
            
            position = raw_input("Enter your position for marker '{0}': ".format(game_state["marker"]))
            
            game_state["error"] = ""

            if(len(position) > 0 and position in "123456789"):
                position = int(position)-1                
                if(game_state["board"][position] == " "):
                    game_state["board"][position] = game_state["marker"] 
                    check_winner()
                    if(not game_state["winner"]):
                        check_full_board()
                        if(not game_state["tied"]):
                            next_marker()
                else:
                    game_state["error"] = "Invalid position, try again!"
            else:
                game_state["error"] = "Invalid position, try again!"

            
            print_board()

            
        print ""
        another_game = raw_input("Another game? (Y/N): ")


game()