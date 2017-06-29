# ticTacToe from Chapter 5

import sys
theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

def gameOver(board):
    # Check horizontals
    if board['top-L'] != '' and board['top-L'] == board['top-M'] == board['top-R']:
        return board['top-L']
    elif board['mid-L'] != '' and board['mid-L'] == board['mid-M'] == board['mid-R']:
        return board['mid-L']
    elif board['low-L'] != '' and board['low-L'] == board['low-M'] == board['low-R']:
        return board['low-L']
    # Check diagonals
    elif board['top-L'] != '' and board['top-L'] == board['mid-M'] == board['low-R']:
        return board['top-L']
    elif board['low-L'] != '' and board['low-L'] == board['top-M'] == board['top-R']:
        return board['low-L']
    # Check verticles
    elif board['top-L'] != '' and board['top-L'] == board['mid-L'] == board['low-L']:
        return board['top-L']
    elif board['top-M'] != '' and board['top-M'] == board['mid-M'] == board['low-M']:
        return board['top-M']
    elif board['top-R'] != '' and board['top-R'] == board['mid-R'] == board['low-R']:
        return board['top-R']
    else:
        return ''

def playGame():
    turn = 'X'
    for i in range(9):
        printBoard(theBoard)
        print('Turn for ' + turn + '. Move on which space?')
        move = input()
        theBoard[move] = turn
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'

        winner = gameOver(theBoard)
        if winner == 'X' or winner == 'O':
            printBoard(theBoard)
            print('Game Over. Player ' + winner + ' wins!')
            break
            
playGame()
