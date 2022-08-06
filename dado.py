import random
from tkinter import*

class Dice_roller(object):
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()


        self.label = Label(master, font=("times", 200))
        button = Button(master, text="roll dice", command=self.roll)
        button.place(x=200, y=0)

    def roll(self):
        symbols = ["\u2680", "\2681", "\2682", "\2683", "\2684", "\2685"]
        self.label.config(text=f"{random.choice(symbols)}{random.choice(symbols)}")
        self.label.pack()


if_name_ == '__main__'
    root = Tk()
    root.title("dice roller")
    root.geometry("500x300")
    Dice_roller(root)
    root.mainloop()
