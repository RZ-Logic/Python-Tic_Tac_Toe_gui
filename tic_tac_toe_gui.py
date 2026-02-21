"""
Tic Tac Toe - AI Opponent (Minimax Algorithm)
A graphical Tic Tac Toe game built with Tkinter.
Features an unbeatable AI opponent powered by the Minimax algorithm.
"""

import tkinter as tk
from tkinter import messagebox
import random

class TicTacToeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe - AI Opponent")
        self.root.configure(bg="#2E4053")

        self.board = [" "] * 9
        self.human_player = "O"
        self.ai_player = "X"
        self.buttons = []
        self.ai_turn = False

        self.create_widgets()
        self.start_game()

    def create_widgets(self):
        """Builds the 3x3 grid and the bottom control panel."""
        for i in range(9):
            btn = tk.Button(
                self.root,
                text=" ",
                font=("Arial", 30, "bold"),
                width=5,
                height=2,
                bg="#D6EAF8",
                fg="black",
                command=lambda idx=i: self.player_move(idx)
            )
            btn.grid(row=i // 3, column=i % 3, padx=5, pady=5)
            self.buttons.append(btn)

        # Bottom frame for controls + watermark
        bottom_frame = tk.Frame(self.root, bg="#2E4053")
        bottom_frame.grid(row=3, column=0, columnspan=3, sticky="we", padx=10, pady=(0, 10))
        bottom_frame.columnconfigure(0, weight=1)
        bottom_frame.columnconfigure(1, weight=1)

        reset_btn = tk.Button(
            bottom_frame,
            text="Reset Game",
            font=("Arial", 12),
            command=self.reset_game,
            bg="#34495E",
            fg="white"
        )
        reset_btn.grid(row=0, column=0, sticky="w")

        watermark = tk.Label(
            bottom_frame,
            text="rizwan",
            font=("Arial", 10, "italic"),
            bg="#2E4053",
            fg="#B0B0B0"  
        )
        watermark.grid(row=0, column=1, sticky="e")

    def player_move(self, idx):
        """Handles the human player's click event."""
        if self.board[idx] == " " and not self.ai_turn:
            self.board[idx] = self.human_player
            self.update_button(idx)
            self.root.update() # Force UI to draw the move before popping up the message box
            
            if self.check_winner() == self.human_player:
                self.end_game("Congratulations! You (O) win!")
                return
            elif self.is_board_full():
                self.end_game("It's a tie!")
                return
                
            self.ai_turn = True
            self.root.after(500, self.ai_move)

    def ai_move(self):
        """Calculates and executes the AI's best move."""
        move = self.get_best_move()
        if move is not None:
            self.board[move] = self.ai_player
            self.update_button(move)
            self.root.update() # Force UI to draw the move
            
            if self.check_winner() == self.ai_player:
                self.end_game("Just like real life, AI beat you here as well!")
                return
            elif self.is_board_full():
                self.end_game("It's a tie!")
                return
        self.ai_turn = False

    def update_button(self, idx):
        """Updates the visual state of a button on the grid."""
        symbol = self.board[idx]
        btn = self.buttons[idx]
        btn.config(text=symbol)
        if symbol == "X":
            btn.config(fg="red")
        elif symbol == "O":
            btn.config(fg="blue")
        else:
            btn.config(fg="black")

    def check_winner(self):
        """Checks all winning combinations to see if a player has won."""
        # Check rows
        for i in range(0, 9, 3):
            if self.board[i] == self.board[i+1] == self.board[i+2] != " ":
                return self.board[i]
        # Check columns
        for i in range(3):
            if self.board[i] == self.board[i+3] == self.board[i+6] != " ":
                return self.board[i]
        # Check diagonals
        if self.board[0] == self.board[4] == self.board[8] != " ":
            return self.board[0]
        if self.board[2] == self.board[4] == self.board[6] != " ":
            return self.board[2]
        return None

    def is_board_full(self):
        return " " not in self.board

    def minimax(self, depth, is_maximizing):
        """
        Minimax algorithm to evaluate the best possible moves.
        Incorporates 'depth' to prioritize faster wins and prolonged losses.
        """
        winner = self.check_winner()
        if winner == self.ai_player:
            return 10 - depth  # AI wins (faster is better)
        elif winner == self.human_player:
            return -10 + depth # Human wins (slower is better)
        elif self.is_board_full():
            return 0

        if is_maximizing:
            best_score = float("-inf")
            for i in range(9):
                if self.board[i] == " ":
                    self.board[i] = self.ai_player
                    score = self.minimax(depth + 1, False)
                    self.board[i] = " "
                    best_score = max(score, best_score)
            return best_score
        else:
            best_score = float("inf")
            for i in range(9):
                if self.board[i] == " ":
                    self.board[i] = self.human_player
                    score = self.minimax(depth + 1, True)
                    self.board[i] = " "
                    best_score = min(score, best_score)
            return best_score

    def get_best_move(self):
        """Triggers the Minimax algorithm to find the optimal next move."""
        best_score = float("-inf")
        best_move = None
        for i in range(9):
            if self.board[i] == " ":
                self.board[i] = self.ai_player
                # Call minimax starting at depth 0, next turn is minimizing (human)
                score = self.minimax(0, False)
                self.board[i] = " "
                if score > best_score:
                    best_score = score
                    best_move = i
        return best_move

    def end_game(self, message):
        """Disables the board and shows the end game message."""
        messagebox.showinfo("Game Over", message)
        for btn in self.buttons:
            btn.config(state="disabled")

    def reset_game(self):
        """Clears the board and starts a new game."""
        self.board = [" "] * 9
        for btn in self.buttons:
            btn.config(text=" ", state="normal", fg="black")
        self.start_game()

    def start_game(self):
        """Randomly decides who goes first."""
        self.ai_turn = random.choice([True, False])
        if self.ai_turn:
            # If AI goes first, add a slight delay so it doesn't feel instantaneous
            self.root.after(500, self.ai_move)

if __name__ == "__main__":
    root = tk.Tk()
    game_app = TicTacToeGUI(root)
    root.mainloop()