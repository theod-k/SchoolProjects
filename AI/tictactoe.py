#!/usr/bin/env python
import sys
import random
import math

def minimax(squares):
    # print(squares)
    value = getScore(squares)
    if endState(squares):
        # print(endState(squares))
        return(value)
    
    if player(squares) == "o":
        value = float('-inf')
        for a in actions(squares):
            score = minimax(result(squares, a))
            if score > value:
                value = score
        return(value)
    
    if player(squares) == "x":
        value = float('inf')
        for b in actions(squares):
            score = minimax(result(squares, b))
            if score < value:
                value = score
        return(value)

def endState(squares):
    # First check for a win
    # Rows
    if squares[6] == squares[7] == squares[8] != "-":
        return(True)
    if squares[3] == squares[4] == squares[5] != "-":
        return(True)
    if squares[0] == squares[1] == squares[2] != "-":
        return(True)
    
    # Columns
    if squares[6] == squares[3] == squares[0] != "-":
        return(True)
    if squares[7] == squares[4] == squares[1] != "-":
        return(True)
    if squares[8] == squares[5] == squares[2] != "-":
        return(True)
    
    # Diagonals
    if squares[6] == squares[4] == squares[2] != "-":
        return(True)
    if squares[8] == squares[4] == squares[0] != "-":
        return(True)
    
    # Next check if board is full
    for i in squares:
        # print(i)
        if i == "-":
            return(False)
    return(True)
        
def getScore(squares):
    # Check win for players
    # Rows
    if squares[6] == squares[7] == squares[8] == "o":
        return(1)
    if squares[3] == squares[4] == squares[5] == "o":
        return(1)
    if squares[0] == squares[1] == squares[2] == "o":
        return(1)
    
    if squares[6] == squares[7] == squares[8] == "x":
        return(-1)
    if squares[3] == squares[4] == squares[5] == "x":
        return(-1)
    if squares[0] == squares[1] == squares[2] == "x":
        return(-1)
    
    # Columns
    if squares[6] == squares[3] == squares[0] == "o":
        return(1)
    if squares[7] == squares[4] == squares[1] == "o":
        return(1)
    if squares[8] == squares[5] == squares[2] == "o":
        return(1)
    
    if squares[6] == squares[3] == squares[0] == "x":
        return(-1)
    if squares[7] == squares[4] == squares[1] == "x":
        return(-1)
    if squares[8] == squares[5] == squares[2] == "x":
        return(-1)
    
    # Diagonals
    if squares[6] == squares[4] == squares[2] == "o":
        return(1)
    if squares[8] == squares[4] == squares[0] == "o":
        return(1)
    
    if squares[6] == squares[4] == squares[2] == "x":
        return(-1)
    if squares[8] == squares[4] == squares[0] == "x":
        return(-1)
    
    #Otherwise return a draw
    return(0)

def player(squares):
    xCount = 0
    oCount = 0
    
    for i in squares:
        if i == "x":
            xCount = xCount+1
        if i == "o":
            oCount = oCount+1
    
    if xCount > oCount:
        return("o")
    else:
        return("x")
    
def notPlayer(squares):
    if player(squares) == "x":
        return("o")
    else:
        return("x")
    
def actions(squares):
    possibilities = []
    for i in range(0, 8):
       if squares[i] == "-":
           possibilities.append(i)
    # print(possibilities)
    return(possibilities)

def result(squares, action):
    resulting = squares.copy()
    resulting[action] = player(squares)
    return(resulting)

def printBoard(squares):
    print(f"{squares[6]},{squares[7]},{squares[8]}")
    print(f"{squares[3]},{squares[4]},{squares[5]}")
    print(f"{squares[0]},{squares[1]},{squares[2]}")
    print("\n")
    
def findMove(squares):
    bestVal = -1000
    bestMove = -1
    for i in range(8):
        if squares[i] == "-":
            squares[i] = player(squares)
        
            moveVal = minimax(squares)
            squares[i] = "-"
            
            if(moveVal > bestVal):
                bestMove = i
                bestVal = moveVal
    return(bestMove)

s = int(sys.argv[1])
print("Seed = ", s)
random.seed(s)

taken = [False, False, False, False, False, False, False, False, False]
squares = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]

for i in range(0,5):
    # Running random first player
    rNum = math.floor(9 * random.random())
    while(taken[rNum] != False):
        rNum = math.floor(9 * random.random())
    # print(rNum)
    squares[rNum] = "x"
    taken[rNum] = True
    # printBoard(squares)
    squares2 = squares.copy()

    # Second player minimax
    print(squares)
    minimaxIndex = findMove(squares)
    if(minimaxIndex == -1):
        printBoard(squares)
        break
    print(minimaxIndex)
    squares2[minimaxIndex] = "o"
    taken[minimaxIndex] = True
    squares = squares2.copy()

    printBoard(squares)

# print(taken)
# printBoard(squares)