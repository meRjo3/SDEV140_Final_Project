from tkinter import *

Two_player = Tk()


def showstaxs():
    pass


def donothing():
    pass


class Two_Player_Page:
    Two_player.geometry("404x415")
    Two_player.title("MTG Stacks")
    label = Label(Two_player, text="MTG Stacks", font=('Arial', 20))
    label.place(x=130, y=0)

    menubar = Menu(Two_player)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Staxs", command=showstaxs)
    filemenu.add_command(label="Open", command=donothing)
    filemenu.add_command(label="Save", command=donothing)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=Two_player.quit)
    menubar.add_cascade(label="File", menu=filemenu)

    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label="Help Index", command=donothing)
    helpmenu.add_command(label="About...", command=donothing)
    menubar.add_cascade(label="Help", menu=helpmenu)


class Player1:
    def __init__(self):
        def player1lifeup():
            # Make it do the math!
            nonlocal player1lifetotal
            player1lifetotal += 1
            displayp1life["text"] = player1lifetotal
            print(player1lifetotal)

        def player1lifedown():
            nonlocal player1lifetotal
            player1lifetotal -= 1
            displayp1life["text"] = player1lifetotal
            print(player1lifetotal)

        player1lifetotal = 40
        player1canvas = Canvas(Two_player, bg='red', height=190, width=400)
        player1canvas.place(x=0, y=30)
        player1frame = Label(Two_player, text="Player One HP", font=('Arial', 18))
        player1frame.place(x=125, y=40)
        displayp1life = Label(Two_player, text=player1lifetotal, font=('Arial', 20))
        displayp1life.place(x=195, y=100)

        p1plusbutton = Button(Two_player, command=player1lifeup, text="+", height=1, width=1, font=('Arial', 12), )
        p1plusbutton.place(x=193, y=150)
        p1minusbutton = Button(Two_player, text="-", height=1, width=1, font=('Arial', 12), command=player1lifedown)
        p1minusbutton.place(x=215, y=150)


class Player2:
    def __init__(self):
        def player2lifeup():
            # Make it do the math!
            nonlocal player2lifetotal
            player2lifetotal += 1
            displayp2life["text"] = player2lifetotal
            print(player2lifetotal)

        def player2lifedown():
            nonlocal player2lifetotal
            player2lifetotal -= 1
            displayp2life["text"] = player2lifetotal
            print(player2lifetotal)

        player2lifetotal = 40
        player2canvas = Canvas(Two_player, bg='blue', height=190, width=400)
        player2canvas.place(x=0, y=200)
        player2frame = Label(Two_player, text="Player Two HP", font=('Arial', 18))
        player2frame.place(x=125, y=240)
        displayp2life = Label(Two_player, text=player2lifetotal, font=('Arial', 20))
        displayp2life.place(x=195, y=300)

        p2plusbutton = Button(Two_player, command=player2lifeup, text="+", height=1, width=1, font=('Arial', 12), )
        p2plusbutton.place(x=193, y=350)
        p2minusbutton = Button(Two_player, text="-", height=1, width=1, font=('Arial', 12), command=player2lifedown)
        p2minusbutton.place(x=215, y=350)


P1 = Player1()
P2 = Player2()
Two_player.mainloop()
