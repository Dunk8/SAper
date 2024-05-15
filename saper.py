import tkinter as tk
from tkinter import messagebox
import random

def create_board(rows, cols, bombs):
    board = [[0 for _ in range(cols)] for _ in range(rows)]
    for _ in range(bombs):
        row, col = random.randint(0, rows-1), random.randint(0, cols-1)
        while board[row][col] == -1:
            row, col = random.randint(0, rows-1), random.randint(0, cols-1)
        board[row][col] = -1
        for r in range(row-1, row+2):
            for c in range(col-1, col+2):
                if 0 <= r < rows and 0 <= c < cols and board[r][c] != -1:
                    board[r][c] += 1
    return board

def reveal(board, buttons, row, col):
    if board[row][col] == -1:
        buttons[row][col].config(text='*', state='disabled')
        messagebox.showinfo('Game Over', 'You hit a bomb!')
        root.quit()  
    else:
        buttons[row][col].config(text=str(board[row][col]), state='disabled')
        if board[row][col] == 0:
            for r in range(row-1, row+2):
                for c in range(col-1, col+2):
                    if 0 <= r < rows and 0 <= c < cols and buttons[r][c]['state'] != 'disabled':
                        reveal(board, buttons, r, c)

# Функция для установки/удаления флажка на клетке
def toggle_flag(button):
    current_text = button.cget("text")
    if current_text == "":
        button.config(text="F")
    elif current_text == "F":
        button.config(text="")
        
def main():
    global root, rows, cols
    root = tk.Tk()
    root.title("Minesweeper")
    
    rows, cols, bombs = 10, 10, 10
    board = create_board(rows, cols, bombs)
    buttons = []
    for row in range(rows):
        button_row = []
        for col in range(cols):
            btn = tk.Button(root, width=3, height=1)
            btn.grid(row=row, column=col)
            btn.bind("<Button-1>", lambda event, r=row, c=col: reveal(board, buttons, r, c))
            btn.bind("<Button-3>", lambda event, btn=btn: toggle_flag(btn))
            button_row.append(btn)
        buttons.append(button_row)
    
    root.mainloop()

if __name__ == "__main__":
    main()  
