from tkinter import *
import random
from tkinter import messagebox


# ---------- Colors ----------
BG = "#171525"
PRIMARY = "#4B2DB8"
LIGHT_PURPLE = "#A78BFA"
TEXT = "#F5F3FF"
INPUT_BG = "#242139"
HEART = "#FF5C8A"
BUTTON_TEXT = "#000000"


def set_number(level):
    if level == 'easy':
        hearts = 4
        number = random.randint(1, 20)

    elif level == 'medium':
        hearts = 5
        number = random.randint(1, 50)

    elif level == 'hard':
        hearts = 7
        number = random.randint(1, 100)

    return hearts, number


def first_page():

    def submit():
        inp = inputtxt.get().strip()

        if inp == "":
            messagebox.showerror(
                "Error",
                "Please enter your name!"
            )
            return

        root.destroy()
        second_page(inp)

    root = Tk()
    root.title("Guess Number Game")
    root.geometry("400x500")
    root.configure(bg=BG)

    first_text = Label(
        root,
        text="Hi, Welcome to my game",
        font=('Helvetica', 20, 'bold'),
        bg=BG,
        fg=TEXT
    )
    first_text.place(y=70, relx=0.5, anchor='center')

    second_text = Label(
        root,
        text="Enter your name",
        font=('Helvetica', 16),
        bg=BG,
        fg=LIGHT_PURPLE
    )
    second_text.place(y=120, relx=0.5, anchor='center')

    inputtxt = Entry(
        root,
        bg=INPUT_BG,
        fg=TEXT,
        insertbackground=TEXT,
        font=('Helvetica', 12),
        relief='flat'
    )
    inputtxt.place(
        y=165,
        relx=0.5,
        anchor='center',
        width=250,
        height=35
    )

    first_button = Button(
        root,
        text="Let's Play",
        font=('Helvetica', 15, 'bold'),
        bg=PRIMARY,
        fg=BUTTON_TEXT,
        activebackground=LIGHT_PURPLE,
        activeforeground=BUTTON_TEXT,
        relief='flat',
        cursor='hand2',
        command=submit
    )
    first_button.place(
        y=230,
        relx=0.5,
        anchor='center',
        width=250,
        height=45
    )

    root.mainloop()


def second_page(player_name):

    def submit(level):
        root.destroy()
        third_page(level, player_name)

    root = Tk()
    root.title("Guess Number Game")
    root.geometry("400x500")
    root.configure(bg=BG)

    greeting_text = 'Hi ' + player_name

    first_text = Label(
        root,
        text=greeting_text,
        font=('Helvetica', 20, 'bold'),
        bg=BG,
        fg=TEXT
    )
    first_text.place(y=80, relx=0.5, anchor='center')

    second_text = Label(
        root,
        text='Choose level of difficulty',
        font=('Helvetica', 16),
        bg=BG,
        fg=LIGHT_PURPLE
    )
    second_text.place(y=130, relx=0.5, anchor='center')

    easy_button = Button(
        root,
        text="Easy",
        font=('Helvetica', 12, 'bold'),
        bg=PRIMARY,
        fg=BUTTON_TEXT,
        activebackground=LIGHT_PURPLE,
        activeforeground=BUTTON_TEXT,
        relief='flat',
        cursor='hand2',
        command=lambda: submit("easy")
    )
    easy_button.place(
        y=190,
        relx=0.5,
        anchor='center',
        width=300,
        height=45
    )

    medium_button = Button(
        root,
        text="Medium",
        font=('Helvetica', 12, 'bold'),
        bg=PRIMARY,
        fg=BUTTON_TEXT,
        activebackground=LIGHT_PURPLE,
        activeforeground=BUTTON_TEXT,
        relief='flat',
        cursor='hand2',
        command=lambda: submit("medium")
    )
    medium_button.place(
        y=245,
        relx=0.5,
        anchor='center',
        width=300,
        height=45
    )

    hard_button = Button(
        root,
        text="Hard",
        font=('Helvetica', 12, 'bold'),
        bg=PRIMARY,
        fg=BUTTON_TEXT,
        activebackground=LIGHT_PURPLE,
        activeforeground=BUTTON_TEXT,
        relief='flat',
        cursor='hand2',
        command=lambda: submit("hard")
    )
    hard_button.place(
        y=300,
        relx=0.5,
        anchor='center',
        width=300,
        height=45
    )

    root.mainloop()


def third_page(level, player_name):

    hearts, number = set_number(level)

    # Set the allowed range
    if level == 'easy':
        min_number = 1
        max_number = 20

    elif level == 'medium':
        min_number = 1
        max_number = 50

    else:
        min_number = 1
        max_number = 100

    def write_to_file(condition):
        with open('log.txt', 'a') as file:
            file.write(player_name + " " + condition + '\n')

    def play_game(inp):
        nonlocal hearts

        guess = int(inp)

        if guess == number:
            return 1

        hearts -= 1
        hearts_text['text'] = str(hearts)

        if guess > number:
            return 2

        else:
            return 3

    def submit():

        inp = inputtxt.get().strip()

        # Check empty input
        if inp == "":
            messagebox.showerror(
                "Error",
                "Please enter a number!"
            )
            return

        # Check invalid input
        try:
            guess = int(inp)

        except ValueError:
            messagebox.showerror(
                "Error",
                "Please enter a valid number!"
            )
            return

        # Check number range
        if guess < min_number or guess > max_number:
            messagebox.showerror(
                "Error",
                f"Please enter a number between {min_number} and {max_number}!"
            )
            return

        result = play_game(inp)

        if hearts <= 0:
            messagebox.showerror(
                "Sorry",
                "You lost! Number was " + str(number)
            )
            write_to_file("lost")
            root.destroy()
            fourth_page()
            return

        if result == 1:
            messagebox.showinfo(
                "Congrats",
                "You won!"
            )
            write_to_file("won")
            root.destroy()
            fourth_page()
            return

        elif result == 2:
            messagebox.showerror(
                "Wrong answer",
                "Go down!"
            )

        else:
            messagebox.showerror(
                "Wrong answer",
                "Go up!"
            )

        inputtxt.delete(0, END)

    root = Tk()
    root.title("Guess Number Game")
    root.geometry("400x500")
    root.configure(bg=BG)

    greeting_text = "Hi " + player_name

    first_text = Label(
        root,
        text=greeting_text,
        font=('Helvetica', 20, 'bold'),
        bg=BG,
        fg=TEXT
    )
    first_text.place(y=50, relx=0.5, anchor='center')

    second_text = Label(
        root,
        text='Choose a number',
        font=('Helvetica', 16),
        bg=BG,
        fg=LIGHT_PURPLE
    )
    second_text.place(y=90, relx=0.5, anchor='center')

    inputtxt = Entry(
        root,
        bg=INPUT_BG,
        fg=TEXT,
        insertbackground=TEXT,
        font=('Helvetica', 12),
        relief='flat'
    )
    inputtxt.place(
        y=150,
        relx=0.5,
        anchor='center',
        width=250,
        height=35
    )

    emoji = Label(
        root,
        text='❤️',
        font=('Helvetica', 20),
        bg=BG,
        fg=HEART
    )
    emoji.place(x=25, y=15)

    hearts_text = Label(
        root,
        text=str(hearts),
        font=('Helvetica', 20, 'bold'),
        bg=BG,
        fg=HEART
    )
    hearts_text.place(x=55, y=15)

    first_button = Button(
        root,
        text="Guess!",
        font=('Helvetica', 15, 'bold'),
        bg=PRIMARY,
        fg=BUTTON_TEXT,
        activebackground=LIGHT_PURPLE,
        activeforeground=BUTTON_TEXT,
        relief='flat',
        cursor='hand2',
        command=submit
    )
    first_button.place(
        y=200,
        relx=0.5,
        anchor='center',
        width=250,
        height=45
    )

    root.mainloop()


def fourth_page():

    def yes_action():
        root.destroy()
        first_page()

    def no_action():
        root.destroy()

    root = Tk()
    root.title("Guess Number Game")
    root.geometry("400x500")
    root.configure(bg=BG)

    greeting_text = Label(
        root,
        text="Do you want to play again?",
        font=('Helvetica', 20, 'bold'),
        bg=BG,
        fg=TEXT
    )
    greeting_text.place(
        y=100,
        relx=0.5,
        anchor='center'
    )

    btn_yes = Button(
        root,
        text='Yes',
        font=('Helvetica', 12, 'bold'),
        bg=PRIMARY,
        fg=BUTTON_TEXT,
        activebackground=LIGHT_PURPLE,
        activeforeground=BUTTON_TEXT,
        relief='flat',
        cursor='hand2',
        command=yes_action
    )
    btn_yes.place(
        y=170,
        width=100,
        height=40,
        relx=0.5,
        anchor='center'
    )

    btn_no = Button(
        root,
        text='No',
        font=('Helvetica', 12, 'bold'),
        bg="#302A4A",
        fg=BUTTON_TEXT,
        activebackground=LIGHT_PURPLE,
        activeforeground=BUTTON_TEXT,
        relief='flat',
        cursor='hand2',
        command=no_action
    )
    btn_no.place(
        y=220,
        width=100,
        height=40,
        relx=0.5,
        anchor='center'
    )

    root.mainloop()


first_page()
