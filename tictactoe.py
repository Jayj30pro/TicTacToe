import time
import os

gameboard = [["-","-","-"],
             ["-","-","-"],
             ["-","-","-"],]

demoboard = 'row 1 spaces: 1|2|3 \nrow 2 spaces: 1|2|3 \nrow 3 spaces: 1|2|3 \n'

currentplayer = "X"

running = 0

def clear_screen():

    # It is for MacOS and Linux(here, os.name is 'posix')
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        # It is for Windows platfrom
        _ = os.system('cls')

def setboard():
    clear_screen()
    print("\n\n\n")
    for i in gameboard:
        print(i)


def getMove():
    setboard()
    print("\n\n\n")
    print("It is the " + currentplayer + "'s trun")
    row = input("Which row? ")
    if "exit" in row:
        return False
    space = input("Which space ")
    if "exit" in space:
        return False
    else:
        checkMove(row,space)


def checkMove(row,space):
    try:
        if int(row) > 3:
            print("The row should be 1,2,or 3")
            time.sleep(3)
            getMove()
        elif int(row) < 1:
            print("The row should be 1,2,or 3")
            time.sleep(3)
            getMove()
        elif int(space) > 3:
            print("The space should be 1,2,or 3")
            time.sleep(3)
            getMove()
        elif int(space) < 1:
            print("The space should be 1,2,or 3")
            time.sleep(3)
            getMove()
        else:openSpace(row,space)

    except:
        print("invalid entry \n Please try again")
        time.sleep(3)
        getMove()


def openSpace(row,space):
    x = int(row) - 1
    y = int(space) -1
    if gameboard[x][y] != "-":
        print("This space is taken\n Try again.")
        time.sleep(3)
        getMove()        
    else:
        setMove(row,space)

def setMove(row,space):
    x = int(row) - 1
    y = int(space) -1
    gameboard[x][y] = currentplayer
       

def intro():
    print("welcome to Tic Tac Toe")
    

def checkBoard():
    if gameboard[0][0] == "X" and gameboard[0][1] == "X" and gameboard[0][2] == "X":
        clear_screen()
        print("\n\n\n")
        print("X is the winner!!!")
        return True
    elif gameboard[0][0] == "O" and gameboard[0][1] == "O" and gameboard[0][2] == "O":
        clear_screen()
        print("\n\n\n")
        print("O is the winner!!!")
        return True
    elif gameboard[1][0] == "X" and gameboard[1][1] == "X" and gameboard[1][2] == "X":
        clear_screen()
        print("\n\n\n")
        print("X is the winner!!!")
        return True
    elif gameboard[1][0] == "O" and gameboard[1][1] == "O" and gameboard[1][2] == "O":
        clear_screen()
        print("\n\n\n")
        print("O is the winner!!!")
        return True
    elif gameboard[2][0] == "X" and gameboard[2][1] == "X" and gameboard[2][2] == "X":
        clear_screen()
        print("\n\n\n")
        print("X is the winner!!!")
        return True
    elif gameboard[2][0] == "O" and gameboard[2][1] == "O" and gameboard[2][2] == "O":
        clear_screen()
        print("\n\n\n")
        print("O is the winner!!!")
        return True
    elif gameboard[0][0] == "X" and gameboard[1][0] == "X" and gameboard[2][0] == "X":
        clear_screen()
        print("\n\n\n")
        print("X is the winner!!!")
        return True
    elif gameboard[0][0] == "O" and gameboard[1][0] == "O" and gameboard[2][0] == "O":
        clear_screen()
        print("\n\n\n")
        print("O is the winner!!!")
        return True
    elif gameboard[0][1] == "X" and gameboard[1][1] == "X" and gameboard[2][1] == "X":
        clear_screen()
        print("\n\n\n")
        print("X is the winner!!!")
        return True
    elif gameboard[0][1] == "O" and gameboard[1][1] == "O" and gameboard[2][1] == "O":
        clear_screen()
        print("\n\n\n")
        print("O is the winner!!!")
        return True
    elif gameboard[0][2] == "X" and gameboard[1][2] == "X" and gameboard[2][2] == "X":
        clear_screen()
        print("\n\n\n")
        print("X is the winner!!!")
        return True
    elif gameboard[0][2] == "O" and gameboard[1][2] == "O" and gameboard[2][2] == "O":
        clear_screen()
        print("\n\n\n")
        print("O is the winner!!!")
        return True
    elif gameboard[0][0] == "X" and gameboard[1][1] == "X" and gameboard[2][2] == "X":
        clear_screen()
        print("\n\n\n")
        print("X is the winner!!!")
        return True
    elif gameboard[0][1] == "O" and gameboard[1][1] == "O" and gameboard[2][2] == "O":
        clear_screen()
        print("\n\n\n")
        print("O is the winner!!!")
        return True
    elif gameboard[0][2] == "X" and gameboard[1][1] == "X" and gameboard[2][0] == "X":
        clear_screen()
        print("\n\n\n")
        print("X is the winner!!!")
        return True
    elif gameboard[0][2] == "O" and gameboard[1][1] == "O" and gameboard[2][0] == "O":
        clear_screen()
        print("\n\n\n")
        print("O is the winner!!!")
        return True
    elif gameboard[0][0] != "-" and gameboard[0][1] != "-" and gameboard[0][2] != "-" and gameboard[1][0] != "-" and gameboard[1][1] != "-" and gameboard[1][2] != "-" and gameboard[2][0] != "-" and gameboard[2][1] != "-" and gameboard[2][2] != "-":
        clear_screen()
        print("\n\n\n")
        print("Looks like a draw  :-( ")
        return True
    
    
    else:
        return False    
        




# RUNNING CODE STARTS HERE
    

clear_screen()
print("\n\n\n")
print(demoboard)
intro()
startgame = input("Would you like to play?  ")
startgame = startgame.lower()
if "y" in startgame:
    running = 1
    while running == 1:
         
        if getMove() == False:
            running -= 1

        if checkBoard() == True:
            print("And there you have it folks\n It's Over!!" )
            for i in gameboard:
                print(i)
            running -= 1

        if currentplayer == "X":
            currentplayer = "O"
        else:
            currentplayer = "X"    
else:
    print("Thanks for stopping by")

print("Bye Bye")




