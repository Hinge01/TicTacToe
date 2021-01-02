currentBoard = {"1":" ","2":" ","3":" ",
                "4":" ","5":" ","6":" ",
                "7":" ","8":" ","9":" "}

def Printboard(board):
    print(board["1"]+" | "+board["2"]+" | "+board["3"])
    print("--+---+--")
    print(board["4"]+" | "+board["5"]+" | "+board["6"])
    print("--+---+--")
    print(board["7"]+" | "+board["8"]+" | "+board["9"])

def game():

    turn = 1
    game = True

    Printboard(currentBoard)
    playedMoves = []
        
    while game == True:    

        if(turn % 2 != 0):
            player = "X"
        else:
            player = "O"       
        
        print("It is "+player+"'s turn") 

        played = input() 
                    
        if played not in playedMoves:
            currentBoard[played] = player
            Printboard(currentBoard)
            playedMoves.append(played)
            turn += 1
        else:
            print("invalid") 
        
        currentPlayer = player

        if currentBoard["1"] == currentPlayer and currentBoard["2"] == currentPlayer and currentBoard["3"] == currentPlayer:
            print(player + " won!")   
            game = False           
        elif currentBoard["1"] == currentPlayer and currentBoard["4"] == currentPlayer and currentBoard["7"] == currentPlayer:
            print(player + " won!")               
            game = False 
        elif currentBoard["1"] == currentPlayer and currentBoard["5"] == currentPlayer and currentBoard["9"] == currentPlayer:
            print(player + " won!")             
            game = False   
        elif currentBoard["2"] == currentPlayer and currentBoard["5"] == currentPlayer and currentBoard["8"] == currentPlayer:
            print(player + " won!")  
            game = False              
        elif currentBoard["3"] == currentPlayer and currentBoard["5"] == currentPlayer and currentBoard["7"] == currentPlayer:
            print(player + " won!")  
            game = False              
        elif currentBoard["3"] == currentPlayer and currentBoard["6"] == currentPlayer and  currentBoard["9"] == currentPlayer:
            print(player + " won!") 
            game = False               
        elif currentBoard["4"] == currentPlayer and currentBoard["5"] == currentPlayer and currentBoard["6"] == currentPlayer:
            print(player + " won!") 
            game = False               
        elif currentBoard["7"] == currentPlayer and currentBoard["8"] == currentPlayer and currentBoard["9"] == currentPlayer:
            print(player + " won!")  
            game = False              
        elif turn == "10":
            print("Its a tie")
            game = False
        
        if played == "Stop":
            game = False      

        
game()
input()








