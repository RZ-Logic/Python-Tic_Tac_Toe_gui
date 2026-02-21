# Unbeatable Tic Tac Toe (Minimax AI) 🎮

A graphical Tic Tac Toe game built in Python using the Tkinter library. Play against an unbeatable AI opponent powered by the classic Minimax algorithm.

## Features
* **Unbeatable AI:** The computer uses the Minimax algorithm to calculate every possible future move, ensuring it will always win or force a tie.
* **Optimized Decision Making:** The AI incorporates "depth" into its calculations, meaning it actively seeks the fastest possible path to victory rather than just a guaranteed win.
* **Graphical Interface:** A clean, interactive GUI built with Python's native Tkinter library.
* **Randomized Starts:** The game randomly decides whether the human or the AI makes the first move to keep gameplay varied.

## Under the Hood: The Minimax Algorithm


This project demonstrates the application of **Game Theory** in AI. The Minimax algorithm works by simulating all possible future states of the game board. It scores these end-states (+10 for an AI win, -10 for a human win, 0 for a tie) and works backward to choose the move that maximizes its own score while minimizing the human's score. 

## Prerequisites
* Python 3.x
* *Note: Tkinter is included in the standard Python library, so no additional installations are required.*

## How to Run

Clone the repository and run the script directly from your terminal.

### Windows
Open Command Prompt or PowerShell:
```cmd
python tic_tac_toe_gui.py