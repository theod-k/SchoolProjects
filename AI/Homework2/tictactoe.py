import sys
import random
import math

squares = [["-" for i in range(3)] for j in range(3)]

def display(squares):
    for i in range(3):
        for j in range(3):
            # print(f"printing ({j}, {i})")
            if j != 2:
                print(squares[j][i] + ",", end="")
            else:
                print(squares[j][i], end="\n")
    return("")
        
def checkWin(squares, player):
    #Checking rows
    if (squares[0][0] == player and squares[1][0] == player and squares[2][0] == player):
        return(True)
    if (squares[0][1] == player and squares[1][1] == player and squares[2][1] == player):
        return(True)
    if (squares[0][2] == player and squares[1][2] == player and squares[2][2] == player):
        return(True)
    
    #Checking columns
    if (squares[0][0] == player and squares[0][1] == player and squares[0][2] == player):
        return(True)
    if (squares[1][0] == player and squares[1][1] == player and squares[1][2] == player):
        return(True)
    if (squares[2][0] == player and squares[2][1] == player and squares[2][2] == player):
        return(True)
    
    #Checking diagonals
    if (squares[0][0] == player and squares[1][1] == player and squares[2][2] == player):
        return(True)
    if (squares[0][2] == player and squares[1][1] == player and squares[2][0] == player):
        return(True)
    
    return(False)

def checkDraw(squares):
    return(all(cell != "-" for row in squares for cell in row))

def randomMove():
    randInt = math.floor(9 * random.random())
    if randInt == 0:
        return(0, 2)
    if randInt == 1:
        return(1, 2)
    if randInt == 2:
        return(2, 2)
    if randInt == 3:
        return(0, 1)
    if randInt == 4:
        return(1, 1)
    if randInt == 5:
        return(2, 1)
    if randInt == 6:
        return(0, 0)
    if randInt == 7:
        return(1, 0)
    if randInt == 8:
        return(2, 0)

def minimax(squares, depth, isMax, maxDepth):
    if checkWin(squares, "x"):
        return(-1)
    elif checkWin(squares, "o"):
        return(1)
    elif checkDraw(squares) or depth == maxDepth:
        return(0)
    
    if isMax:
        # For maximizing player, recursively call moves to find maximum value
        maxVal = -float('inf')
        for i in range(3):
            for j in range(3):
                if squares[i][j] == "-":
                    squares[i][j] = 'o'
                    val = minimax(squares, depth+1, False, maxDepth)
                    squares[i][j] = "-"
                    maxVal = max(maxVal, val)
        return maxVal
    else:
        # For minimizing player, recursively call moves to find minimum value
        minVal = float('inf')
        for i in range(3):
            for j in range(3):
                if squares[i][j] == "-":
                    squares[i][j] = "x"
                    val = minimax(squares, depth+1, True, maxDepth)
                    squares[i][j] = "-"
                    minVal = min(minVal, val)
        return minVal

def getBestMove(squares, maxDepth):
    bestVal = -float('inf')
    bestMove = None
    
    for i in range(3):
        for j in range(3):
            if squares[i][j] == "-":
                squares[i][j] = "o"
                val = minimax(squares, 0, False, maxDepth)
                squares[i][j] = "-"
                if val > bestVal:
                    bestVal = val
                    bestMove = (i, j)

    return bestMove

s = int(sys.argv[1])
print("Seed = ", s)
random.seed(s)

squares = [["-" for i in range(3)] for j in range(3)]

for i in range(5):
    #Random player goes first
    randMove = randomMove()
    # print(randMove)

    while squares[randMove[0]][randMove[1]] == "x" or squares[randMove[0]][randMove[1]] == "o":
        # print("Triggered!")
        randMove = randomMove()
        # print(randMove)

    squares[randMove[0]][randMove[1]] = "x"
    display(squares)
    print()
    
    #Check for a win/draw
    if checkWin(squares, "x"):
        display(squares)
        print("Random player wins")
        break
    elif checkWin(squares, "o"):
        display(squares)
        print("Minimax wins")
        break
    elif checkDraw(squares):
        display(squares)
        print("Draw")
        break
    
    #Minimax goes second
    row, col = getBestMove(squares, 9)
    squares[row][col] = "o"
    
    #Check for a win/draw
    if checkWin(squares, "x"):
        display(squares)
        print("Random player wins")
        break
    elif checkWin(squares, "o"):
        display(squares)
        print("Minimax wins")
        break
    elif checkDraw(squares):
        display(squares)
        print("Draw")
        break
    
    display(squares)
    print()
    
# display(squares)