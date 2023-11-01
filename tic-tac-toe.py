#importing random module
import random

#list of board contains 10 ' ' spaces 
board = [' ' for x in range(10)]

#possibleMoves = [x for x,letter in enumerate(board) if letter == ' ' and x!=0]
#print(possibleMoves)

#checking wether there is space is free in choosing option 
def spaceIsFree(pos):
    return board[pos] == ' '

#changing ' ' to letter by computer or user
def insertLetter(letter,pos):
    board[pos] = letter

#there is 10 spaces in list of board... if ' '.count ==1 means the board is full
def isBoardFull(board):
    if board.count(' ') > 1:    #count of " " are 10 in board....
        return False    #means the board is not full
    else:
        return True     #means the board is full


def printBoard(board):
    print("   |   |   ")
    print(" " + board[1] + " | " + board[2] + " | " + board[3] + " ")
    print("   |   |   ")
    print("-----------")
    print("   |   |   ")
    print(" " + board[4] + " | " + board[5] + " | " + board[6] + " ")
    print("   |   |   ")
    print("-----------")
    print("   |   |   ")
    print(" " + board[7] + " | " + board[8] + " | " + board[9] + " ")
    print("   |   |   ")

#printBoard(board)

#return true if any of the condition is true by player or computer
def isWinner(b,l):
    return ((b[1] == l and b[2] == l and b[3] == l) or 
    (b[4] == l and b[5] == l and b[6] == l) or 
    (b[7] == l and b[8] == l and b[9] == l) or 
    (b[1] == l and b[4] == l and b[7] == l) or 
    (b[2] == l and b[5] == l and b[8] == l) or 
    (b[3] == l and b[6] == l and b[9] == l) or 
    (b[1] == l and b[5] == l and b[9] == l) or
    (b[3] == l and b[5] == l and b[7] == l) )


def playerMove():
    run = True
    while run:
        move = input("please select a position to exnter X between 0 and 9 : ")
        #using try and catch beacause if the input from user is must be an integer...
        try:
            #if the input from user is not an integer.. it shows an error so we use try catch
            move=int(move)
            if move > 0 and move < 10 :
                #checking wether is space occupancy for player move 
                #spaceIsFree(move) give true if there is space
                if spaceIsFree(move):
                    #to stops the while loop make run as false
                    run = False
                    #inset the player 'X' in board
                    insertLetter("X" , move)
                else:
                    print("Sorry, The space is Occupies...")
            else:
                print("enter a valid number between 0 and 9 : ")
        except:
            print("Please type a number between 1 and 9 : ")

#there is confusing in computer move
def computerMove():
    #list of possible moves in the board by checking spaces
    possibleMoves = [x for x,letter in enumerate(board) if letter == ' ' and x!=0]
    move = 0

    #checking who is about to win by which position..
    #make a move of that position
    for let in ["O" , "X"]:
        for i in possibleMoves:
            boardCopy = board[:]
            boardCopy[i] = let  
            if isWinner(boardCopy,let):
                move = i
                return move

    cornersOpen = []
    for i in possibleMoves:
        if i in [1, 3, 7, 9]:
            cornersOpen.append(i)

    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move

    if 5 in possibleMoves:
        move = 5
        return move

    edgeMoves = []
    for i in possibleMoves:
        if i in [2, 4, 6, 8]:
            edgeMoves.append(i)

    if len(edgeMoves) > 0:
        move = selectRandom(edgeMoves)
        return move
            

def selectRandom(li):
    ln = len(li)
    r = random.randrange(0,ln)
    return li[r]


def main():
    print("Welcome to Tic Tac Toe game :")
    printBoard(board)

    #checking wether the board is full or not...??
    #if the board is not fill... loops runs!!!
    while not(isBoardFull(board)):         
        #checking wether the computer is win or loose.... for having player move
        if not(isWinner(board , 'O')):     
            #if computer is about to play there is no win of any or tie... there is move of player 
            playerMove()        
            printBoard(board)
        #else part if the computer wins the game 
        else:
            print("Sorry, You loose...!!")
            break
        
        #checking wether the player may win or loose....
        if not(isWinner(board, 'X')):
            #after the computer move.. system check that is player wins or not..??   thus it gives the computer move..
            move = computerMove()
            #after completing the computermove it returns move..
            if move == 0:       #we also defining the move variable in computerMove() also..
                #print("Tie game...!!")
                print(' ')

            #this loop for making computer move randomly 
            elif isBoardFull(board) ==False :
                insertLetter('O', move)
                print("computer placed O on position : ",move)
                printBoard(board)
        #else part if the player wins..
        else:
            print("you Win..!!")
            break
    
    #if the board is full and both are not win..
    if isBoardFull(board):
        print("Tie game...!!")


#Tic Tac Toe Game starts here...
s = input("do you want to play? [y/n]")
while True:
    if s.lower() == 'y':
        board = [' ' for x in range(10)]
        #printBoard(board)
        print("--------------")
        #main() function to implement the game
        main()
        #at the end of game ask again to play???
        s = input("do you want to play again ? [y/n]")
    elif s.lower() == 'n':
        break


