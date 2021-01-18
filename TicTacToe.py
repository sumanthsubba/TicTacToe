#!/usr/bin/env python
# coding: utf-8

# In[1]:


from IPython.display import clear_output

def display_board(board):
    clear_output()  # Remember, this only works in jupyter!
    
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')


# In[2]:


def player_input():
    marker = ''
    
    while marker != 'X' and marker != 'O':
        marker = input('Player 1: Do you want to be X or O? ')

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')


# In[3]:


def place_marker(board, marker, position):
    board[position] = marker


# In[4]:


def win_check(board,mark):
    
    if ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)): # diagonal
        return True 


# In[5]:


import random

def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'


# In[6]:


def space_check(board, position):
    
    if board[position] == ' ':
        return True


# In[7]:


def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i) == True:
            return False
    return True


# In[8]:


def player_choice(board):
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or space_check(board, position) == False:
        position = int(input('Choose your next position: (1-9) '))
     
    return position


# In[9]:


def replay():
    
    wannareplay = input('Do you want to play again? Enter Yes or No: ')
    
    if wannareplay.lower()[0] == 'y':
        return True
    else:
        return False


# In[ ]:


print('Welcome to Tic Tac Toe!')

while True:
    # Reset the board
    theBoard = [' ']*10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first.')
    
    play_game = input('Are you ready to play? Enter Yes or No.')
    
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on == True:
        if turn == 'Player 1':
            # Player1's turn.
            
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1_marker, position)

            if win_check(theBoard, player1_marker) == True:
                display_board(theBoard)
                print('Congratulations! Player 1 has won the game!')
                game_on = False
            else:
                if full_board_check(theBoard) == True:
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'

        else:
            # Player2's turn.
            
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)

            if win_check(theBoard, player2_marker) == True:
                display_board(theBoard)
                print('Congratulations! Player 2 has won the game!')
                game_on = False
            else:
                if full_board_check(theBoard) == True:
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'

    if replay() == False:
        break


# In[ ]:





# In[ ]:





# In[ ]:




