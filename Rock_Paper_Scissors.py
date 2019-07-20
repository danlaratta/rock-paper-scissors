import tkinter as tk
import random

# sets up window, window's size, window's title, and window's background color
window = tk.Tk()
window.geometry("350x300")
window.title("Rock, Paper, Scissors")
window.configure(background='#66e0ff')


# game title
game_title = tk.Label(text="Rock, Paper, Scissors", bg="#66e0ff")
game_title.grid(row=0, column=0)

# simple directions for game
enter_pick = tk.Label(text="Enter Your Pick", bg="#66e0ff")
enter_pick.grid(row=1, column=0)

# validates the entry making sure its only letters
def validate(data):
    if data.isalpha():
        return True
    elif user_entry.get() == "":
        return False
    else:
        return False

# creates entry widget and creates a string variable to allow edits to the entry data (capitalize it)
var = tk.StringVar()
user_entry = tk.Entry(textvariable=var, highlightthickness=0, width=12)
user_entry.grid(row=2, column=0, padx=10, pady=5)
reg = window.register(validate)
user_entry.config(validate="key", validatecommand=(reg, "%P"))

# function capitalizes the first letter of the entry
def caps(*arg):
    var.set(var.get().capitalize())


# function checks to see who won
# noinspection PyRedundantParentheses
def check():
    # prints the PC pick
    pc_label = tk.Label(text="The PC guessed " + pc_pick, bg="#66e0ff")
    pc_label.grid(row=7, column=0)
    pc_label.after(5000, lambda: pc_label.destroy())

    # prints the user's pick
    user_label = tk.Label(text="Your pick was " + user_entry.get(), bg="#66e0ff")
    user_label.grid(row=8, column=0)
    user_label.after(5000, lambda: user_label.destroy())

    # checks who won as well as makes sure entry is text
    if (pc_pick == user_entry.get()):
        same_label = tk.Label(text="You both chose " + pc_pick, bg="#66e0ff")
        same_label.grid(row=9, column=0)
        same_label.after(5000, lambda: same_label.destroy())
    elif (pc_pick == "Rock" and user_entry.get() == "Scissors"):
        pc_won = tk.Label(text="Sorry, you lose :(", bg="#66e0ff")
        pc_won.grid(row=9, column=0)
        pc_won.after(5000, lambda: pc_won.destroy())
    elif (pc_pick == "Paper" and user_entry.get() == "Rock"):
        pc_won = tk.Label(text="Sorry, you lose :(", bg="#66e0ff")
        pc_won.grid(row=9, column=0)
        pc_won.after(5000, lambda: pc_won.destroy())
    elif (pc_pick == "Scissors" and user_entry.get() == "Paper"):
        pc_won = tk.Label(text="Sorry, you lose :(", bg="#66e0ff")
        pc_won.grid(row=9, column=0)
        pc_won.after(5000, lambda: pc_won.destroy())
    elif (user_entry.get() == "Rock" and pc_pick == "Scissors"):
        user_won = tk.Label(text="Congratulations, you won :)", bg="#66e0ff")
        user_won.grid(row=9, column=0)
        user_won.after(5000, lambda: user_won.destroy())
    elif (user_entry.get() == "Paper" and pc_pick == "Rock"):
        user_won = tk.Label(text="Congratulations, you won :)", bg="#66e0ff")
        user_won.grid(row=9, column=0)
        user_won.after(5000, lambda: user_won.destroy())
    elif (user_entry.get() == "Scissors" and pc_pick == "Paper"):
        user_won = tk.Label(text="Congratulations, you won :)", bg="#66e0ff")
        user_won.grid(row=9, column=0)
        user_won.after(5000, lambda: user_won.destroy())


# performs the actions of the other functions when the button is clicked
def click():
    caps()
    check()
    user_entry.delete(0, "end")


# creates the submit button
submit_btn = tk.Button(text="Enter", command=click)
submit_btn.grid(row=3, column=0)

# makes the stringvar read only
var.trace("r", caps)

# list of possible picks
pick_list = ["Rock", "Paper", "Scissors"]

# randomly chooses a list item as the pick for the PC
pc_pick = random.choice(pick_list)


window.mainloop()



