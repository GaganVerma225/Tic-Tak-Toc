# Make tic tac toe game using GUI

import tkinter as tk
from tkinter import messagebox
import random

# Function to display tic tac toe board
def display_board():
    for i in range(3):
        for j in range(3):
            b = tk.Button(root, text=" ", font=("Arial", 20), width=5, height=2, command=lambda row=i, col=j: user_click(row, col))
            b.grid(row=i, column=j)
            buttons[i][j] = b

# Function to display winner
def display_winner(winner):
    global user_turn
    if winner == "X":
        messagebox.showinfo("Game Result", "You won!")
    elif winner == "O":
        messagebox.showinfo("Game Result", "Computer won!")
    elif winner == "tie":
        messagebox.showinfo("Game Result", "It's a tie!")
    else:
        messagebox.showinfo("Game Result", "Error!")
    user_turn = False
    reset()

# Function to check if there is a winner
def check_winner():
    global winner
    winner = None

# Check if there is a winner in rows
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] != " ":
            winner = board[row][0]
            display_winner(winner)
            return True

# Check if there is a winner in columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            winner = board[0][col]
            display_winner(winner)

# Check if there is a winner in diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        winner = board[0][0]
        display_winner(winner)
    elif board[0][2] == board[1][1] == board[2][0] != " ":
        winner = board[0][2]
        display_winner(winner)

# Check if there is a tie
    if winner == None and empty_spaces() == False:
        winner = "tie"
        display_winner(winner)

# Function to check if there is an empty space


def empty_spaces():
    for row in range(3):
        for col in range(3):
            if board[row][col] == " ":
                return True
    return False
# Function to make computer move


def computer_move():
    global row, col, user_turn
    row = random.randint(0, 2)
    col = random.randint(0, 2)
    while board[row][col] != " ":
        row = random.randint(0, 2)
        col = random.randint(0, 2)
    board[row][col] = "O"
    buttons[row][col]["text"] = "O"
    user_turn = True
# Function to make user move


def user_click(row, col):
    global user_turn
    if user_turn == True:
        if board[row][col] == " ":
            board[row][col] = "X"
            buttons[row][col]["text"] = "X"
            user_turn = False
            check_winner()
            computer_move()
            check_winner()
        else:
            messagebox.showinfo("Tic Tac Toe", "That space is already taken!")
    else:
        messagebox.showinfo("Tic Tac Toe", "It's not your turn!")
# Function to reset the game


def reset():
    global board, user_turn
    board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    user_turn = True
    display_board()


# Main program
root = tk.Tk()
root.title("Tic Tac Toe")
board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
buttons = [{}, {}, {}]
user_turn = True
display_board()
reset_button = tk.Button(root, text="Reset", font=(
    "Arial", 20), width=5, height=2, command=reset)
reset_button.grid(row=3, column=1)
root.mainloop()
# End
