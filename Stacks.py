import tkinter.ttk
from tkinter import *

Staxs = Tk()


def showstaxs():
    pass


def donothing():
    pass


Staxs.geometry("404x515")

Staxs.title("MTG Stacks")


def clear():
    pass


effects = [
    "Add/Remove Counters",
    "Copied Spell",
    "Counter Spell",
    "ETB",
    "LTB",
    "Spell Effect",
    "Trigger"
]


class Background:
    StaxsBg = Canvas(Staxs, bg='blue', height=415, width=415)
    StaxsBg.pack()
    interaction_field = Canvas(Staxs, bg='white', height=390, width=235)
    interaction_field.place(x=160, y=10)


class P1Stuff:
    def __init__(self):
        player1label = Label(Staxs, text="Player 1 Effects", font=('Arial', 10))
        player1label.place(x=10, y=100)
        player1effect = tkinter.ttk.Combobox(Staxs, values=effects)

        def etb_selected():
            etb_label = Label(Staxs, text="ETB", bg='red', font=('Arial', 12))
            etb_label.pack()

        def ltb_selected():
            ltb_label = Label(Staxs, text="LTB", bg='red', font=('Arial', 12))
            ltb_label.pack()

        def counter_spell_selected():
            cs_label = Label(Staxs, text="Counter Spell", bg='red', font=('Arial', 12))
            cs_label.pack()

        def counters_selected():
            counters_label = Label(Staxs, text="Add/Remove Counters", bg='red', font=('Arial', 12))
            counters_label.pack()

        def trigger_selected():
            trigger_label = Label(Staxs, text="Trigger", bg='red', font=('Arial', 12))
            trigger_label.pack()

        def spell_effect_selected():
            spell_effect_label = Label(Staxs, text="Spell Effect", bg='red', font=('Arial', 12))
            spell_effect_label.pack()

        def copied_spell_selected():
            copied_spell_label = Label(Staxs, text="Copied Spell", bg='red', font=('Arial', 12))
            copied_spell_label.pack()

        def pick_effect(e=None):
            if player1effect.get() == "ETB":
                etb_selected()
            elif player1effect.get() == "LTB":
                ltb_selected()
            elif player1effect.get() == "Counter Spell":
                counter_spell_selected()
            elif player1effect.get() == "Add/Remove Counters":
                counters_selected()
            elif player1effect.get() == "Spell Effect":
                spell_effect_selected()
            elif player1effect.get() == "Copied Spell":
                copied_spell_selected()
            elif player1effect.get() == "Triggered":
                trigger_selected()

        player1effect.bind("<<ComboboxSelected>>", pick_effect)
        player1effect.place(x=10, y=125)


class P2Stuff:
    def __init__(self):
        player2label = Label(Staxs, text="Player 2 Effects", font="Arial, 10")
        player2label.place(x=10, y=150)
        player2effect = tkinter.ttk.Combobox(Staxs, values=effects)

        def etb_selected():
            etb_label = Label(Staxs, text="ETB", bg='blue', fg='white', font=('Arial', 12))
            etb_label.pack()

        def ltb_selected():
            ltb_label = Label(Staxs, text="LTB", bg='blue', fg='white', font=('Arial', 12))
            ltb_label.pack()

        def counter_spell_selected():
            cs_label = Label(Staxs, text="Counter Spell", bg='blue', fg='white', font=('Arial', 12))
            cs_label.pack()

        def counters_selected():
            counters_label = Label(Staxs, text="Add/Remove Counters", bg='blue', fg='white', font=('Arial', 12))
            counters_label.pack()

        def trigger_selected():
            trigger_label = Label(Staxs, text="Trigger", bg='blue', fg='white', font=('Arial', 12))
            trigger_label.pack()

        def spell_effect_selected():
            spell_effect_label = Label(Staxs, text="Spell Effect", bg='blue', fg='white', font=('Arial', 12))
            spell_effect_label.pack()

        def copied_spell_selected():
            copied_spell_label = Label(Staxs, text="Copied Spell", bg='blue', fg='white', font=('Arial', 12))
            copied_spell_label.pack()

        def pick_effect(e=None):
            if player2effect.get() == "ETB":
                etb_selected()
            elif player2effect.get() == "LTB":
                ltb_selected()
            elif player2effect.get() == "Counter Spell":
                counter_spell_selected()
            elif player2effect.get() == "Add/Remove Counters":
                counters_selected()
            elif player2effect.get() == "Spell Effect":
                spell_effect_selected()
            elif player2effect.get() == "Copied Spell":
                copied_spell_selected()
            elif player2effect.get() == "Triggered":
                trigger_selected()

        player2effect.bind("<<ComboboxSelected>>", pick_effect)
        player2effect.place(x=10, y=175)


class P3Stuff:
    def __init__(self):
        player3label = Label(Staxs, text="Player 3 Effects", font="Arial, 10")
        player3label.place(x=10, y=200)
        player3effect = tkinter.ttk.Combobox(Staxs, values=effects)

        def etb_selected():
            etb_label = Label(Staxs, text="ETB", bg='green', font=('Arial', 12))
            etb_label.pack()

        def ltb_selected():
            ltb_label = Label(Staxs, text="LTB", bg='green', font=('Arial', 12))
            ltb_label.pack()

        def counter_spell_selected():
            cs_label = Label(Staxs, text="Counter Spell", bg='green', font=('Arial', 12))
            cs_label.pack()

        def counters_selected():
            counters_label = Label(Staxs, text="Add/Remove Counters", bg='green', font=('Arial', 12))
            counters_label.pack()

        def trigger_selected():
            trigger_label = Label(Staxs, text="Trigger", bg='green', font=('Arial', 12))
            trigger_label.pack()

        def spell_effect_selected():
            spell_effect_label = Label(Staxs, text="Spell Effect", bg='green', font=('Arial', 12))
            spell_effect_label.pack()

        def copied_spell_selected():
            copied_spell_label = Label(Staxs, text="Copied Spell", bg='green', font=('Arial', 12))
            copied_spell_label.pack()

        def pick_effect(e=None):
            if player3effect.get() == "ETB":
                etb_selected()
            elif player3effect.get() == "LTB":
                ltb_selected()
            elif player3effect.get() == "Counter Spell":
                counter_spell_selected()
            elif player3effect.get() == "Add/Remove Counters":
                counters_selected()
            elif player3effect.get() == "Spell Effect":
                spell_effect_selected()
            elif player3effect.get() == "Copied Spell":
                copied_spell_selected()
            elif player3effect.get() == "Triggered":
                trigger_selected()

        player3effect.bind("<<ComboboxSelected>>", pick_effect)
        player3effect.place(x=10, y=225)


class P4Stuff:
    def __init__(self):
        player4label = Label(Staxs, text="Player 4 Effects", font="Arial, 10")
        player4label.place(x=10, y=250)
        player4effect = tkinter.ttk.Combobox(Staxs, values=effects)

        def etb_selected():
            etb_label = Label(Staxs, text="ETB", bg='purple', fg='white', font=('Arial', 12))
            etb_label.pack()

        def ltb_selected():
            ltb_label = Label(Staxs, text="LTB", bg='purple', fg='white', font=('Arial', 12))
            ltb_label.pack()

        def counter_spell_selected():
            cs_label = Label(Staxs, text="Counter Spell", bg='purple', fg='white', font=('Arial', 12))
            cs_label.pack()

        def counters_selected():
            counters_label = Label(Staxs, text="Add/Remove Counters", bg='purple', fg='white', font=('Arial', 12))
            counters_label.pack()

        def trigger_selected():
            trigger_label = Label(Staxs, text="Trigger", bg='purple', fg='white', font=('Arial', 12))
            trigger_label.pack()

        def spell_effect_selected():
            spell_effect_label = Label(Staxs, text="Spell Effect", bg='purple', fg='white', font=('Arial', 12))
            spell_effect_label.pack()

        def copied_spell_selected():
            copied_spell_label = Label(Staxs, text="Copied Spell", bg='purple', fg='white', font=('Arial', 12))
            copied_spell_label.pack()

        def pick_effect(e=None):
            if player4effect.get() == "ETB":
                etb_selected()
            elif player4effect.get() == "LTB":
                ltb_selected()
            elif player4effect.get() == "Counter Spell":
                counter_spell_selected()
            elif player4effect.get() == "Add/Remove Counters":
                counters_selected()
            elif player4effect.get() == "Spell Effect":
                spell_effect_selected()
            elif player4effect.get() == "Copied Spell":
                copied_spell_selected()
            elif player4effect.get() == "Triggered":
                trigger_selected()

        player4effect.bind("<<ComboboxSelected>>", pick_effect)
        player4effect.place(x=10, y=275)


class FunctionButtons:
    def __init__(self):
        remove = Button(Staxs, text="Remove Effect", font=("Arial", 10))
        remove.place(x=10, y=300)
        clearstack = Button(Staxs, text="Clear the Stack", font="Arial, 14", command=clear)
        clearstack.place(x=10, y=10)
        top_of_stack = Button(Staxs, text="Top of the Stack", font=("Arial", 10))
        top_of_stack.place(x=10, y=330)


Player1 = P1Stuff()
Player2 = P2Stuff()
Player3 = P3Stuff()
Player4 = P4Stuff()
Buttons = FunctionButtons()
Staxs.mainloop()
