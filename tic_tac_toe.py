# import tkinter as tk
# from tkinter import messagebox

# def check_winner():
#     global winner
#     win_combos = [
#         [0,1,2], [3,4,5], [6,7,8],   # rows
#         [0,3,6], [1,4,7], [2,5,8],   # columns
#         [0,4,8], [2,4,6]             # diagonals
#     ]

#     for combo in win_combos:
#         b1 = buttons[combo[0]]["text"]
#         b2 = buttons[combo[1]]["text"]
#         b3 = buttons[combo[2]]["text"]

#         if b1 == b2 == b3 != "":
#             winner = True
#             buttons[combo[0]].config(bg="green")
#             buttons[combo[1]].config(bg="green")
#             buttons[combo[2]].config(bg="green")
#             messagebox.showinfo("Tic-Tac-Toe", f"Player {b1} WINS!")
#             root.quit()
#             return

# def button_click(index):
#     global winner
#     if buttons[index]["text"] == "" and not winner:
#         buttons[index]["text"] = current_player
#         check_winner()
#         if not winner:
#             toggle_player()

# def toggle_player():
#     global current_player
#     current_player = "X" if current_player == "O" else "O"
#     label.config(text=f"Player {current_player}'s turn")

# root = tk.Tk()
# root.title("Tic-Tac-Toe")

# buttons = []
# current_player = "X"
# winner = False

# # Create buttons
# for i in range(9):
#     btn = tk.Button(root, text="", font=("Arial", 24), width=5, height=2,
#                     command=lambda i=i: button_click(i))
#     btn.grid(row=i//3, column=i%3)
#     buttons.append(btn)

# # Label
# label = tk.Label(root, text=f"Player {current_player}'s turn", font=("Arial", 16))
# label.grid(row=3, column=0, columnspan=3)

# root.mainloop()
import tkinter as tk
from tkinter import messagebox

def check_winner():
    global winner
    win_combos = [
        [0,1,2], [3,4,5], [6,7,8], 
        [0,3,6], [1,4,7], [2,5,8], 
        [0,4,8], [2,4,6]
    ]

    for combo in win_combos:
        b1 = buttons[combo[0]]["text"]
        b2 = buttons[combo[1]]["text"]
        b3 = buttons[combo[2]]["text"]

        if b1 == b2 == b3 != "":
            winner = True
            buttons[combo[0]].config(bg="green")
            buttons[combo[1]].config(bg="green")
            buttons[combo[2]].config(bg="green")
            messagebox.showinfo("Tic-Tac-Toe", f"Player {b1} WINS!")
            restart_game()
            return

def restart_game():
    global moves, winner, current_player
    moves = 0
    winner = False
    current_player = "X"
    label.config(text=f"Player {current_player}'s turn")

    for btn in buttons:
        btn.config(text="", bg="SystemButtonFace")

def button_click(index):
    global moves
    if buttons[index]["text"] == "" and not winner:
        buttons[index]["text"] = current_player
        moves += 1
        check_winner()

        if moves == 9 and not winner:
            messagebox.showinfo("Tic-Tac-Toe", "Match Draw! No one wins.")
            restart_game()
            return

        if not winner:
            toggle_player()

def toggle_player():
    global current_player
    current_player = "X" if current_player == "O" else "O"
    label.config(text=f"Player {current_player}'s turn")

root = tk.Tk()
root.title("Tic-Tac-Toe")

buttons = []
current_player = "X"
winner = False
moves = 0

for i in range(9):
    btn = tk.Button(root, text="", font=("Arial", 24), width=5, height=2,
                    command=lambda i=i: button_click(i))
    btn.grid(row=i//3, column=i%3)
    buttons.append(btn)

label = tk.Label(root, text=f"Player {current_player}'s turn", font=("Arial", 16))
label.grid(row=3, column=0, columnspan=3)

root.mainloop()
